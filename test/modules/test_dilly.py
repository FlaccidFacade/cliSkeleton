"""Tests the swapomatic function
"""

import src.modules.silly.magic as magic


def test_swapping():
  """Test the swap_O_Matic function with simple spot check
  should see the first two characters swapped as the result
  """
  swapped = magic.swap_O_Matic('VERY FUN!')

  assert swapped == "EVRY FUN!"


  swapped = magic.swap_O_Matic('')

  assert swapped == ""