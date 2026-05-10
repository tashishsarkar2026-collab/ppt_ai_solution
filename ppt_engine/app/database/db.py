# #app/database/db.py

# """
# Centralized database setup.

# Responsibilities:
# - Create SQLite connection
# - Detect first-time execution
# - Create readable logs
# """

# from pathlib import Path

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from app.utils.logger import logger


# # Project root folder
# PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


# # Force DB inside project root
# DB_PATH = PROJECT_ROOT / "ppt_engine.db"


# # SQLite connection string
# DATABASE_URL = f"sqlite:///{DB_PATH}"


# # Detect DB existence
# if DB_PATH.exists():

#     logger.info(
#         f"Database found at: {DB_PATH}"
#     )

# else:

#     logger.warning(
#         "Database not found."
#     )

#     logger.info(
#         "Running first-time setup."
#     )

#     logger.info(
#         "New SQLite database will be created."
#     )


# # Create SQLAlchemy engine
# engine = create_engine(
#     DATABASE_URL,
#     echo=False
# )


# logger.info(
#     "SQLAlchemy engine initialized."
# )


# # Session factory
# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )


# logger.info(
#     "Database session factory created."
# )



# app/database/db.py

"""
Database connection layer only.

Responsibilities:
- Create SQLite connection
- Create SQLAlchemy engine
- Create session factory
"""

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.utils.logger import logger


# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


# SQLite database path
DB_PATH = PROJECT_ROOT / "ppt_engine.db"


# SQLite connection string
DATABASE_URL = f"sqlite:///{DB_PATH}"


# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=False
)


logger.info(
    "SQLite database connection initialized."
)


# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


logger.info(
    "Database session factory created."
)


logger.info(
    "Database connection layer ready."
)