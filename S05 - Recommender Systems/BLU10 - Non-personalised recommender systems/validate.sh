#!/usr/bin/env bash
set -x
set -e

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# Validate notebook
ldsagrader portal validate --notebook_path="$NOTEBOOK_PATH" --timeout=240

