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
    """convert a csv file to a dictionary

    Args:
        path (str, optional): Path of the csv file to convert. Defaults to "".

    Returns:
        dict: the resulting dictionary.
    """
    return pandas.read_csv(path, header=None, index_col=0).to_dict()
  


  # def generate(self, student_id:int=0)->dict:
  
  
