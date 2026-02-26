from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional

# Base properties shared by Create and Response
class TaskBase(BaseModel):
    title:  str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    completed: bool = False

# Schema for creating a task (what the user sends)
class TaskCreate(TaskBase):
    pass  

# Schema for returning a task (what the API sends back)
class TaskResponse(TaskBase):
    id: int
    created_at: datetime

    # This allows Pydantic to read SQLAlchemy models (which are objects, not dicts)
    model_config = ConfigDict(from_attributes=True)
