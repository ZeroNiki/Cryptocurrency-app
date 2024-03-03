from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional


from operation.router import get_all, currency_symbol
from operation.utils import get_db

# from auth.base_config import get_user_manager, current_user
# from auth.models import User
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

# @ router.post("/create")
# async def create_user(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
#     async with SessionLocal() as session:
#         user = User(username=username, email=email,
#                     hashed_password=password)
#
#         user.set_password(password)
#
#         session.add(user)
#         await session.commit()
#     return {"Status": "200"}


@ router.get("/login_page")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# @ router.post("/login")
# async def login(user_manager: BaseUserManager[User, int] = Depends(get_user_manager), email: str = Form(...), password: str = Form(...)):
#     try:
#         login_user = await user_manager.get_by_email(email)
#
#         if not login_user:
#             return "Incorrect email or password"
#
#         if not verify_password(password, login_user.hashed_password):
#             return "Incorrect email or password"
#
#         return login_user
#     except Exception as e:
#         return e
