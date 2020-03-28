from config import * 

from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

# Im not sure for this one now- its just a test 
from datetime import date  

#-- Initiate the database 
db = SQLAlchemy(app)

#-- Migrate object for migrate with app,db as a super class 
migrate = Migrate(app,db)

"""
To constructing the database
follow the below cammands in terminal
1) flask db.init  				 # Initializing the database
2) flask db migrate -m "comment" # creating the migration 
3) flask db upgrade 			 # after each change in construction of database 	
"""

class Workout(db.Model):
	#-- workout table 
	workout_id = db.Column(db.Integer, primary_key=True)
	workout_date = db.Column(db.String(40), nullable=False)
	workout_name = db.Column(db.String(60), nullable=False)
	weight = db.Column(db.Integer, default=0)
	rep = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return  "{}-{}-{}-{}-{}".format(self.workout_id, self.workout_date, self.workout_name, self.weight, self.rep)


def show_all_workouts():
	all_workouts = Workout.query.all()
	return all_workouts

def search_by_name(workout_name):
	workouts = Workout.query.filter_by(workout_name=workout_name).all()
	return workouts 

def search_by_date(workout_date):
	workouts = Workout.query.filter_by(workout_date=workout_date).all()
	return workouts

def search_by_id(workout_id):
	workout = Workout.query.filter_by(workout_id=workout_id).first()
	return workout

def insert_new_workout(workout_date, workout_name, weight, rep):
	new_workout = Workout(workout_date=workout_date, workout_name=workout_name, weight=weight, rep=rep )
	db.session.add(new_workout)
	db.session.commit()

def delete_workout(workout_id):
	workout = Workout.query.filter_by(workout_id=workout_id).first()
	db.session.delete(workout)
	db.session.commit()
	

def update_workout(workout_id, workout_date, workout_name, weight, rep):
	workout = Workout.query.filter_by(workout_id=workout_id).first()
	
	workout.workout_id = workout_id 
	workout.workout_date = workout_date 
	workout.workout_name = workout_name 
	workout.weight = weight 
	workout.rep = rep 
	db.session.commit()
	
	return True  





