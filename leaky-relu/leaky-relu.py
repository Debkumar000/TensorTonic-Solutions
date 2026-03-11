import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    x = np.array(x)
    x = np.where(x<0, x*alpha, x)
    return x
    # lst = []
    # for i in x:
    #     if i<0:
    #         a = i*alpha
    #         lst.(a)
    #     else:
    #         list.append(i)
    # return lst
    pass