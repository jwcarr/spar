import numpy as np

class spar:

  def __init__(self, space):
    if type(space) == tuple:
      self.__space = np.zeros(space, dtype=int)
    else:
      self.__space = np.asarray(space, dtype=int)

  def __len__(self):
    return len(np.unique(self.__space))

  def __str__(self):
    return self.__space.__str__()

  def __getitem__(self, key):
    if type(key) == tuple:
      return self.__space[key]
    return list(map(tuple, np.transpose(np.where(self.__space==key))))

  def __setitem__(self, key, value):
    if type(key) == tuple:
      self.__space[key] = value
    else:
      raise TypeError('Index must be tuple')

  def __iter__(self):
    self.spar_iterator = np.ndenumerate(self.__space)
    return self

  def __next__(self):
    return self.spar_iterator.__next__()

  def next(self): # For Python 2 compatibility
    return self.spar_iterator.__next__()

  def labels(self):
    for label in np.unique(self.__space):
      yield label

  def points(self):
    for point in np.ndindex(self.__space.shape):
      yield point

  def subsets(self):
    for subset_label in np.unique(self.__space):
      yield list(map(tuple, np.transpose(np.where(self.__space==subset_label))))

  def shape(self):
    return self.__space.shape

  def size(self):
    return np.product(self.__space.shape)
