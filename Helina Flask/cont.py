from flask import Flask, render_template,request, redirect
from db import mydb, mycursor


app = Flask(__name__)


@app.route('/')
def index():
    mycursor.execute("SELECT * FROM Meal")
    foods = mycursor.fetchall()
    return render_template('index.html',foods = foods)


@app.route('/gotoadmin')
def gotoadmin():
    mycursor.execute("SELECT * FROM Meal")
    foods = mycursor.fetchall()
    return render_template('admin.html',foods = foods)



@app.route('/addmealpage')
def addmealpage():
    return render_template('addmeal.html')



@app.route('/adddetailspage')
def addchefpage():
    return render_template('adddetail.html')





@app.route('/adddetail', methods=['GET', 'POST'])
def adddetail():
    if request.method == 'GET':
        return redirect('/Student')
    if request.method == 'POST':
          # _ = request.form['name']
        mealname = request.form['mealname']
        chefname = request.form['chefname']
        ingredients = request.form['ingredients']
        chefphoneno = request.form['chefphoneno']

        sql = 'INSERT INTO Detail (meal_name,chef_name,ingredients, chefphoneno) VALUE (%s, %s,%s, %s)'
        val = (mealname, chefname,ingredients,chefphoneno)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('adddetail.html')




@app.route('/makeedit', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'GET':
        return render_template('editdata.html')
    if request.method == 'POST':
        _name = request.form['name']
        _address = request.form['address']
        _age = request.form['age']
        sql = 'INSERT INTO Meal (name, address, age) VALUES (%s, %s, %s)'
        val = (_name, _address, _age)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/')





@app.route('/addmeal', methods=['GET', 'POST'])
def addmeal():
    if request.method == 'GET':
        return redirect('/Student')
    if request.method == 'POST':
          # _ = request.form['name']
        mealname = request.form['mealname']
        preparationtime = request.form['preparationtime']

        sql = 'INSERT INTO Meal (meal_name,preparation_time) VALUE (%s, %s)'
        val = (mealname, preparationtime)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('addmeal.html')
    


@app.route('/getmealdetails', methods=['GET', 'POST'])
def getmealdetails():
    nam = request.form['name']
    mycursor.execute("SELECT * FROM Detail WHERE meal_name = '" + nam + "'")
    foods = mycursor.fetchall()
    return render_template('details.html', foods = foods)
    





@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_food(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM Meal WHERE ID={id}')
        food = mycursor.fetchone()
        return render_template('editfood.html', food = food)
    if request.method == 'POST':
        mealname = request.form['mealname']
        preparationtime = request.form['preparationtime']
        sql = f'UPDATE Meal SET meal_name = %s, preparation_time = %sWHERE ID = %s'
        values = (mealname, preparationtime, id)
        mycursor.execute(sql, values)
        mydb.commit()
        mycursor.execute("SELECT * FROM Meal")
        foods = mycursor.fetchall()
        return render_template('admin.html', foods = foods)


@app.route('/delete/<int:id>')
def delete_food(id):
    sql = f'DELETE FROM Meal WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    mycursor.execute("SELECT * FROM Meal")
    foods = mycursor.fetchall()
    return render_template('admin.html', foods = foods)




if __name__ == '__main__':
        app.run()




