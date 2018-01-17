import json
import time


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]

def byte_size(obj):
    return len(json.dumps(obj))


# Give the current time
def chrono():
    return time.time(), time.process_time()


# Give the elapsed time between starting_time and current time
def end_chrono(real_time, process_time):
    return (time.time() - real_time), (time.process_time() - process_time)