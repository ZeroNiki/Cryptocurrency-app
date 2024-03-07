from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

import contextlib

from database import SessionLocal, get_async_session

from pages.schemas import get_async_session_context, get_user_db_context, get_user_manager_context

from operation.router import get_all, currency_symbol
from operation.utils import get_db

# from auth.base_config import get_user_manager, current_user
from auth.schemas import UserCreate, UserRead
from auth.utils import get_user_db
from auth.manager import get_user_manager
from auth.models import User
# from database import SessionLocal

# from pages.utils import verify_password


router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)


templates = Jinja2Templates(directory="templates")


@router.get("/home")
def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get('/search/{symbol}')
def home_page(request: Request, cr_data=Depends(currency_symbol)):
    return templates.TemplateResponse("search.html", {"request": request, "cr_data": cr_data})


@router.get("/cr_db")
async def data_page(request: Request, db: AsyncSession = Depends(get_db)):
    data = await get_all(db)
    return templates.TemplateResponse('cr_data.html', {"request": request, "data": data})


@ router.get("/register_page")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@ router.post("/create")
async def create_user(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    async with get_async_session_context() as session:
        async with get_user_db_context(session) as user_db:
            async with get_user_manager_context(user_db) as user_manager:
                user = await user_manager.create(
                    UserCreate(
                        username=username, email=email, password=password
                    )
                )
                print(f"User create: {user}")
                return {"Status": "200"}


@router.get("/login_page")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
