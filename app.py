
import csv
import flask

from flask import request, jsonify

# df = pd.read_csv(r'/Users/ah5an_002/ahsanPythonProjects/pythonProject/mfoodfacility.csv')
# restaurants = df.to_json()
# print(restaurants)
with open('mfoodfacility.csv', "r") as f:
    reader = csv.reader(f)
    next(reader)
    restaurants = []
    for row in reader:
        restaurants.append({"locationid": int(row[0]), "Applicant": row[1], 'FacilityType': row[2], 'cnn': row[3],
                            'LocationDescription': row[4],
                            'Address': row[5], 'blocklot': row[6], 'block': row[7], 'lot': row[8], 'permit': row[9],
                            'Status': row[10],'X':row[12], 'Y':row[13], 'Latitude':row[14], 'Longitude':row[15]})

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Testing my Code</h1>"


@app.route('/api/v1/resources/restaurants/all', methods=['GET'])
def api_all():
    return jsonify(restaurants)


@app.route('/api/v1/resources/restaurants', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'locationid' in request.args:
        locationid = int(request.args['locationid'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for restaurant in restaurants:
        if restaurant['locationid'] == locationid:
            results.append(restaurant)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()
