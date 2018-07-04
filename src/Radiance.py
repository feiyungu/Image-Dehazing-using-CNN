import numpy;

def recover(imgar, atm, t, tmin=0.1):
    """
    Parameters
    -----------
    imgar:    an H*W RGB hazed image
    atm:      the atmospheric light in imgar
    t:        the transmission in imgar 
    tmin:     the minimum value that transmission can take (default=0.1)
    
    Return
    -----------
    The imaged recovered and dehazed, j (a H*W RGB matrix).
    """ 
    
    #the output dehazed image
    j = numpy.zeros(imgar.shape)
    
    #equation (16)
    for c in range(0, imgar.shape[2]):
        j[:,:, c] = ((imgar[:,:,c]-atm[c])/numpy.maximum(t[:,:], tmin))+atm[c]
    
    return j/numpy.amax(j)
