from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase

# Define the base class
class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "tasks"

    # Define the fields as requested
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())