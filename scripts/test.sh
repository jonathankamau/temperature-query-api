#!/bin/bash

set -o errexit
set -o pipefail

coverage run --omit='*/site-packages/*' -m pytest
coverage html
COVERALLS_REPO_TOKEN=${COVERALLS_REPO_TOKEN} coveralls

exec "$@"
