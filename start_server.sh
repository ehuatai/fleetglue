#!/bin/bash

set -Eeuo pipefail
flask --app server --debug run --host 0.0.0.0 --port 8000
