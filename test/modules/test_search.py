
from src.modules.search.linear_search import LinearSearch 
import src.modules.file_play.csv_to_JSON as c2j


def test_linear_search():
  """quick test to show linear search is working
  """
  a = {'id': 'name', '1': 'A', '2': 'A', '3': 'C'}

  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example1/tests.csv", "Example1/marks.csv", "Example1/output.json")
  
  loc = report.search(a,'A')

  assert loc == ['1','2']
