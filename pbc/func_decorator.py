def log_func_args(func):
    """Decorator to log a function name and given arguments to her - func_name(args)"""

    def wrapper(*args):
        if len(args) == 1:
            print("\nInitiate call\n\t>>>{0}({1})".format(func.__name__, args[0]))
        else:
            print("\nInitiate call\n\t>>>{0}{1}".format(func.__name__, str(args)))
        return func(*args)
    return wrapper
