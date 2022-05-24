# Import sqllite to use sql with python
import sqlite3

# Establish dataBase connection and store it in connection parameter
conn = sqlite3.connect('data.db')


# Create a function to check the input parameter from the user -> Input Validation
# We want to ensure we get the right parameters
# check_user_input checks if a numerical value is entered by the use returns true if it finds a number
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

# Below code checks , if the latitude and longitude are legit
# and executes the sql and store the values returned in result variable
# fetchall fetches all the rows and gets stored in result variable
# it could be user inputs a made up value which does not fetch any results .This is just covering
# the basis that if check_user_input has missed validation it gets picked within the if else statement
if (check_user_input(lat)) & (check_user_input(lon)):
    # crux of the logic, sql picks the top 5 closest location to the input location. and stores in result.
    # This can definitely be improved .Distance between two points uses a different formulae I have modified it
    # given the time to run the program .Can explain
    c.execute("SELECT * FROM mfoodfacility f where f.Status=? "
              "order by ABS(f.Latitude - (?)) + ABS(f.Longitude - (?)) ASC LIMIT 5", (status, lat, lon,))
    result = c.fetchall()
    if result:  # result could be None or tuple (record)
        for res in result:
            print(res)
    else:
        print("No result found for the location .Please check the latitudes and Longitudes")
else:
    print("Re=Run the program and Please enter valid inputs")
