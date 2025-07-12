import numpy as np

def calculate(list):
    # Execption
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Frist transform list to NumPy matrix 3x3
    mtx = np.array(list).reshape(3,3)

    # Create dicctionary using tolist (python list)
    calculations = { 'mean' : [mtx.mean(axis = 0).tolist(), mtx.mean(axis = 1).tolist(), mtx.mean().tolist()],
                    'variance': [mtx.var(axis = 0).tolist(), mtx.var(axis = 1).tolist(), mtx.var().tolist()],
                    'standard deviation': [mtx.std(axis = 0).tolist(), mtx.std(axis = 1).tolist(), mtx.std().tolist()],
                    'max': [mtx.max(axis = 0).tolist(), mtx.max(axis = 1).tolist(), mtx.max().tolist()],
                    'min': [mtx.min(axis = 0).tolist(), mtx.min(axis = 1).tolist(), mtx.min().tolist()],
                    'sum': [mtx.sum(axis = 0).tolist(), mtx.sum(axis = 1).tolist(), mtx.sum().tolist()]
    }

    return calculations