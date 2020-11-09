import dataclass
import student
import score
import time
@dataclass

class diary:
  students : list[student.student]
  class_sign : str
  scores : list[score.score]
  attendance : list[list[time.date,int]]
  
  def add_score(self,student_nr,subject,score):
    if(6<score or 1>score): 
      return 0;
    self.scores.append(score.score(student_nr,subject,score))

  def add_student(self,name,surname):
    #to powinna być zaawansowana logika zmiany numeru, tak by były alfabetycznie, ale nie ma czasu :(
    self.students.append(student.student(name,surname,len(self.students)))
    return len(self.students)-1

def get_student_total_avarage(self,student_nr):
  score_sum = 0;
  cnt = 0;
  for single_score in self.scores:
    if single_score.student_nr == student_nr:
      score_sum += single_score.score
      cnt += 1
  return score_sum/cnt

def get_student_subject_avarage(self,student_nr,subject):
  score_sum = 0;
  cnt = 0;
  for single_score in self.scores:
    if single_score.student_nr == student_nr and single_score.subject == subject:
      score_sum += single_score.score
      cnt += 1
  return score_sum/cnt

