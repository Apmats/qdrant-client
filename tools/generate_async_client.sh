#!/bin/bash

set -e

RELATIVE_PROJECT_ROOT="$(dirname "$0")/.."
cd $RELATIVE_PROJECT_ROOT
ABSOLUTE_PROJECT_ROOT=$(pwd)

cd $ABSOLUTE_PROJECT_ROOT/tools/async_client_generator

python3 -m tools.async_client_generator.base_client_generator
python3 -m tools.async_client_generator.fastembed_generator
python3 -m tools.async_client_generator.client_generator
python3 -m tools.async_client_generator.remote_generator

ls -1 | autoflake --recursive --imports qdrant_client --remove-unused-variables --in-place async*.py
ls -1 | grep async | xargs -I {} isort -w 99 --multi-line 3 --trailing-comma --force-grid-wrap 0 --combine-as {}
ls -1 | grep async | xargs -I {} black --fast -l 99 --target-version py38 {}

mv async_client_base.py $ABSOLUTE_PROJECT_ROOT/qdrant_client/async_client_base.py
mv async_qdrant_client.py $ABSOLUTE_PROJECT_ROOT/qdrant_client/async_qdrant_client.py
mv async_qdrant_fastembed.py $ABSOLUTE_PROJECT_ROOT/qdrant_client/async_qdrant_fastembed.py
mv async_qdrant_remote.py $ABSOLUTE_PROJECT_ROOT/qdrant_client/async_qdrant_remote.py