from abc import ABC, abstractmethod

class absSearch(ABC):
  """Abstract class for searching algorithms
  this allows for easy replacement of the simple linear search
  if real data set is too large for linear search and we need
  a smaller big O complexity

  Args:
      ABC ([type]): [description]
  """
  @abstractmethod
  def find(self, obj:dict={}, target=None)->list:
    """The function used to complete the algorithm.

    Args:
        obj (dict, optional): object to search in. Defaults to {}.
        target (Any): target to search for. Defaults to None.
    Returns:
        list: keys of target values in obj
    """
    pass#TODO Write test to cover this