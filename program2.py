# This program runs the API based output in web interface
# API Can be used to by other programs

import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Function stores results in the dictionary format
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Food Location Archive</h1>
<p>A prototype API for finding close by food locations.</p>'''


# @app_route specifies the querystring location
@app.route('/api/v1/resources/food/all', methods=['GET'])
# api_all will fetch all the results on web
def api_all():
    conn = sqlite3.connect('data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    all_foods = cur.execute('SELECT * FROM mfoodfacility').fetchall()

    return jsonify(all_foods)


# If user enters an incorrect api url throw an error
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# this app_route tells the program to use the get method and uses query parameters refer the statement
# query_parameters= request.args means the program will treat anything specified after "?" as parameter  i.e as
#  in below url change the querystring after running the program (on web browser)
# http://127.0.0.1:5000/api/v1/resources/food?Latitude=37.76&Longitude=-122.42730642251331
@app.route('/api/v1/resources/food', methods=['GET'])
def api_filter():
    query_parameters = request.args
    status = "APPROVED"
    lat = query_parameters.get('Latitude')
    lon = query_parameters.get('Longitude')

    # author = query_parameters.get('author')
    # Create a function to check the input parameter from the user -> Input Validation
    # We want to ensure we get the right parameters
    # check_user_input checks if a numerical value is entered by the use returns true if it finds a number
    def check_user_input(inpu):
        try:
            # Convert it into integer
            int(inpu)
            # print("Input is an integer number. Number = ", val)
            return True
        except ValueError:
            try:
                # Convert it into float
                float(inpu)

                return True
            except ValueError:
                return False

    conn = sqlite3.connect('data.db')
    # conn.row_factory = dict_factory
    cur = conn.cursor()
    '''Microsoft challenge has  shared  a file,  which has some food location  status as Approved. We want 
    to ensure we are checking the inputs distance  against the Approved location.
    lat and lon are variable  which will store user specified latitudes and longitudes value 
    c is storing the cursor object  which provides the attribute lastrowid that is used to fetch the last auto-generated ID
    '''
    # this is one thing I could have done better .Could have separated the common code to another file.
    if (check_user_input(lat)) & (check_user_input(lon)):

        cur.execute("SELECT * FROM mfoodfacility f where f.Status=? "
                    "order by ABS(f.Latitude - (?)) + ABS(f.Longitude - (?)) ASC LIMIT 5", (status, lat, lon,))
        result = cur.fetchall()
        if result:  # result could be None or tuple (record)
            print(result)
        else:
            print("No result found for the location .Please check the latitudes and Longitudes")
    else:
        print("Please enter valid inputs")

    return jsonify(result)


app.run()
