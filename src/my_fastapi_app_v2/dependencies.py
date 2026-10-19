from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from my_fastapi_app_v2.database import get_db

DbSession = Annotated[Session, Depends(get_db)]
