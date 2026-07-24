import time 
from functools import wraps
from typing import Callable, Any
from src.utils.logger import logger

def time_it(func : Callable)->Callable:
    @wraps(func)
    def wrapper(*args: Any,**kwargs:Any)->Any:
        start = time.perf_counter()
        result = func(*args,**kwargs)
        elapsed = time.perf_counter()-start
        logger.info(f"[{func.__name__}] executed in {elapsed:.4f} seconds.")
        return result
    return wrapper

def retry(retries: int=3,delay: float=1.0)->Callable:
    def decorator(func: Callable)->Callable:
        @wraps(func)
        def wrapper(*args:Any, **kwargs: Any)->Any:
            for attempt in range(1,retries+1):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    logger.warning(f"Attempt {attempt} failed for {func.__name__}: {e}")
                    time.sleep(delay)
            raise RuntimeError(f"All {retries} attempts failed for {func.__name__}")
        return wrapper
    return decorator

        

