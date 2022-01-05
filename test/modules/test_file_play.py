"""Tests the swapomatic function
"""

import src.modules.file_play.csv_to_JSON as c2j


# def test_dict_to_JSON():
  

def test_csv_to_dict():
  """Test the c2j function with simple spot check
  epecting to see the csv files as a dictionary type
  """
  report = c2j.Report("./e2/courses.csv", "e2/students.csv", "e2/tests.csv", "e2/marks.csv", "e2/output.json")

  assert getattr(report,'students_dict')