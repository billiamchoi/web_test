from flask import Flask, render_template
from flask import request
import pymysql
from flask import jsonify

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='web_test', charset="utf8")
cursor = db.cursor()

app = Flask(__name__)
#
@app.route("/", methods = ["GET"])
def main():
	return render_template('index.html')
#
@app.route("/student_score", methods = ["GET"])
def get_student_score():
	sql = "select * from student_score"
	cursor.execute(sql)
	db.commit()
	results = cursor.fetchall()
	students = []
	for result in results:
		students.append({
			"id" : result[0],
			"name" : result[1],
			"korean" : result[2],
			"math" : result[3],
			"english" : result[4]
		})
	return jsonify(students)

@app.route("/student_score/create", methods = ["POST"])
def create_student_score():
	name = request.form["name"]
	korean = request.form["korean"]
	math = request.form["math"]
	english = request.form["english"]
	sql = "insert into student_score (name, korean, math, english) values ('%s', %s, %s, %s)" %(name, korean, math, english)
	cursor.execute(sql)
	db.commit()
	return "ok"

@app.route("/student_score/edit", methods = ["PUT"])
def edit_student():
	name = request.form["name"]
	korean = request.form["korean"]
	math = request.form["math"]
	english = request.form["english"]
	sql = "update student_score set korean = %s, math = %s, english = %s  where name = '%s'" %(korean, math, english, name)
	cursor.execute(sql)
	db.commit()
	return "ok"

@app.route("/student_score/delete", methods = ["DELETE"])
def delete_student():
	name = request.form["name"]
	sql = "delete from student_score where name = '%s'" %(name)
	cursor.execute(sql)
	db.commit()
	return "ok"

@app.route("/student_score/kor_align", methods = ["GET"])
def get_student_score_order_by_kor():
	sql = "select * from student_score order by korean desc"
	cursor.execute(sql)
	db.commit()
	results = cursor.fetchall()
	students = []
	for result in results:
		students.append({
			"id" : result[0],
			"name" : result[1],
			"korean" : result[2],
			"math" : result[3],
			"english" : result[4]
		})
	return jsonify(students)

@app.route("/student_score/math_align", methods = ["GET"])
def get_student_score_order_by_math():
	sql = "select * from student_score order by math desc;"
	cursor.execute(sql)
	db.commit()
	results = cursor.fetchall()
	students = []
	for result in results:
		students.append({
			"id" : result[0],
			"name" : result[1],
			"korean" : result[2],
			"math" : result[3],
			"english" : result[4]
		})
	return jsonify(students)

@app.route("/student_score/eng_align", methods = ["GET"])
def get_student_score_order_by_eng():
	sql = "select * from student_score order by english desc;"
	cursor.execute(sql)
	db.commit()
	results = cursor.fetchall()
	students = []
	for result in results:
		students.append({
			"id" : result[0],
			"name" : result[1],
			"korean" : result[2],
			"math" : result[3],
			"english" : result[4]
		})
	return jsonify(students)

if __name__ == "__main__":
	app.run(debug=True)
