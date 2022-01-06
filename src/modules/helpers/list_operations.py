

def multiply_lists(l1:list=[], l2:list=[]) -> list:
  """multiply two lists to a list products
    preconditions:
      lists must hold values that are divisible
  Args:
      l1 (list, optional): factors1. Defaults to [].
      l2 (list, optional): factors2. Defaults to [].

  Returns:
      list: products
  """
  return [ float(x) * float(y) for x, y in zip(l1,l2)]



def unique_list(l1:list=[]) -> list:
  """Create a new list with only unique values from the given

  Args:
      l1 (list, optional): The list to trim. Defaults to [].

  Returns:
      list: unique values from given list
  """

  unique = []

  for x in l1:
    if x not in unique:
      unique.append(x)

  return unique