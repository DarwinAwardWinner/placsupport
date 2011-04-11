def nonneg_int(s):
    x = int(s)
    if x < 0:
        raise ValueError("%s is not a nonnegative integer" % (s,))
    return(x)

def positive_int(s):
    x = int(s)
    if x <= 0:
        raise ValueError("%s is not a positive integer" % (s,))
    return(x)

def maybe_parse_int(s):
    """Try to parse arg as int, else return unchanged"""
    try:
        return int(s)
    except ValueError:
        return s
