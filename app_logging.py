import logging

logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error messagedd ffff.")  
logging.debug("This is a debug message.")
logging.critical("This is a critical message.")