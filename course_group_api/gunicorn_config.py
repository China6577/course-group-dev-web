import multiprocessing

bind = "0.0.0.0:8000"

workers = multiprocessing.cpu_count() + 1

threads = 2

timeout = 30

keepalive = 2

accesslog = "-"

errorlog = "-"

loglevel = "error"

access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

max_requests = 800

max_requests_jitter = 100

proc_name = "course-group-api"
