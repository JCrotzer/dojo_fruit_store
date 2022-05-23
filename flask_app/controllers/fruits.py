from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.fruit import Fruit

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    totalOrder = int(raspberry) + int(apple) + int(strawberry)
    print('charging ' + first_name + ' ' + last_name + ' for ' + str(totalOrder) + ' fruits')
    return render_template("checkout.html", strawTemp = strawberry, raspTemp = raspberry, appleTemp = apple, totalTemp = totalOrder, firstTemp = first_name, lastTemp = last_name, studentTemp = student_id)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")