import sqlite3 as sql
from flask import Flask, render_template, Response

app = Flask(__name__)

def get_countries():
    try:
        db = sql.connect("blog.db")
        cursor = db.cursor()
        cursor.execute("SELECT country_name, links, capital, country_code, population, currency, cities, images FROM Countries")
        countries = cursor.fetchall()
    except sql.Error as e:
        print(f"Database Error: {e}")
        countries = []
    finally:
        if db:
            db.close()
    return countries

@app.route('/')
def index():
    countries = get_countries()
    return render_template('index.html', countries=countries)

@app.route('/about')
def about_me():
    return render_template('about.html')

def get_education():
    try:
        db = sql.connect("blog.db")
        cursor = db.cursor()
        cursor.execute("SELECT institution_name, grade, extra_inf, gpa FROM Education")
        education = cursor.fetchall()
    except sql.Error as e:
        print(f"Database Error: {e}")
        education = []
    finally:
        if db:
            db.close()
    return education

def get_internships():
    try:
        db = sql.connect("blog.db")
        cursor = db.cursor()
        cursor.execute("SELECT company_name, position, start_date, end_date, location FROM Internships")
        internships = cursor.fetchall()
    except sql.Error as e:
        print(f"Database Error: {e}")
        internships = []
    finally:
        if db:
            db.close()
    return internships

def get_ProfExp():
    try:
        db = sql.connect("blog.db")
        cursor = db.cursor()
        cursor.execute("SELECT company_name, position, start_date, end_date, location FROM ProfExp")
        ProfExp = cursor.fetchall()
    except sql.Error as e:
        print(f"Database Error: {e}")
        ProfExp = []
    finally:
        if db:
            db.close()
    return ProfExp

@app.route('/ptfy')
def portfolio():
    education = get_education()
    internships = get_internships()
    profExp = get_ProfExp()
    return render_template('portfolio.html', education=education, internships=internships, profExp=profExp)

@app.route('/visited')
def visited():
    countries = get_countries()
    return render_template('visited.html', countries=countries)

@app.route('/country/<int:country_id>')
def country(country_id):
    countries = get_countries()
    country_info = countries[country_id - 1] if 0 < country_id <= len(countries) else None
    if not country_info:
        return "Country could not found!"
    return render_template('country.html', country=country_info, country_id=country_id)

@app.route('/image/<int:country_id>')
def image(country_id):
    try:
        db = sql.connect("blog.db")
        cursor = db.cursor()
        cursor.execute("SELECT images FROM Countries WHERE by_order = ?", (country_id,))
        photo_blob = cursor.fetchone()[0]
        if photo_blob:
            return Response(photo_blob, mimetype='image/jpeg')
        return "Photo could not found!", 404
    except sql.Error as e:
        print(f"Database Error!: {e}")
        return "Something went wrong!", 500
    finally:
        if db:
            db.close()

if __name__ == '__main__':
    app.run(debug=True, port=8000)
