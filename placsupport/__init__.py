import plac

# Don't ask.
# http://stackoverflow.com/questions/4492559
def _giveupthefunc(depth=1):
    """Return the calling function.

This returns the actual function object, not its name. The function object can be used to get the plac help text.

Obviously, there are edge cases for which the function fails. None of them are likely to occur in practice."""
    import inspect, gc
    frame = inspect.currentframe(depth)
    code  = frame.f_code
    globs = frame.f_globals
    functype = type(lambda: 0)
    funcs = []
    for func in gc.get_referrers(code):
        if type(func) is functype:
            if getattr(func, "func_code", None) is code:
                if getattr(func, "func_globals", None) is globs:
                    funcs.append(func)
                    # if len(funcs) > 1:
                    #     return None
    return funcs[0] if funcs else None

# Utilities for showing help text and argument error messages
def get_plac_parser(depth=1):
    """Get the plac-generated parser for the calling function.

With optional arg 'depth', get the parser for the function that far up the call stack."""
    func = _giveupthefunc(depth=depth+1)
    if func:
        return plac.parser_from(func)
    else:
        raise ValueError("Could not find function at specified depth")

def print_help(depth=1):
    """Print help text inferred by plac for calling function

If 'depth' is specified, then the help text is printed for the function that far up the call stack."""
    get_plac_parser(depth + 1).print_help()

def get_help_text(depth=1):
    """Same as print_help, but returns the help text instead of printing it."""
    return get_plac_parser(depth + 1).format_help()

def argument_error(message, depth=1):
    """Print error message, followed by the help text, then exit

    Depth has the same meaning as for print_help."""
    get_plac_parser(depth + 1).error(message)

def assert_arg_cond(assertion, message, depth=1):
    """Like assert, but uses argument_error() to to print the error"""
    try:
        assert assertion, message
    except AssertionError, e:
        print_argument_error(e.args[0], depth + 1)
