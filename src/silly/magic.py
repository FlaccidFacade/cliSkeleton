"""This is a simple example of a py file
From this file you should follow the patterns of
documentation, type hinting, and style.

This style is to assure readability over
speed, efficiency, or simplicity.

Author: Zachary Turner
Contributers:
Credit:
"""


def swap_O_Matic(word: str = "") -> str:
  """Swaps the first two letters of a string.

  Args:
      word (str, optional): A word of any length. Defaults to "".

  Returns:
      str: The given word with swapped characters
  """

  #test for preconditions and exit early
  wordLength = len(word)
  if wordLength < 2:
      return word


  #swap the first two characters
  #python string does not support item assignment
  newWord = word[1] + word[0] + word[2:]

  return newWord



