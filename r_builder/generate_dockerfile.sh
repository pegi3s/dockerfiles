#!/bin/bash

# Check if jq is installed (used for parsing JSON)
if ! command -v jq &> /dev/null
then
    echo "Error: jq is not installed. Please install jq to use this script."
    exit 1
fi

# Input JSON file
JSON_FILE=$1
if [ ! -f "$JSON_FILE" ]; then
    echo "Error: JSON file '$JSON_FILE' does not exist."
    exit 1
fi

# Initialize DRY_RUN to 0
DRY_RUN=0

# Parse additional arguments
shift
while (( "$#" )); do
    case "$1" in
        --dry-run)
            DRY_RUN=1
            shift
            ;;
        --work_dir=*)
            WORK_DIR="${1#*=}"
            shift
            ;;
        *)
            echo "Error: Unsupported flag $1"
            exit 1
            ;;
    esac
done

# Set default work directory if not provided
WORK_DIR=${WORK_DIR:-$(pwd)}
cd ${WORK_DIR}

# Extract values from the JSON file
NAME=$(jq -r '.name' "$JSON_FILE")
FROM=$(jq -r '.from' "$JSON_FILE")
IMAGE_VERSION=$(jq -r '.image_version' "$JSON_FILE")
APT_PACKAGES=$(jq -r '.packages.apt // [] | join(" ")' "$JSON_FILE")
R_PACKAGES=$(jq -r '.packages.r // [] | map("'"'"'" + . + "'"'"'") | join(", ")' "$JSON_FILE")
BIOC_PACKAGES=$(jq -r '.packages.biocmanager // [] | map("'"'"'" + . + "'"'"'") | join(", ")' "$JSON_FILE")
GITHUB_PACKAGES=$(jq -r '.packages.devtools_install_github // []' "$JSON_FILE")

# Check if there are GitHub packages in the JSON (only if the array is not empty)
if [ "$(echo "$GITHUB_PACKAGES" | jq 'length')" -gt 0 ]; then
    # Ensure devtools is included in R packages if there are GitHub packages
    if [[ -z "$R_PACKAGES" || ! "$R_PACKAGES" =~ "devtools" ]]; then
        R_PACKAGES="${R_PACKAGES:+$R_PACKAGES, }'devtools'"
    fi
fi

FILES_DIR=$(echo ${NAME}_${IMAGE_VERSION} | sed 's/://;s/\//_/')
mkdir -p ${FILES_DIR}

# Initialize the Dockerfile content
DOCKERFILE_CONTENT="""FROM ${FROM}

RUN apt-get update -y \\
    && apt-get install -y ${APT_PACKAGES} \\
    && apt-get clean \\
    && rm -rf /var/lib/apt/lists/*

ENV R_REMOTES_NO_ERRORS_FROM_WARNINGS=true

ADD list_r_packages.sh list_r_packages.sh
RUN chmod u+x list_r_packages.sh

RUN R -e \"install.packages('BiocManager')\"$(
    [ -n "$BIOC_PACKAGES" ] && echo " \\
    && echo 'n' | R --no-save -e \"BiocManager::install(c(${BIOC_PACKAGES}))\""
)$(
    [ -n "$R_PACKAGES" ] && echo " \\
    && echo 'n' | R --no-save -e \"install.packages(c(${R_PACKAGES}))\""
)"

# Handle GitHub packages with optional 'ref'
if [ "$(echo "$GITHUB_PACKAGES" | jq 'length')" -gt 0 ]; then
    for package_info in $(echo "$GITHUB_PACKAGES" | jq -c '.[]'); do
        PACKAGE_NAME=$(echo "$package_info" | jq -r '.package')
        REF=$(echo "$package_info" | jq -r '.ref // empty')

        if [ -n "$REF" ]; then
            INSTALL_CMD="devtools::install_github('${PACKAGE_NAME}', ref = '${REF}')"
        else
            INSTALL_CMD="devtools::install_github('${PACKAGE_NAME}')"
        fi
        
        DOCKERFILE_CONTENT="$DOCKERFILE_CONTENT \\
        && echo 'n' | R --no-save -e \"${INSTALL_CMD}\""
    done
fi

# Final Dockerfile content
DOCKERFILE_CONTENT="$DOCKERFILE_CONTENT

CMD [\"/list_r_packages.sh\"]"

# Write the Dockerfile to disk
DOCKERFILE_PATH="${FILES_DIR}/Dockerfile"
echo "$DOCKERFILE_CONTENT" > $DOCKERFILE_PATH

cp /resources/list_r_packages.sh ${FILES_DIR}/

# Build the Docker image if not in dry-run mode
IMAGE_TAG="${NAME}:${IMAGE_VERSION}"
if [ $DRY_RUN -eq 1 ]; then
    echo "Dry run mode: Docker image with tag $IMAGE_TAG would be built."
else
    echo "Building Docker image with tag: $IMAGE_TAG"
    docker build -t "$IMAGE_TAG" -f "$DOCKERFILE_PATH" "${FILES_DIR}"
fi
