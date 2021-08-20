from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class SimpleObject(BaseModel):
    name: str
