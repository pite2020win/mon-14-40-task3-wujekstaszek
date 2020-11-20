from dataclasses import dataclass
import datetime
import statistics

@dataclass
class Student:
  name: str
  surname: str
  diary_number: int

@dataclass
class Score:
  student_nr: int
  subject: str
  score: int

@dataclass
class Attendance:
  date : datetime.date
  check : list[int,bool]


@dataclass
class Diary:
  students : list[Student]
  class_sign : str
  scores : list[Score]
  attendances : list[Attendance]
  
  def add_score(self,student_nr,subject,new_score):
    if(6<new_score or 1>new_score): 
      return 0;
    self.scores.append(Score(student_nr,subject,new_score))

  def add_student(self,name,surname):
    self.students.append(Student(name,surname,len(self.students)))
    return len(self.students)-1

  def get_student_total_average(self,student_nr):
    scores = list(filter(lambda x: x.student_nr == student_nr,self.scores))
    mean = statistics.mean([x.score for x in scores])
    return mean


  def get_student_subject_average(self,student_nr,subject):
    scores = list(filter(lambda x: x.student_nr == student_nr and x.subject == subject,self.scores))
    mean = statistics.mean([x.score for x in scores])
    return mean


  def add_attendance(self,date:datetime.date,lesson:int,check:bool):
    
    date_attandance = list(filter(lambda x:x.date == date,self.attendances))
    if date_attandance:  
      single_check = list(filter(lambda x:x[0] == lesson,date_attandance[0].check))
      if single_check:
        single_check[0][1] = check    
      else:
        single_check[0].append([lesson,check])
    else:
      date_attandance.append(Attendance(date,[lesson,check]))

  def class_average(self):
    mean = statistics.mean([x.score for x in self.scores])
    return mean