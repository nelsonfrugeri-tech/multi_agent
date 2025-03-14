from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional
from src.domain.file import File


class Vector(BaseModel):
    id: str
    name: str
    files: Optional[List[File]] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now())
