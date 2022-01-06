
from modules.search.abs_search import absSearch


class LinearSearch(absSearch):

  def find(self, obj:dict={}, target=None)->list:
    keys = []

    for (key,value) in obj.items():
      if target == value:
        keys.append(key)
    
    return keys
    