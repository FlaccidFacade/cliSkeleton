
import src.modules.helpers.list_operations as lo
import src.modules.helpers.math as math

def test_list_multiplication():
  """quick test to show list multiplication is calclulating correctly
  """
  factor1 = [ 100,100,100]
  factor2 = [1, 2, 5]
  assert lo.multiply_lists(factor1,factor2) == [100,200,500]

def test_weighted_grade():
  """quick test to show weighted grades is calclulating correctly
  """
  weights = [10,40,50]
  grades = [78,87,15]
  assert math.weighted_grade(grades,weights) == 50.1