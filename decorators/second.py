import time


def caching(func):
  cach_value={}
  def warpper(*args):
    if args in cach_value:
      return cach_value[args]
    result=func(*args)
    cach_value[args]=result
    return result
    
  return warpper

@caching
def long_run_func(a,b):
    time.sleep(4)
    return a + b

print(long_run_func(1,2))
print(long_run_func(1,2))