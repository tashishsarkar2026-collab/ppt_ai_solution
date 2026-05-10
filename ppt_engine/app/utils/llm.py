from openai import OpenAI

# from services.ingestion.shared.utils.logger import setup_logger

# logger = setup_logger(__name__)


# try:

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

#     logger.info("Successfully connected to LM Studio chat client.")

# except Exception as e:

#     logger.error(f"Failed to initialize chat client: {str(e)}")

#     raise