#!/bin/bash

set -o errexit
set -o pipefail

coverage run --omit='*/site-packages/*' -m pytest

exec "$@"
