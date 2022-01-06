import pandas
from modules.search.abs_search import absSearch
from modules.search.linear_search import LinearSearch
from modules.helpers.list_operations import unique_list
from modules.helpers.math import weighted_grade


class Report:

  course_dict = {}
  students_dict = {}
  tests_dict = {}
  marks_dict = {}
  ouput_path = ""
  report = {}
  strategy: absSearch

  def __init__(self, courses_path:str, students_path:str, tests_path:str, marks_path:str, ouput_path:str, strategy:absSearch=None) -> None:
    """creates dictionaries of csv files

    Args:
        courses_path (str): The path for the courses.csv file. 
        students_path (str): The path for the students.csv file. 
        tests_path (str): The path for the tests.csv file. 
        marks_path (str): The path for the marks.csv file.
        marks_path (str, optional): The path for the report file. Defaults to None.
    """
    self.course_dict = self._csv2dict(courses_path)
    self.students_dict = self._csv2dict(students_path)
    self.tests_dict = self._csv2dict(tests_path)
    self.marks_dict = self._csv2dict(marks_path,None,uc=["test_id","student_id","mark"])
    self.ouput_path = ouput_path
    if strategy == None:
      self.set_search_alg()
    else:
      self.set_search_alg(strategy=strategy) #TODO Write test to cover this
  
  def _csv2dict(self, path:str="",ic:int=0,uc:list=None)->dict:
    """convert a csv file to a dictionary

    Args:
        path (str, optional): Path of the csv file to convert. Defaults to "".
        ic (int, optional): index col to use for read_csv. Defaults to 0.
        uc (list, optional): name of columes to use for read_csv. Defaults to None.
    Returns:
        dict: the resulting dictionary.
    """
    return pandas.read_csv(path, header=None, index_col=ic,names=uc).to_dict()
  
  def set_search_alg(self, strategy: absSearch = LinearSearch) -> None:
    """used to set the searching algorithm strategy

    Args:
        strategy (absSearch, optional): the searching algorithm to use. Defaults to LinearSearch.
    """
    self.strategy = strategy

  def search(self,obj:dict={},target=None)->list:
    """Execute the searching algorithm

    Args:
        obj (dict, optional): object to search in. Defaults to {}.
        target ([type], optional): target to search for. Defaults to None.

    Returns:
        list: keys of values in obj
    """
    return self.strategy.find(self,obj,target)

  def write_JSON(self) -> bool:
    #TODO create this

    #make sure output path is specified

    

    pass

  def generate_all(self) -> dict:
    """generate all the students report given their ids

    Returns:
        dict: report of all the students
    """
    numOfStudents = len(self.students_dict.get(1)) - 1
    studentReports = []
    for i in range(numOfStudents):
      studentReports.append(self.generate(i+1))
    
    self.report = {"students": studentReports}
    return self.report

  def generate(self, student_id:int=0)-> dict:
    """generate the student report given their id

    student_id as 0 creates a None type object

    Args:
        student_id (int, optional): id of the student for report. Defaults to 0.

    Returns:
        dict: report of the student
    """
    #get the student id postions for the marks file
    markStudentId = self.marks_dict.get('student_id')
    markStudentKeys = self.search(markStudentId,str(student_id))
    if not markStudentKeys:
      return

    #map those keys to test_id and mark
    markTestId = []
    marks = []
    for key in markStudentKeys:
      markTestId.append(self.marks_dict.get('test_id').get(key))
      marks.append(self.marks_dict.get('mark').get(key))
  
    #map markTestId to course_id and weight
    courseIds = []
    courseWeights =[]
    for key in markTestId:
      courseIds.append(self.tests_dict.get(1).get(key))
      courseWeights.append(self.tests_dict.get(2).get(key))

    uniqueCourseIds = unique_list(courseIds)
    
    #get course averages
    courseAverages = self.get_course_average(uCI=uniqueCourseIds,marks=marks,cI=courseIds,cW=courseWeights)

    courses = []
    for i in range(len(uniqueCourseIds)):
      courseReport = {}
      courseReport["id"] = int(uniqueCourseIds[i])
      courseReport["name"] = self.course_dict.get(1).get(uniqueCourseIds[i])
      courseReport["teacher"] = self.course_dict.get(2).get(uniqueCourseIds[i])
      courseReport["courseAverage"] = float(format(courseAverages[i],'.1f'))
      courses.append(courseReport)

    #calculate students total average 
    totalAverage = sum(courseAverages)/len(courseAverages)
    
    # create student report
    self.report = {"id": int(student_id), "name": self.students_dict.get(1).get(str(student_id)), 
                      "totalAverage": float(format(totalAverage,'.2f')), "courses": courses}
    return self.report
  

  def get_course_average(self,uCI:list,marks:list,cI:list,cW:list) -> list:
    """calculate the weighted grades for current the student

    Args:
        uCI (list): unique course ids.
        marks (list): marks.
        cI (list): course ids
        cW (list): course weights

    Returns:
        list: grades
    """
    
    tempMarks = {}
    tempWeights = {}
    
    for i, course in enumerate(uCI):
      #group the marks
      tempVals = []
      for j, value in enumerate(marks):
        if cI[j] == course:
          tempVals.append(value)
      tempMarks[str(i)] = tempVals 

      #group the weights
      tempVals = []
      for j, value in enumerate(cW):
        if cI[j] == course:
          tempVals.append(value)
      tempWeights[str(i)] = tempVals

    #calculate grades
    courseAverages = []
    for i in range(len(uCI)):
      courseAverages.append(weighted_grade(tempMarks.get(str(i)),tempWeights.get(str(i))))

    return courseAverages