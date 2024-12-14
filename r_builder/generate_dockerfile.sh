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

# Extract values from the JSON file
NAME=$(jq -r '.name' "$JSON_FILE")
FROM=$(jq -r '.from' "$JSON_FILE")
IMAGE_VERSION=$(jq -r '.image_version' "$JSON_FILE")
APT_PACKAGES=$(jq -r '.packages.apt // [] | join(" ")' "$JSON_FILE")
R_PACKAGES=$(jq -r '.packages.r // [] | map("'"'"'" + . + "'"'"'") | join(", ")' "$JSON_FILE")
BIOC_PACKAGES=$(jq -r '.packages.biocmanager // [] | map("'"'"'" + . + "'"'"'") | join(", ")' "$JSON_FILE")

FILES_DIR=$(echo ${NAME}_${IMAGE_VERSION} | sed 's/://;s/\//_/')
mkdir -p ${FILES_DIR}

# Generate the Dockerfile
DOCKERFILE_CONTENT="""FROM ${FROM}

RUN apt-get update -y \\
    && apt-get install -y ${APT_PACKAGES} \\
    && apt-get clean \\
    && rm -rf /var/lib/apt/lists/*

ENV R_REMOTES_NO_ERRORS_FROM_WARNINGS=true

ADD list_r_packages.sh list_r_packages.sh
RUN chmod u+x list_r_packages.sh

RUN R -e \"install.packages('BiocManager')\"$(
    [ -n "$R_PACKAGES" ] && echo " \\
    && echo 'n' | R --no-save -e \"install.packages(c(${R_PACKAGES}))\""
)$(
    [ -n "$BIOC_PACKAGES" ] && echo " \\
    && echo 'n' | R --no-save -e \"BiocManager::install(c(${BIOC_PACKAGES}))\""
)

CMD [\"/list_r_packages.sh\"]
"""

# Write the Dockerfile to disk
DOCKERFILE_PATH="${FILES_DIR}/Dockerfile"
echo "$DOCKERFILE_CONTENT" > $DOCKERFILE_PATH

cp list_r_packages.sh ${FILES_DIR}/

# Build the Docker image
IMAGE_TAG="${NAME}:${IMAGE_VERSION}"
echo "Building Docker image with tag: $IMAGE_TAG"
docker build -t "$IMAGE_TAG" -f "$DOCKERFILE_PATH" .
