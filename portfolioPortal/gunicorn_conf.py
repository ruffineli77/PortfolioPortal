
import multiprocessing
import os

bind = os.environ.get("CV_APP_ADDRESS")
workers = multiprocessing.cpu_count() * 2 + 1
