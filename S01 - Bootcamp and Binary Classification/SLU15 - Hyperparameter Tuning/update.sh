#!/usr/bin/env bash
set -x
set -e

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# Update notebook checksum
ldsagrader portal update --notebook_path="$NOTEBOOK_PATH" --checksum_url=$PORTAL_CHECKSUM_URL --token=$PORTAL_TOKEN

