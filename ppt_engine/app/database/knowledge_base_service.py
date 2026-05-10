# #app/database/reset_db.py

# """
# Database reset utility.

# Responsibilities:
# - Delete SQLite database
# - Clear template folders
# - Generate readable logs
# """

# import shutil
# import time

# from pathlib import Path

# from app.utils.logger import logger


# # Project root
# ROOT_DIR = Path(__file__).resolve().parent.parent.parent


# # Database path
# DB_PATH = ROOT_DIR / "ppt_engine.db"


# # Template folders
# RAW_FOLDER = ROOT_DIR / "templates/raw"


# def reset_database(
#     progress_bar=None,
#     status_text=None
# ):
#     """
#     Completely reset knowledge base.
#     """

#     logger.warning(
#         "Knowledge base reset initiated."
#     )

#     # -----------------------------------
#     # STEP 1
#     # Delete database
#     # -----------------------------------

#     if status_text:
#         status_text.text(
#             "Deleting database..."
#         )

#     if progress_bar:
#         progress_bar.progress(25)

#     time.sleep(1)

#     if DB_PATH.exists():

#         DB_PATH.unlink()

#         logger.info(
#             "Database deleted successfully."
#         )

#     else:

#         logger.warning(
#             "Database file not found."
#         )

#     # -----------------------------------
#     # STEP 2
#     # Clear raw templates
#     # -----------------------------------

#     if status_text:
#         status_text.text(
#             "Clearing template folders..."
#         )

#     if progress_bar:
#         progress_bar.progress(60)

#     time.sleep(1)

#     if RAW_FOLDER.exists():

#         shutil.rmtree(RAW_FOLDER)

#         RAW_FOLDER.mkdir(
#             parents=True,
#             exist_ok=True
#         )

#         logger.info(
#             "Template folders cleared."
#         )

#     # -----------------------------------
#     # STEP 3
#     # Finish
#     # -----------------------------------

#     if status_text:
#         status_text.text(
#             "Knowledge base reset completed."
#         )

#     if progress_bar:
#         progress_bar.progress(100)

#     logger.info(
#         "Knowledge base reset completed."
#     )

#     return True

# app/services/knowledge_base_service.py

"""
Knowledge base service.

Responsibilities:
- Reset knowledge base
- Delete SQLite database
- Clear template folders
- Generate readable logs
"""

import shutil

from pathlib import Path

from app.utils.logger import logger


# Project root
ROOT_DIR = Path(__file__).resolve().parent.parent.parent


# Database path
DB_PATH = ROOT_DIR / "ppt_engine.db"


# Template folders
RAW_FOLDER = ROOT_DIR / "templates/raw"


def reset_knowledge_base():
    """
    Completely reset the knowledge base.
    """

    logger.warning(
        "Knowledge base reset initiated."
    )

    # -----------------------------------
    # STEP 1
    # Delete database
    # -----------------------------------

    if DB_PATH.exists():

        DB_PATH.unlink()

        logger.info(
            "Database deleted successfully."
        )

    else:

        logger.warning(
            "Database file not found."
        )

    # -----------------------------------
    # STEP 2
    # Clear template folders
    # -----------------------------------

    if RAW_FOLDER.exists():

        shutil.rmtree(RAW_FOLDER)

        RAW_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

        logger.info(
            "Template folders cleared."
        )

    else:

        logger.warning(
            "Template folder not found."
        )

    # -----------------------------------
    # STEP 3
    # Finish
    # -----------------------------------

    logger.info(
        "Knowledge base reset completed."
    )

    return {
        "success": True,
        "message": "Knowledge base reset completed."
    }