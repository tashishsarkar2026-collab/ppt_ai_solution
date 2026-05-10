# app/services/template_service.py

"""
Template service.

Responsibilities:
- Save uploaded templates
- Validate PPT files
- Trigger extraction workflow
- Coordinate ingestion pipeline
- Generate readable logs
"""

import shutil

from pathlib import Path

from app.utils.logger import logger


# Project root
ROOT_DIR = Path(__file__).resolve().parent.parent.parent


# Template storage folder
RAW_TEMPLATE_FOLDER = ROOT_DIR / "templates/raw"


def validate_template_file(
    file_name: str
):
    """
    Validate uploaded template file.
    """

    valid_extensions = [
        ".pptx"
    ]

    file_extension = Path(
        file_name
    ).suffix.lower()

    is_valid = (
        file_extension in valid_extensions
    )

    logger.info(
        f"Template validation result "
        f"for '{file_name}': {is_valid}"
    )

    return is_valid


def save_template(
    uploaded_file
):
    """
    Save uploaded PPT template.
    """

    RAW_TEMPLATE_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    destination_path = (
        RAW_TEMPLATE_FOLDER
        / uploaded_file.name
    )

    with open(
        destination_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            uploaded_file,
            buffer
        )

    logger.info(
        f"Template saved: "
        f"{destination_path}"
    )

    return destination_path


def trigger_extraction_workflow(
    template_path: Path
):
    """
    Trigger template extraction workflow.

    Placeholder for future extraction pipeline.
    """

    logger.info(
        f"Starting extraction workflow "
        f"for: {template_path.name}"
    )

    # Future extraction pipeline:
    #
    # 1. Extract slides
    # 2. Extract shapes
    # 3. Extract groups
    # 4. Extract layout hierarchy
    # 5. Generate metadata
    # 6. Insert into database
    # 7. Generate embeddings

    logger.info(
        f"Extraction workflow completed "
        f"for: {template_path.name}"
    )

    return {
        "success": True,
        "template_name": template_path.name
    }


def ingest_template(
    uploaded_file
):
    """
    Complete template ingestion workflow.
    """

    logger.info(
        "Template ingestion initiated."
    )

    # -----------------------------------
    # STEP 1
    # Validate template
    # -----------------------------------

    if not validate_template_file(
        uploaded_file.name
    ):

        logger.error(
            "Invalid template format."
        )

        return {
            "success": False,
            "message": (
                "Only .pptx files "
                "are supported."
            )
        }

    # -----------------------------------
    # STEP 2
    # Save template
    # -----------------------------------

    template_path = save_template(
        uploaded_file
    )

    # -----------------------------------
    # STEP 3
    # Trigger extraction workflow
    # -----------------------------------

    extraction_result = (
        trigger_extraction_workflow(
            template_path
        )
    )

    logger.info(
        "Template ingestion completed."
    )

    return {
        "success": True,
        "template_path": str(template_path),
        "extraction_result": extraction_result
    }