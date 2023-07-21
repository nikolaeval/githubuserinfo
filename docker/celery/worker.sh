#!/usr/bin/env sh

set -o errexit
set -o nounset

# Use named queue if passed or default one:
QUEUE_NAME=${1:-'celery'}
echo "[starting worker for queue: ${QUEUE_NAME}]"

# Runs celery worker with events sourcing to monitoring:
celery --app=server worker -E -B -Q "$QUEUE_NAME"
