import os 
from models import * 


"""
Workout schema:
	workout_id = db.Column(db.Integer, primary_key=True)
	workout_date = db.Column(db.String(40), nullable=False)
	workout_name = db.Column(db.String(60), nullable=False)
	weight = db.Column(db.Integer, default=0)
	rep = db.Column(db.Integer, nullable=False)
"""

def insert(workout_name, weight, rep):
	workout_date = str(date.today())
	new_workout = Workout(workout_date = workout_date, workout_name = workout_name, weight = weight, rep = rep)
	db.session.add(new_workout)
	db.session.commit()


	print("Inserted")


def all_workouts():
	workouts = Workout.query.all()
	for workout in workouts:
		print(workout)


global final_date
temp_date = []

def get_date():
	enter_year()

def enter_year():
	count = 0
	year = input("Enter year: ")
	for c in year:
		count += 1
	if count != 4:
		print("Wrong year")
		enter_year()
	for i in year:
		if i.isdigit() != True:
			print("Enter numeric values")
			enter_year()
	
	temp_date.append(year)
	enter_month()

def enter_month():
	count = 0 
	month = input("Month: ")

	for c in month:
		count += 1
	if count != 2:
		print("Wrong month")
		enter_month()
	for i in month:
		if i.isdigit() != True:
			print("Enter numeric values")
			enter_month()

	temp_date.append(month)
	enter_day()

def enter_day():
	count = 0 
	day = input("Day: ")

	for i in day:
		count += 1
	if count != 2:
		print("Wrong day!")
		enter_day()
	for i in day:
		if i.isdigit() != True:
			print("Enter numeric values")
			enter_day()
	temp_date.append(day)

	
	final_date = (temp_date[0]+"-"+temp_date[1]+"-"+temp_date[2])
	
	return final_date


def search_by_date():
	get_date()
	workout = Workout.query.filter_by(workout_date=final_date).all()
	if len(workout) != 0:
		print(workout)

	else:
		print("No record found")