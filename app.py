from config import * 
from forms import * 
from models import * 
from flask import render_template, url_for, redirect
from datetime import date

########################################################### Showing all workouts 
@app.route("/home", methods = ["GET", "POST"])
def home():
	form = SelectWorkout()
	list_of_workouts = []
	all_workouts = show_all_workouts()
	
	all_workouts.reverse()

	for workout in all_workouts:
		if workout.workout_name not in list_of_workouts:
			list_of_workouts.append(workout.workout_name)

	return render_template("home.html", all_workouts=all_workouts, form=form, list_of_workouts=list_of_workouts)

 
"""
class EditWorkout(FlaskForm):
	workout_date = StringField("Workout date")
	workout_name = StringField("Workout")
	weight = IntegerField("Weight")
	rep = IntegerField("Rep")
	update = SubmitField("Update")
	delete = SubmitField("Delete")
"""
########################################################### Single workout with Update and Delete 
@app.route("/<workout_id>", methods=["POST","GET"])
def workout(workout_id):
	workout = search_by_id(workout_id)

	form = EditWorkout(workout_date=workout.workout_date,
					   workout_name=workout.workout_name,
					   weight=workout.weight,
					   rep=workout.rep)
	
	if form.validate_on_submit():
		if form.update.data:
			workout_id = workout_id
			workout_date = form.workout_date.data 
			workout_name = form.workout_name.data 
			weight = form.weight.data
			rep = form.rep.data 
			print(workout_id,",", workout_date,",",workout_name, ",", weight, ",", rep)
			if update_workout(workout_id, workout_date, workout_name, weight, rep) is True:
				return redirect(url_for("home"))

		if form.delete.data:
			delete_workout(workout_id)
			return redirect(url_for("home"))

		if form.add.data:
			workout_date = str(date.today())
			workout_name = form.workout_name.data 
			weight = form.weight.data 
			rep = form.rep.data 
			if weight is None:
				weight = 0 
			insert_new_workout(workout_date, workout_name, weight, rep)
			return redirect(url_for("home"))



	return render_template("single_workout.html", workout_id=workout_id, workout=workout, form=form)

########################################################### Adding new workout record to database
@app.route("/add_workout", methods=["post", "get"])
def add_workout():
	form = InsertWorkout()

	if form.validate_on_submit():
            workout_date = str(date.today())
            workout_name = form.workout_name.data
            weight = form.weight.data
            rep = form.rep.data
            #print(workout_date,",",workout_name, ",", weight, ",", rep) 
            if weight == None:
                weight=0
            insert_new_workout(workout_date, workout_name, weight, rep)
            return redirect (url_for("home"))
	return render_template("add_workout.html", form=form)

########################################################### Search workout by name
@app.route("/workout_by_name", methods=["POST", "GET"])
def workout_by_name():
	form = SearchWorkout()
	if form.validate_on_submit():
		global workouts
		search_subject = form.search.data
		workouts = search_by_name(search_subject)
		if len(workouts) != 0:
			return redirect(url_for("results"))

		else:
			return redirect(url_for('workout_by_name'))
			#-- Here should be result page 
	
	#all_workouts = search_by_name(workout_name)
	return render_template("workouts_by_name.html", form=form)

########################################################### Search workout by Date
@app.route("/workout_by_date", methods=["POST","GET"])
def workout_by_date():
	form = SearchWorkout()
	if form.validate_on_submit():
		global workouts 
		search_subject = form.search.data 
		workouts = search_by_date(search_subject)
		if len(workouts) != 0:
			return redirect(url_for("results"))
		else:
			return redirect(url_for("workout_by_date"))

	return render_template("workouts_by_date.html", form=form)

########################################################### Search results 
@app.route("/results", methods=["POST", "GET"])
def results():
	form = ResultWorkout()
	return render_template("results.html", form=form, workouts=workouts)

if __name__ == "__main__":
	app.run(debug=True)
