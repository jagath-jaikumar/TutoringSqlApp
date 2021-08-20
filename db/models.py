"""
Content Scraper models
"""
import uuid

from sqlalchemy import Column, Enum, ForeignKey, String, UniqueConstraint, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.types import Boolean, DateTime

Base = declarative_base()


class TimestampMixin(object):
    """Provides auto generating created_at field"""

    created_at = Column(DateTime, default=func.now())


class SimpleTable(TimestampMixin, Base):
    __tablename__ = "simple_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    __table_args__ = (UniqueConstraint("name", sqlite_on_conflict="IGNORE"),)
