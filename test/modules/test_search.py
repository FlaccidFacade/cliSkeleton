
import src.modules.search.linear_search as ls
import src.modules.search.abs_search as abs

def test_linear_search():
  """quick test to show linear search is working
  """
  a = {'id': 'name', '1': 'A', '2': 'A', '3': 'C'}

  loc = ls.LinearSearch.find(None,a,'A')

  assert loc == ['1','2']


def test_abstract_serach():
  """quick test to show abstract is working
  """
  a = {'id': 'name', '1': 'A', '2': 'A', '3': 'C'}

  loc = abs.AbsSearch.find(None,a,'A')

  assert loc == []