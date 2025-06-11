#!/bin/bash

echo "Installed R packages and their versions:"
R -e "installed.packages()[, c('Package', 'Version')]"
