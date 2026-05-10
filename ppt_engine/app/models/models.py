#app/models/models.py

"""
Database models.

These models define how extracted PPT data
will be stored inside SQLite.
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    ForeignKey,
    JSON
)

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Template(Base):
    """
    Stores PPT file information.
    """

    __tablename__ = "templates"

    id = Column(Integer, primary_key=True)

    file_name = Column(String)

    slide_count = Column(Integer)

    source_path = Column(Text)


class Slide(Base):
    """
    Stores slide-level information.
    """

    __tablename__ = "slides"

    id = Column(Integer, primary_key=True)

    template_id = Column(
        Integer,
        ForeignKey("templates.id")
    )

    slide_index = Column(Integer)


class ShapeObject(Base):
    """
    Stores extracted shape information.
    """

    __tablename__ = "shape_objects"

    id = Column(Integer, primary_key=True)

    template_id = Column(
        Integer,
        ForeignKey("templates.id")
    )

    slide_id = Column(
        Integer,
        ForeignKey("slides.id")
    )

    shape_name = Column(String)

    shape_type = Column(String)

    text_content = Column(Text)

    x = Column(Float)

    y = Column(Float)

    width = Column(Float)

    height = Column(Float)

    children = Column(JSON)