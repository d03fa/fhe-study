

class BGV_PARAM:
    n = 0
    q = 0
    x = None


def ParamGen(l, P, K, B) -> BGV_PARAM:
    '''
    Parameters
    ----------
    l : int
        Security level
    P : int
        An integer plaintext modulus, P > 1
    K : int
        An integer vector length, K >= 1
    B : int
        Maximum multiplicative depth
    '''
    if P <= 1:
        return None
    if K < 1:
        return None
    if B < 1:
        return None
    
    params = BGV_PARAM()

    # TODO: Set parameters

    return params

def SecKeygen(params: BGV_PARAM):
    # TODO: Create ring element s 
    pass

def PubKeygen(params: BGV_PARAM):
    # TODO: Create ring element a
    # TODO: Create ring element s
    # TODO: Create error from x
    # return key tuple (a, a*s + p*e)
    pass


