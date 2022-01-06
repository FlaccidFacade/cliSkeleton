"""Tests the report class
"""

import modules.conversion.csv_to_json as c2j


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
  
  assert report.generate('2') == {
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
  creates an error report
  """
  
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example1/tests.csv", "Example1/marks.csv", "Example1/output.json")
  
  assert report.generate(4) == {'error': "Can't find given student id", 'value': 4}

def test_generate_single_error_bad_weights():
  """test to see if generate handles improper value and
  creates the error report 
  """
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example3/tests.csv", "Example1/marks.csv", "Example1/output.json")
  
  output = report.generate(1)
  assert output == {'error': "Can't find given student id", 'value': 1}

def test_generate_all_error_bad_weights():
  """test to see if generate_all handles improper value and
  creates the error report
  """
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example3/tests.csv", "Example1/marks.csv", "Example1/output.json")
  output = report.generate_all()
  assert len(list(output.items())[0]) == 2
  assert list(output.items())[0][1][1]["courses"][0]["error"] == "Invalid course weights"
  assert list(output.items())[0][1][1]["courses"][0]["value"] == 46.2
  assert list(output.items())[0][1][2]["courses"][2]["id"] == 3

def test_generate_all_students_1():
  """test to see report output for example 1"""
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example1/tests.csv", "Example1/marks.csv", "Example1/output.json")
  
  output = report.generate_all()
  #spot check
  assert len(list(output.items())[0][1]) == 3
  assert len(list(output.items())[0][1][0]["courses"]) == 3
  assert list(output.items())[0][1][2]["totalAverage"] == 72.03
  assert list(output.items())[0][1][0]["courses"][0]["courseAverage"] == 90.1
  assert list(output.items())[0][1][0]["courses"][2]["courseAverage"] == 74.2
  assert list(output.items())[0][1][2]["courses"][2]["name"] == "Math"

def test_generate_all_students_2():
  """test to see report output for example 2"""
  report = c2j.Report("Example2/courses.csv", "Example2/students.csv", "Example2/tests.csv", "Example2/marks.csv", "Example2/output.json")
  
  output = report.generate_all()

  #spot check
  assert list(output.items())[0][1][0]["name"] == "D"
  assert list(output.items())[0][1][0]["id"] == 5
  assert list(output.items())[0][1][0]["totalAverage"] == 26.55
  assert len(list(output.items())[0][1][0]["courses"]) == 2
  assert list(output.items())[0][1][0]["courses"][0]["courseAverage"] == 51.8


def test_write():
  """test to see report file example 1
  this tests isolates the report class from the click module
  """

  #create report object given the file paths specified
  report = c2j.Report("Example1/courses.csv", "Example1/students.csv", "Example1/tests.csv", "Example1/marks.csv", "Example1/output.json")
  
  #generate a report for all students in files
  report.generate_all()
  #write the report to JSON file
  report.write_JSON()

  #manually tested file with diff checker
  #tested output.json against given output
  assert True

def test_write_2():
  """test to see report file example 2
  this tests isolates the report class from the click module
  """

  #create report object given the file paths specified
  report = c2j.Report("Example2/courses.csv", "Example2/students.csv", "Example2/tests.csv", "Example2/marks.csv", "Example2/output.json")
  
  #generate a report for all students in files
  report.generate_all()
  #write the report to JSON file
  report.write_JSON()

  #manually tested file with diff checker
  #tested output.json against given output 
  assert True