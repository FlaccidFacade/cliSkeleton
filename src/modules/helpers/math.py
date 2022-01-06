
from src.modules.helpers.list_operations import multiply_lists

def weighted_grade(grades:list=[],weights:list=[]) -> float:
  """calculate the weighted grade for given grades and weights

  Args:
      grades (list, optional): [description]. Defaults to [].
      weights (list, optional): [description]. Defaults to [].

  Returns:
      float: weighted grade result
  """
  #check if args are sames length
  if not (len(grades) == len(weights)):
    return None
  
  weight = sum(list(map(int, weights)))

  if weight == 100:
    return sum(multiply_lists(grades,weights))/weight
  else:
    return None
