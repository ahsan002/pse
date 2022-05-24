

## Summary

For this excercise I have created two program files simpleprogram1 and program2

**simpleProgram1** uses  **Python with sqllite** to find the closest locations from Input locations. 

simpleProgram1 accepts  input from the user (via cmdline) and calculates the nearby locations from the input (latitudes and longitude).It then displays the result on the command line itself.

**Program2** uses same logic as *simpleprogram1*  but disaplays  the JSON format result on Web . It takes querystring parameters to display results.As the result can be called via an API we can exploit it further to display the results as we like (i.e on maps or on Web Interface ) 



## Program1 -simpleProgram1
## Requirements to Run simpleProgram1 successfully 
Program needs latest python installed and need sqllite to run it  successfully. It needs data.db file in the project to query  the data  
Program checks ( for some basic) invalid input entries (*input validation) 
Finds and lists  5 nearby  location  (from user  input loctions) of  **Approved** sites


## Steps (Algorithm)
1.First the csv is imported as database  to sqllite to generate a db file --*this step is done manually*
2.We then connect to the Database (data.db)
3.SQl script calculates closest location from the input values,  sorts it by distance and displays the first 5 (to get the nearby locations)


## 2nd Program program2
## Requirements to Run it successfully 
Program needs latest python version (3.10)  installed and need sqllite and FLASK  to run it  sucessfully .Can be run from terminal and will use default port 5100 on localhost to call the api 
Uses the first program and demostantrates the possbility of converting it to api (using the same logic)

I noticed on the sfgov website they already group by location . So I have taken a different approach and  calculated distance based on Latitude and Longitude .

## Steps 
**Program2** Uses the first 3 steps of program 1 and uses FLASK , flask comes with built in webserver. This program  just shows how we can see results from api call  .

Once the code is running one needs to modify the querystring to see the reults 

## Detailed Steps
```
Install Python on your macbook or windows 
run on cmd prompt (macbook)> pip install sqllite
run on cmd prompt (macbook) >pip install flask
create a directory and create project 
Open pycharm(or any other IDE) and import the project directory
pull project from the repo and run program1
```

## Checking  Program2
## Once the program is running goto  all locations to verify API results
```
http://127.0.0.1:5000/api/v1/resources/food/all
```

## goto below location and modify the Latitude and Longitude value to check the results
```
http://127.0.0.1:5000/api/v1/resources/food/all?Latitude=37.76&Longitude=-122.42730642251331

```

# Why I chose Python . 


Given the timeframe.I wanted to keep it simple.I chose Python as  I knew that it has lots of libraries and I will not need to re-invent a wheel creating unnecessary methods. 
I chose sqllite with it as it will allow to keep the data separate and give me more power to manipulate data on the client , which mean less line of code.If new food location  are added or approved in database it will automatically be picked by my code.

# What would I have done different if given more time ?

Would have spent more time on sql to make it more accurate and would have prepared an interface  for the user to enter or choose the location.Although the program demonstrates what was asked its not complete.Some more code  need to be added for API and I am sure we can break the program one way or another. 
Being a Security enthusiat I would  have done more checks and would have done more testing.

