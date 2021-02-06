#!/bin/bash

echo "Running App..."
gunicorn src.app.wsgi:application -b 0.0.0.0:8000 -t 3600
