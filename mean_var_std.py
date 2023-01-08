import numpy as np


def calculate(list):
  #ensure list is spec length 9
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  # convert input to numpy array for processing
  matrix = np.array(list).reshape(3, 3)

  # dictionary to hold matrix calculations

  calculations = {
    'mean': [
      np.mean(matrix, axis=0).tolist(),
      np.mean(matrix, axis=1).tolist(),
      np.mean(matrix)
    ],
    'variance': [
      np.var(matrix, axis=0).tolist(),
      np.var(matrix, axis=1).tolist(),
      np.var(matrix)
    ],
    'standard deviation': [
      np.std(matrix, axis=0).tolist(),
      np.std(matrix, axis=1).tolist(),
      np.std(matrix)
    ],
    'max': [
      np.max(matrix, axis=0).tolist(),
      np.max(matrix, axis=1).tolist(),
      np.max(matrix)
    ],
    'min': [
      np.min(matrix, axis=0).tolist(),
      np.min(matrix, axis=1).tolist(),
      np.min(matrix)
    ],
    'sum': [
      np.sum(matrix, axis=0).tolist(),
      np.sum(matrix, axis=1).tolist(),
      np.sum(matrix)
    ]
  }

  return calculations
