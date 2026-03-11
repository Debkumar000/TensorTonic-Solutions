import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if np.allclose(np.sum(p), 1):
        sum_ = 0
        for i in range(0, len(x)):
            sum_ = sum_+(x[i]*p[i])
        pass
        
    else:
        raise ValueError("Invalid probabilities")
    return sum_   
    pass
