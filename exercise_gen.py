import re

file_path = "/etc/httpd/logs/access_log" 

with open(file_path, "r") as logs:
    lines = logs.readlines() 


def log_timestamp(lines):
    pattern = r'\[.*?\]'
    for line in lines:
        timestamp = (re.findall(pattern, line))[1,-1]
        yield string(timestamp[0])

timestamps = log_timestamp(lines)
print(next(timestamps))
print(next(timestamps))
