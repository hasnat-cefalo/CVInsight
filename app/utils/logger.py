import logging
import os


def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG if os.getenv("DEBUG") == "True" else logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)


logger = setup_logger()
