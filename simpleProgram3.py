'''
This program uses a simple algorith to find the closest food trucks from the input locations (or your current locations)

Algorithm steps
1) Create a temporary database in the program memory
2) Use the temporary database and copy the data supplied into the temp database
3) Add a column to the temp database to store the calculated distance from the input locations
4) Find the distance of all the food locations from your location (input location) and store it iteratively to into the memory database
against the corresponding locationid
5) sort the database by distance and show the top 5 results to show the closest distances



'''



# Import sqllite to use sql with python
import sqlite3
import geopy
from geopy.distance import geodesic as GD

# Establish dataBase connection and store it in connection parameter
conn = sqlite3.connect('data.db')
# Create a database in memory so we can work from the copy of the data and not manipulate the real database
new_db = sqlite3.connect(':memory:')  # create a memory database

query = "".join(line for line in conn.iterdump())

# Dump old database in the new one.
new_db.executescript(query)


# Create a function to check the input parameter from the user -> Input Validation
# We want to ensure we get the right parameters
# check_user_input checks if a numerical value is entered by the user and  returns true if it finds a number
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)

        return True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)

            return True
        except ValueError:
            return False


'''The challenge shares a file which has some food location  status as approved. We want to ensure we are checking the 
location against the Approved location.
lat and lon are variable  which will store user specified latitudes and longitudes value 
c is storing the cursor object  which provides the attribute lastrowid that is used to fetch the last auto-generated ID
'''
status = "APPROVED"
lat = input("Latitude ?")
lon = input("Longitude ?")
c = conn.cursor()
d = new_db.cursor()  # will run the scripts from the memory so program runs from scratch everytime # note new_db is used

# Store the input co-ordinates in coords_1
coords_1 = (lat, lon)

loc_id = d.execute("select f.locationid from mfoodfacility f where f.status=?", (status,))
res = d.fetchall()
# Add a column to store the distance of the food truck locations from your input locations
addColumn = "ALTER TABLE mfoodfacility ADD COLUMN Distance REAL"
d.execute(addColumn)
# new_db.execute("COMMIT")

for location in res:
    r = (int(location[0])) # store the location id in int form and coverts the tuple to int
    # print(r) # have put here for debugging
    latitude_db = d.execute("select f.latitude from mfoodfacility f where  locationid=?",
                            (r,))
    lat1 = (d.fetchone()) # fetch the latitude value into a variable

    # print(float(lat1[0]))
    longitude_db = d.execute("select f.longitude from mfoodfacility f where  locationid=?",
                             (r,))
    lon2 = d.fetchone()
    coords_2 = (float(lat1[0]), float(lon2[0]))
    dist = GD(coords_1, coords_2).km
    d.execute("Update mfoodfacility set Distance=? where locationid =?", (dist, r,)) # add distance calculated to the temp table
    # print(coords_2)
    new_db.execute("COMMIT")
    #print("distance is", GD(coords_1, coords_2).km) --Uncomment to debug

# Below code checks , if the latitude and longitude are legit
# and executes the sql and store the records  returned in result variable
# fetchall fetches all the rows and gets stored in result variable
# second else condition : user inputs could be a made up value which does not fetch any results .
if (check_user_input(lat)) & (check_user_input(lon)):
    # crux of the logic, sql picks the top 5 closest location to the input location. and stores in result.
    # This can definitely be improved .Distance between two points uses a different formulae I have modified it
    # given the time to run the program .Can explain
    # c.execute("SELECT * FROM mfoodfacility f where f.Status=? "
    # "order by ABS(f.Latitude - (?)) + ABS(f.Longitude - (?)) ASC LIMIT 5", (status, lat, lon,))
    d.execute("SELECT * FROM mfoodfacility f where f.Status=? "
              "order by Distance ASC LIMIT 5", (status,))
    result = d.fetchall()
    if result:  # result could be None or tuple (record)
        for res in result:
            print(res)
    else:
        print("No result found for the location .Please check the latitudes and Longitudes")
else:
    print("Re=Run the program and Please enter valid inputs")
