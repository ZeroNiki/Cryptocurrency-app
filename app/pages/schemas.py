import contextlib

from auth.utils import get_user_db 
from auth.manager import get_user_manager

from database import get_async_session


get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


