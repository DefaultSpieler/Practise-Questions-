#Grading Program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for score in student_scores:
  	if student_scores[score] >= 91:
  		student_grades[score] = "Outstanding"
  	elif student_scores[score] >= 81 and student_scores[score] <= 90:
  		student_grades[score] = "Exceeds Expectations"
  	elif student_scores[score] >= 71 and student_scores[score] <= 80:
  		student_grades[score] = "Acceptable"
  	else:
  		student_grades[score] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

#Dictionary in List

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, times, places):
	new_dic = {}
	new_dic["country"] = country
	new_dic["visits"] = times
	new_dic["cities"] = places
	travel_log.append(new_dic)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
