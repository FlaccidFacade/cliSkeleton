"""Tests the swapomatic function
"""

import src.modules.file_play.csv_to_JSON as c2j


def test_csv_to_dict():
  """Test the c2j function with simple spot check
  epecting to see the csv files as a dictionary type
  """
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example1/tests.csv", "Example1/marks.csv", "Example1/output.json")
  stud_dict = getattr(report,'students_dict')
  course_dict = getattr(report,'course_dict')
  marks_dict = getattr(report,'marks_dict')
  tests_dict = getattr(report,'tests_dict')
  assert stud_dict == {
    1: {'id': 'name', '1': 'A', '2': 'B', '3': 'C'}}
  assert course_dict =={
    1: {'id': 'name', '1': 'Biology', '2': 'History', '3': 'Math'}, 
  2: {'id': 'teacher', '1': 'Mr. D', '2': ' Mrs. P', '3': ' Mrs. C'}}
  assert marks_dict == {
  'test_id': {0: 'test_id', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '1', 9: '2', 10: '3', 11: '6', 12: '7', 13: '1', 14: '2', 15: '3', 16: '4', 17: '5',18: '6',19: '7'}, 
  'student_id': {0: 'student_id', 1: '1', 2: '1', 3: '1', 4: '1', 5: '1', 6: '1', 7: '1', 8: '2', 9: '2', 10: '2', 11: '2', 12: '2', 13: '3', 14: '3', 15: '3', 16: '3', 17: '3', 18: '3', 19: '3'}, 
  'mark': {0: 'mark', 1: '78', 2: '87', 3: '95', 4: '32', 5: '65', 6: '78', 7: '40', 8: '78', 9: '87', 10: '15', 11: '78', 12: '40', 13: '78', 14: '87', 15: '95', 16: '32', 17: '65', 18: '78', 19: '40'}}
  
  
  assert tests_dict == {
    1: {'id': 'course_id', '1': '1', '2': '1', '3': '1', '4': '2', '5': '2', '6': '3', '7': '3'},
   2: {'id': 'weight', '1': '10', '2': '40', '3': '50', '4': '40', '5': '60', '6': '90', '7': '10'}}



def test_set_search_strat():
  """simple test to show that the strategy is being set
  """
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example1/tests.csv", "Example1/marks.csv", "Example1/output.json")
  
  
  assert  getattr(report,'strategy') is not None

def test_generate_one_student():
  """show the generation of one student
  """
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example1/tests.csv", "Example1/marks.csv", "Example1/output.json")
  
  assert report.generate(2) == {
                                "id": 2, 
                                "name": "B", 
                                "totalAverage": 62.15, 
                                "courses": [
                                  {
                                    "id": 1,
                                    "name":"Biology",
                                    "teacher": "Mr. D",
                                    "courseAverage": 50.1
                                  },
                                  {
                                    "id": 3,
                                    "name":"Math",
                                    "teacher": " Mrs. C",
                                    "courseAverage": 74.2
                                  }
                                ]
                              }

def test_generate_single_error_no_student():
  """test to see if generate handles improper value and
  creates the error report sepcified in the object
  """
  
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example1/tests.csv", "Example1/marks.csv", "Example1/output.json")
  

  assert report.generate(4) == getattr(report,'err')

def test_generate_single_error_no_student_proper_message():
  """test to see if generate handles improper value and
  creates an error report and the error report is correct
  """
  
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example1/tests.csv", "Example1/marks.csv", "Example1/output.json")
  
  assert report.generate(4) == {"error": "Invalid course weights"}

def test_generate_single_error_bad_weights():
  """test to see if generate handles improper value and
  creates the error report sepcified in the object
  """
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example3/tests.csv", "Example1/marks.csv", "Example1/output.json")
  
  assert report.generate(1) == getattr(report,'err')

def test_generate_all_error_bad_weights():
  """test to see if generate_all handles improper value and
  creates the error report sepcified in the object
  """
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example3/tests.csv", "Example1/marks.csv", "Example1/output.json")
  
  assert report.generate_all() == getattr(report,'err')

def test_generate_all_students():
  """test to see report output"""
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example1/tests.csv", "Example1/marks.csv", "Example1/output.json")
  

  assert report.generate_all() is not None
  #TODO spot check result



def test_generate_all_students_2():
  """test to see report output"""
  report = c2j.Report("Example2/courses.csv", "Example2/students.csv", "Example2/tests.csv", "Example2/marks.csv", "Example2/output.json")
  
  #TODO add 2nd example for testing
  assert report.generate_all() is not None
  #TODO spot check result