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
  weight_err_mess = "Invalid course weights"
  student_err_mess  = "Can't find given student id"
  top_err_mess  = "Problem in student csv"
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
      self.set_search_alg(strategy=strategy)
  
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
  
  def _error(self,message,value=None, info:str=None, level:str="error")->dict:
    """used to generate errors

    Args:
        message ([type]): the error message displayed
        value ([type], optional): used to show variable values. Defaults to None.
        info (str, optional): used to give additional info. Defaults to None.
        level (str, optional): change the level of key. Defaults to "error".

    Returns:
        dict: error created
    """
    err = {level: message}
    if info is not None:
      err["info"] = info
    if value is not None:
      err["value"] = value
    return err

  def _validate_weights(self, courses:list) -> list:
    """get list of weights that are invalid"""

    #get test ids
    test_id_course_id = self.tests_dict.get(1)
    bad_courses = []

    for id in courses:
      #get ids for tests
      keys = self._search(test_id_course_id,id)
      
      #get list of wieghts for ids found
      weights = []
      for k in keys:
        weights.append(self.tests_dict.get(2).get(k))
      
      #check if sum of is 100 or not
      if sum(list(map(float, weights)))  != 100:
        bad_courses.append(id)
   

    return bad_courses

  def _get_course_average(self,uCI:list,marks:list,cI:list,cW:list) -> list:
    """calculate the weighted grades for current the student

    Args:
        uCI (list): unique course ids.
        marks (list): marks.
        cI (list): course ids
        cW (list): course weights

    Returns:
        list: grades
    """
    
    temp_marks = {}
    temp_weights = {}
    
    for i, course in enumerate(uCI):
      #group the marks
      temp_vals = []
      for j, value in enumerate(marks):
        if cI[j] == course:
          temp_vals.append(value)
      temp_marks[str(i)] = temp_vals 

      #group the weights
      temp_vals = []
      for j, value in enumerate(cW):
        if cI[j] == course:
          temp_vals.append(value)
      temp_weights[str(i)] = temp_vals

    #calculate grades
    course_averages = []
    for i in range(len(uCI)):
      course_averages.append(weighted_grade(temp_marks.get(str(i)),temp_weights.get(str(i))))
  

    return course_averages

  def _search(self,obj:dict={},target=None)->list:
    """Execute the searching algorithm

    Args:
        obj (dict, optional): object to search in. Defaults to {}.
        target ([type], optional): target to search for. Defaults to None.

    Returns:
        list: keys of values in obj
    """
    return self.strategy.find(self,obj,target)

  def set_search_alg(self, strategy: absSearch = LinearSearch) -> None:
    """used to set the searching algorithm strategy

    Args:
        strategy (absSearch, optional): the searching algorithm to use. Defaults to LinearSearch.
    """
    self.strategy = strategy



  def write_JSON(self) -> bool:
    #TODO create this

    #make sure output path is specified

    

    pass

  def generate_all(self) -> dict:
    """generate all the students report given their ids

    Returns:
        dict: report of all the students
    """
    students = list(self.students_dict.get(1))
    students.pop(0)
    student_reports = []
    
    for i in students:
      report = self.generate(i)
      student_reports.append(report)
    
    self.report = {"students": student_reports}
    return self.report

  def generate(self, student_id:str="0")-> dict:
    """generate the student report given their id

    student_id as 0 creates a None type object

    Args:
        student_id (str, optional): id of the student for report uses 1 start indexing. Defaults to 0.

    Returns:
        dict: report of the student
    """
    #get the student id postions for the marks file
    mark_student_id = self.marks_dict.get('student_id')
    mark_student_keys = self._search(mark_student_id,student_id)
    if not mark_student_keys:
      return self._error(message=self.student_err_mess,value=student_id)

    #map those keys to test_id and mark
    mark_test_id = []
    marks = []
    for key in mark_student_keys:
      mark_test_id.append(self.marks_dict.get('test_id').get(key))
      marks.append(self.marks_dict.get('mark').get(key))
  
    #map markTestId to course_id and weight
    course_ids = []
    course_weights =[]
    for key in mark_test_id:
      course_ids.append(self.tests_dict.get(1).get(key))
      course_weights.append(self.tests_dict.get(2).get(key))

    unique_course_ids = unique_list(course_ids)
    
    
    #TODO validate weights
    invalid_weights = self._validate_weights(unique_course_ids)

    courses = []
      
    course_averages = self._get_course_average(uCI=unique_course_ids,marks=marks,cI=course_ids,cW=course_weights)
    
    for i in range(len(unique_course_ids)):
      course_report = {}
      if len(invalid_weights) <= 0 or unique_course_ids[i] not in invalid_weights:
        course_report["id"] = int(unique_course_ids[i])
        course_report["name"] = self.course_dict.get(1).get(unique_course_ids[i])
        course_report["teacher"] = self.course_dict.get(2).get(unique_course_ids[i])
        course_report["courseAverage"] = float(format(course_averages[i],'.1f'))
        
      else:
        course_report = self._error(self.weight_err_mess, value=float(format(course_averages[i],'.1f')), info= "Course grades still not included in total averages")

      courses.append(course_report)

    #calculate students total average 
    
    total_average = sum(course_averages)/len(course_averages)

    # create student report
    self.report = {"id": int(student_id), "name": self.students_dict.get(1).get(student_id), 
                      "totalAverage": float(format(total_average,'.2f')), "courses": courses}
    return self.report
