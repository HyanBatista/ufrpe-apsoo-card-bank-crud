#!/bin/bash

set -e

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload