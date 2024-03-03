FROM python:3.11.6

RUN mkdir /fastapi_app
WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x Docker/*.sh

# WORKDIR app
#
# CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "-b", "0.0.0.0:8000"]
