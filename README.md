# Navigation
- [Navigation](https://github.com/ZeroNiki/Cryptocurrency-app?tab=readme-ov-file#Navigation)
    - [About](https://github.com/ZeroNiki/Cryptocurrency-app?tab=readme-ov-file#About)
    - [Install](https://github.com/ZeroNiki/Cryptocurrency-app?tab=readme-ov-file#Install)
    - [Docker install](https://github.com/ZeroNiki/Cryptocurrency-app?tab=readme-ov-file#Docker-Install)
    - [Configuration](https://github.com/ZeroNiki/Cryptocurrency-app?tab=readme-ov-file#Configuration)
    - [Usage](https://github.com/ZeroNiki/Cryptocurrency-app?tab=readme-ov-file#Usage)
    - [TODO](https://github.com/ZeroNiki/Cryptocurrency-app?tab=readme-ov-file#TODO)

## About
Cryptocurrency app

Lib:
- FastApi
- Fastapi-Users
- redis
- sqlalchemy
- postgresql

*more in 'requirements.txt'*

application that displays the exchange rate of cryptocurrencies

## Install

### Clone repo
```sh
git clone https://github.com/ZeroNiki/Cryptocurrency-app.git

cd Cryptocurrency-app
```

### Create venv and install requirements
```
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

### Start project
before launch watch [Configuration](https://github.com/ZeroNiki/Cryptocurrency-app?tab=readme-ov-file#Configuration)


if you not using docker for start. Change startup functionin app/main.py to:
```python
@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(
        "redis://localhost:6379", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
```
if you are going to use docker then do not touch this piece of code and go to Docker Install

start redis and pgadmin4:
```sh
redis-server

pgadmin4
```

```sh
cd app/

uvicorn main:app --reload
```

go to http://127.0.0.1:8000


## Docker install
### Build `Dockerfile`:
```sh
docker build .
```

### Docker compose
```sh
docker compose build 
```

```sh
docker compose up
```

go to http://localhost:9999


## Configuration
.env file:
```env
DB_NAME=postgresdb name
DB_HOST=postgresdb host
DB_PORT=postgresdb port
DB_PASS=postgresdb pass
DB_USER=postgresdb user


ALL_DATA_LINK=https://api.mobula.io/api/1/all
SPECIFIC_DATA_LINK=https://api.mobula.io/api/1/market/data?symbol=

API_TOKEN=Your token from mobula


AUTH_SECRET=Think of something
```


.env-non-dev file:
*! `DB_HOST=db` do not touch*

```env
DB_NAME=postgresdb name
DB_HOST=db
DB_PORT=5432 
DB_PASS=postgresdb pass
DB_USER=postgresdb user

POSTGRES_DB=db name
POSTGRES_USER=db user
POSTGRES_PASSWORD=db password

ALL_DATA_LINK=https://api.mobula.io/api/1/all
SPECIFIC_DATA_LINK=https://api.mobula.io/api/1/market/data?symbol=

API_TOKEN=your token from mobula

AUTH_SECRET=Think of something
```

### Alembic
```sh
alembic revision --autogenerate -m "Init"

alembic upgrade head
```



## Usage
### Documentation
`https://127.0.0.1:8000/docs` 

### Pages
Home page:
`https://127.0.0.1:8000/pages/home`
Just home page

Databes page:
`http://127.0.0.1:8000/pages/cr_db`
see first 50 data

Search:
`http://127.0.0.1:8000/pages/search/BTC`
find by symbol and get price, name, logo

### Other routes see in `documentation`

## TODO
- Improve user authorization;
      - Correct mistakes in Docker
- Improve home, about page;







