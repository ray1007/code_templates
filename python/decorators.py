import functools
import time

# decorator is basically a high-order function that returns
# a wrapper function which wraps the input function.

# Template of a functional decorator: pure, stateless.
def decorator(func):
    # Use `functiontools.wraps` to preserve 
    # information of the original function.
    @functools.wraps(func)
    # use `args`, `kwargs` to accept any 
    # arguemnts of the paased-in function.
    def wrapper(*args, **kwargs):
        # TODO Do something before
        ret = func(*args, **kwargs)
        # TODO Do something after
        return ret
    return wrapper

# if a decorator takes arguments, then we have to create
# a function that returns a decorator function.


# it is possible to create a stateful decorator
# using function attributes, but I prefer using a class.
# it is more clear about what attributes are present,
# and is an analogy to React's functional & class component.

# class decorator: stateful.
class Decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

        # add decorator states as class attributes

    # make this class a callable object, so it acts 
    # like a functional decorator.
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

# common use cases: 
# - time profiling, sleep, retry
# - type checking, validation
# - automatically put functions in a list (register plugins).
# - debugging, logging, ...

def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        ret = func(*args, **kwargs)
        print("{} took {} secs.".format(func.__name__, time.time()-t_start))
        return ret
    return wrapper
    
def after_exec_sleep(n_secs=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            time.sleep(n_secs)
            return ret
        return wrapper
    return decorator

def register_plugin(plugin_dict):
    def decorator(func):
        plugin_dict[func.__name__] = func
        return func
    return decorator

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling {} with arguments: {}, {}".format(func.__name__, args, kwargs))
        ret = func(*args, **kwargs)
        return ret
    return wrapper


# run examples here.
if __name__ == '__main__':

    # 1. time profiling exmaple
    @measure_time
    def waste_some_time(num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(10000)])

    waste_some_time(10)

    # 2. slow down execution
    @after_exec_sleep(n_secs=1)
    def hello():
        print("hello")

    for _ in range(3):
        hello()

    """
    3. register plugin
    With decorator, we don't have to manually typing
    the functions into a list/dict anymore. No more this:

        plugin_dict = {}
        plugin_dict["func1"] = func1
        ...

    or
        plugins = [
            func1,
            func2,
            func3,
            ...
        ]
    """
    plugin_dict = {}

    @register_plugin(plugin_dict)
    def func1():
        print("Execute function #1")

    @register_plugin(plugin_dict)
    def func2():
        print("Execute function #2")

    @register_plugin(plugin_dict)
    def func3():
        print("Execute function #3")

    print(plugin_dict)
    

    # 4. debug
    @debug
    def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fib(n-2) + fib(n-1)
    
    fib(5)

