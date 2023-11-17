import os
import sys
import logging

# logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# logging_str = "[%(timestamp (ASCI time))s: %(log level name)s: %(module name)s: %(error message)s]"

# Creating log path and file
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# configuring log
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath), # write logs to log_file
        logging.StreamHandler(sys.stdout) # will bring log inside terminal too
    ]
)

logger = logging.getLogger("CNNClassifierLogger")