
# #/main.py
# """
# Project entry point.

# This file:
# - extracts PPT data
# - creates SQLite tables
# - stores extracted metadata
# """

# import os

# from app.extractor.extractor import PPTExtractor

# from app.database.db import (
#     engine,
#     SessionLocal
# )

# from app.models.models import (
#     Base,
#     Template,
#     Slide,
#     ShapeObject
# )


# # Create SQLite tables
# Base.metadata.create_all(bind=engine)


# PPT_PATH = (
#     "templates/curated/"
#     "project-management-infographics.pptx"
# )


# def save_shapes(
#     session,
#     template_id,
#     slide_id,
#     shapes
# ):
#     """
#     Recursively save shapes into database.
#     """

#     for shape in shapes:

#         shape_record = ShapeObject(
#             template_id=template_id,
#             slide_id=slide_id,

#             shape_name=shape["shape_name"],
#             shape_type=shape["shape_type"],

#             text_content=shape["text"],

#             x=shape["x"],
#             y=shape["y"],

#             width=shape["width"],
#             height=shape["height"],

#             children=shape["children"]
#         )

#         session.add(shape_record)

#         session.commit()

#         # Save nested children recursively
#         if shape["children"]:

#             save_shapes(
#                 session,
#                 template_id,
#                 slide_id,
#                 shape["children"]
#             )


# def main():

#     extractor = PPTExtractor(PPT_PATH)

#     extracted_data = extractor.extract()

#     session = SessionLocal()

#     # Save template
#     template = Template(
#         file_name=os.path.basename(PPT_PATH),
#         slide_count=len(extracted_data),
#         source_path=PPT_PATH
#     )

#     session.add(template)

#     session.commit()

#     # Save slides + shapes
#     for slide_data in extracted_data:

#         slide_record = Slide(
#             template_id=template.id,
#             slide_index=slide_data["slide_index"]
#         )

#         session.add(slide_record)

#         session.commit()

#         save_shapes(
#             session,
#             template.id,
#             slide_record.id,
#             slide_data["shapes"]
#         )

#     session.close()

#     print("Extraction completed successfully")


# if __name__ == "__main__":
#     main()


"""
Main FastAPI application.

Responsibilities:
- Central API gateway
- Route orchestration
- Service triggering
- Database initialization
"""

from fastapi import FastAPI

from app.database.db import engine
from app.database.reset_db import reset_database

from app.models.models import Base


# =========================================================
# CREATE DATABASE TABLES
# =========================================================

Base.metadata.create_all(bind=engine)


# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI(
    title="Chat PPT Engine"
)


# =========================================================
# ROOT ENDPOINT
# =========================================================

@app.get("/")
def root():
    """
    Health check endpoint.
    """

    return {
        "status": "success",
        "message": "Chat PPT Engine Running"
    }


# =========================================================
# RESET KNOWLEDGE BASE
# =========================================================

@app.post("/reset-knowledge-base")
def reset_knowledge_base():
    """
    Completely wipe:
    - SQLite database
    - raw templates

    Reinitialize fresh knowledge base.
    """

    reset_database()

    return {
        "status": "success",
        "message": (
            "Knowledge base reset completed."
        )
    }