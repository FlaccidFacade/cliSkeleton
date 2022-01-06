
from src.modules.search.linear_search import LinearSearch


def test_linear_search():
  """quick test to show linear search is working
  """
  a = {'id': 'name', '1': 'A', '2': 'A', '3': 'C'}

  loc = LinearSearch.find(None,a,'A')

  assert loc == ['1','2']
