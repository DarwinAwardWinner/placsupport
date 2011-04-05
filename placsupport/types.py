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
