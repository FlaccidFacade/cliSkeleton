
from modules.search.abs_search import absSearch


class LinearSearch(absSearch):

  def find(self, obj:dict={}, target=None)->list:
    """searches dictionary values for target and returns keys if found

    Args:
        obj (dict, optional): dictionary to search. Defaults to {}.
        target ([type], optional): target to search for. Defaults to None.

    Returns:
        list: list of keys
    """
    keys = []
    for (key,value) in obj.items():
      if target == value:
        keys.append(key)
    
    return keys
    