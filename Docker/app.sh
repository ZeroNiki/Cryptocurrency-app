#!/bin/bash

alembic upgrade head

cd app/

gunicorn -k uvicorn.workers.UvicornWorker main:app -b 0.0.0.0:8000
