import logging

job_logger = logging.getLogger("job_logger")
job_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename="/var/log/gunicorn/jobs.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

job_logger.addHandler(file_handler)
