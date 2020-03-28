from config import * 
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from flask_wtf import FlaskForm, Form

class InsertWorkout(FlaskForm):
	
	workout_name = StringField("Workout ")
	weight = IntegerField("Weight ")
	rep = IntegerField("Rep ")
	submit = SubmitField("Add workout")


class SelectWorkout(FlaskForm):
	workout_date = StringField("workout date ")
	workout_name = StringField("Workout ")
	weight = IntegerField("Weight ")
	rep = IntegerField("Rep ")
	submit = SubmitField("Add workout")

class ResultWorkout(FlaskForm):
	workout_date = StringField("workout_date ")
	workout_name = StringField("Workout ")
	weight = IntegerField("Weight ")
	rep = IntegerField("Rep ")

class SearchWorkout(FlaskForm):
	search = StringField("Search ")
	submit = SubmitField("Search ")


class EditWorkout(FlaskForm):
	workout_date = StringField("Workout date ")
	workout_name = StringField("Workout ")
	weight = IntegerField("Weight ")
	rep = IntegerField("Rep ")
	update = SubmitField("Update")
	delete = SubmitField("Delete")
	add = SubmitField("Save as New")