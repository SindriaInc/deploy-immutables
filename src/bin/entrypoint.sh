#!/usr/bin/env bash

set -e

# Infra setup
mkdir -p .setup
cd .setup
git clone https://${IAC_GIT_USERNAME}:${IAC_GIT_PASSWORD}@${IAC_GIT_PROVIDER}/${IAC_GIT_NAMESPACE}/${IAC_INFRA_NAME}.git
cp ${IAC_INFRA_NAME}/config/* ../config

# Run blueprints deployment
python /var/www/app/app/main.py