import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end  = time.time()
        print("Runtime: {t}ms".format(t = (end-start)*1000))
        return result
    return wrapper

