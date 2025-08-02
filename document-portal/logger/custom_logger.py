import os
import logging
from datetime import datetime

class CustomLogger:
    def __init__(self, log_file_path=None):
        logs_dir = os.path.join(os.getcwd(), 'logs')
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        if log_file_path is None:
            log_file_path = os.path.join(logs_dir, f"app_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")
        
        logging.basicConfig(
            filename=log_file_path,
            format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO,
        )
    
    def get_logger(self, name=__file__):
        return logging.getLogger(os.path.basename(name))


if __name__ == "__main__":
    custom_logger = CustomLogger()
    logger = custom_logger.get_logger(__file__)
    logger.info("Custom logger initialized.")
    logger.info("This is an info message.")
    logger.error("This is an error message.")
    logger.warning("This is a warning message.")
    logger.debug("This is a debug message.")

