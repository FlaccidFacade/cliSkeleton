import pandas

class Report:


  course_dict = {}
  students_dict = {}
  tests_dict = {}
  marks_dict = {}
  ouput_path = ""
  

  def __init__(self, courses_path:str="", students_path:str="", tests_path:str="", marks_path:str="", ouput_path:str="") -> None:
    """creates dictionaries of csv files

    Args:
        courses_path (str, optional): The path for the courses.csv file. Defaults to "".
        students_path (str, optional): The path for the students.csv file. Defaults to "".
        tests_path (str, optional): The path for the tests.csv file. Defaults to "".
        marks_path (str, optional): The path for the marks.csv file. Defaults to "".
        marks_path (str, optional): The path for the report file. Defaults to "".
    """
    self.course_dict = self._csv2dict(courses_path)
    self.students_dict = self._csv2dict(students_path)
    self.tests_dict = self._csv2dict(tests_path)
    self.marks_dict = self._csv2dict(marks_path)
    self.ouput_path = ouput_path
  
  def _csv2dict(self, path:str="")->dict:
    return pandas.read_csv('csv_file.csv', header=None, index_col=0).to_dict()
  

  def generate(self):
    #get students []
    # by ID and name
    

    # calculate total average

    # get the student's courses
    #  by ID, name, and teacher
    #  calculate the course average


    # start by parsing through marks to get the courses each student is written to

    students = []
  
