from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}    
    def inner(*args):        
        if args in cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache[args] = func(*args)
        return cache[args]
    return inner