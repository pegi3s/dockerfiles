#!/bin/bash
# entrypoint.sh - Executes commands or performs cleanup based on input
set -e 

export NXF_HOME=$(pwd)/.nf_config_cache 

echo "--- Nextflow Runner Entrypoint ---"
echo "Working Directory : $(pwd)"
echo "NXF_HOME set to : ${NXF_HOME}"
echo "Running command   : $@" 
echo "------------------------------"

# Check if the first argument passed to the container is "cleanAll"
if [ "$1" == "cleanAll" ]; then
    echo "*** CleanAll command received ***"
    
    echo "Attempting to remove Work directory: ${WORK_DIR}"
    # Check if directory exists before trying to remove
    if [ -d "$(pwd)/work" ]; then
        rm -rf "$(pwd)/work"
        echo "Work directory removed."
    else
        echo "Work directory ($(pwd)/work) not found, skipping."
    fi

    echo "Attempting to remove Nextflow config/asset directory: ${NXF_HOME}"
    # Check if directory exists before trying to remove
    if [ -d "${NXF_HOME}" ]; then
        rm -rf "${NXF_HOME}"
        echo "NXF_HOME directory removed."
    else
        echo "NXF_HOME directory (${NXF_HOME}) not found, skipping."
    fi
    
    echo "Cleanup complete."
    exit 0 # Exit successfully after cleaning

else

# Run the main command and Store the exit status
"$@"
EXIT_STATUS=$? 
echo "------------------------------"
echo "Main command finished with status: ${EXIT_STATUS}"

fi

# Exit the entrypoint script with the original exit status of the main command
exit ${EXIT_STATUS} 

