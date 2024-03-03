from fastapi import APIRouter, HTTPException, Depends
from operation.models import crypto_data
from sqlalchemy.orm import Session
from sqlalchemy import select
from config import API_TOKEN, ALL_DATA_LINK, SPECIFIC_DATA_LINK
from operation.utils import get_db
from fastapi_cache.decorator import cache
import requests


router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)


@router.get("/all_data", response_model=None)
async def get_all(db: Session = Depends(get_db)):
    try:
        query = select(crypto_data.c.id, crypto_data.c.symbol).limit(50)

        result = await db.execute(query)

        data = result.fetchall()

        data_dict = [{"id": row[0], "symbol": row[1]} for row in data]

        return data_dict

    except Exception as e:
        return {
            "Error": "Something wrong...",
            "detail": e,
        }


@router.post('/parse_date')
async def parser(db: Session = Depends(get_db)):
    HEADERS = {
        'Authorization': f'{API_TOKEN}'
    }

    url = f'{ALL_DATA_LINK}'

    try:
        r = requests.get(url, headers=HEADERS)

        data = r.json()

        symbols = [item['symbol'] for item in data['data']]

        for symbol in symbols:
            await db.execute(crypto_data.insert().values(symbol=symbol))

        await db.commit()
        await db.close()

        return {
            "Status": "200. Ok"
        }

    except requests.RequestException as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching data from API: {e}")


@router.get('/{symbol}')
@cache(expire=60)
async def currency_symbol(symbol: str, db: Session = Depends(get_db)):
    HEADERS = {
        'Authorization': f'{API_TOKEN}'
    }

    result = await db.execute(crypto_data.select().where(crypto_data.c.symbol == symbol))

    if result.fetchone():
        try:
            r = requests.get(f"{SPECIFIC_DATA_LINK}{symbol}", headers=HEADERS)

            data = r.json()

            name = data['data']['name']
            price = data['data']['price']
            logo = data['data']['logo']

            return {
                "Name": name,
                "Symbol": symbol,
                "Price": price,
                "logo": logo
            }

        except Exception as e:
            return e
    else:
        return "Data not found"

    db.close()
