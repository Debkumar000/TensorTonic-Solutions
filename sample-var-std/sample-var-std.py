import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    sum_ = 0
    mean_ = np.mean(x)
    for i in x:
        y = i-mean_
        y2 = y*y
        sum_+=y2
    vari = sum_/(len(x)-1)
    sd = np.sqrt(vari)
    return (vari, sd)
    pass