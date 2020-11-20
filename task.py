# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

import diary
from dataclasses import dataclass
import json

@dataclass
class School:
	name : str
	diares : list[diary.Diary]
	def get_total_average_by_name(self,name,surname,class_sign):
		diary = list(filter(lambda x:x.class_sign == class_sign,self.diares))
		student = list(filter(lambda x:x.surname == surname and x.name == name,diary[0].students))
		return diary[0].get_student_total_average(student[0].diary_number)
	
	def get_subject_average_by_name(self,name,surname,class_sign,subject):
		diary = list(filter(lambda x:x.class_sign == class_sign,self.diares))
		student = list(filter(lambda x:x.surname == surname and x.name == name,diary[0].students))
		return diary[0].get_student_subject_average(student[0].diary_number,subject)

	def get_all_students(self):
		return_query = f"{self.name}\n"
		for diary in self.diares:
			return_query = f"{return_query}\t {diary.class_sign}:\n"
			for student in diary.students:
				return_query = f"{return_query}\t\t {student.diary_number}. {student.name} {student.surname}\n"
		return return_query

	def get_all_scores(self):
		return_query = f"{self.name}\n"
		for diary in self.diares:
			return_query = f"{return_query}\t {diary.class_sign}:\n"
			for score in diary.scores:
				return_query = f"{return_query}\t\t {score.score}"
			return_query = f"{return_query}\n"
		return return_query



def load_from_file(path,schools):
	with open(path) as json_file:
		data = json.load(json_file)
		for single_school in data['schools']:
			schools.append(School(single_school['name'],[]))
			for single_diary in single_school['diaries']:
				schools[len(schools)-1].diares.append(diary.Diary([],single_diary['class_sign'],[],[]))
				for single_student in single_diary['students']:

					student_nr = schools[len(schools)-1].diares[len(schools[len(schools)-1].diares)-1].add_student(single_student['name'],single_student['surname'])

				current_diary=schools[len(schools)-1].diares[len(schools[len(schools)-1].diares)-1]

				for single_score in single_student['scores']:
					current_diary.add_score(student_nr,single_score['subject'],float(single_score['score']))

				for single_attendance in single_student['attendances']:
					for single_lesson,single_check in single_attendance['check']:
						current_diary.add_attendance(single_attendance['date'],single_lesson,single_check)

def find_by_name(name,surname,schools):
	for school in schools:
		for diary in school.diares:
			found = list(filter(lambda x : x.name == name and x.surname == surname, diary.students))
			if found:
				return [school,diary]


if __name__ == "__main__":

	schools=[]

	load_from_file("data.json",schools)
	print("Looking for Greg Kowalsky:")
	finder = find_by_name("Greg","Kowalsky",schools)
	print(f"School: {finder[0].name}, Class: {finder[1].class_sign}")
	print("\nGreg Kowalsky total average:\n")
	print(schools[0].get_total_average_by_name("Greg","Kowalsky","1C"))
	print("\nGreg Kowalsky math avarage:\n")
	print(schools[0].get_subject_average_by_name("Greg","Kowalsky","1C","math"))
	print(f"\n{schools[1].diares[0].class_sign} in {schools[1].name} average:\n")
	print(schools[1].diares[0].class_average())
	print(f"\n{schools[1].name} all students\n")
	print(schools[1].get_all_students())
	print(f"\n{schools[1].name} all grades\n")
	print(schools[1].get_all_scores())	