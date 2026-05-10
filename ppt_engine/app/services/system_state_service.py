# app/services/system_state_service.py

"""
System state service.

Responsibilities:
- Check database existence
- Check template availability
- Determine first-time setup state
- Provide centralized system state
"""

from pathlib import Path

from app.utils.logger import logger


# Project root
ROOT_DIR = Path(__file__).resolve().parent.parent.parent


# Database path
DB_PATH = ROOT_DIR / "ppt_engine.db"


# Template folders
RAW_FOLDER = ROOT_DIR / "templates/raw"


def database_exists():
    """
    Check whether SQLite database exists.
    """

    exists = DB_PATH.exists()

    logger.info(
        f"Database exists: {exists}"
    )

    return exists


def templates_available():
    """
    Check whether templates are available.
    """

    if not RAW_FOLDER.exists():

        logger.warning(
            "Template folder not found."
        )

        return False

    templates = list(
        RAW_FOLDER.glob("*.pptx")
    )

    available = len(templates) > 0

    logger.info(
        f"Templates available: {available}"
    )

    return available


def is_first_time_setup():
    """
    Determine whether system is in first-time setup state.
    """

    first_time = not database_exists()

    logger.info(
        f"First-time setup: {first_time}"
    )

    return first_time


def knowledge_base_initialized():
    """
    Determine whether knowledge base is initialized.
    """

    initialized = (
        database_exists()
        and templates_available()
    )

    logger.info(
        f"Knowledge base initialized: {initialized}"
    )

    return initialized


def get_system_state():
    """
    Return centralized system state.
    """

    state = {
        "database_exists": database_exists(),
        "templates_available": templates_available(),
        "first_time_setup": is_first_time_setup(),
        "knowledge_base_initialized": knowledge_base_initialized()
    }

    logger.info(
        f"System state: {state}"
    )

    return state