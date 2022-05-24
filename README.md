#pse
```

I used Python with sqllite to find the closest locations from Input locations. 

Program1 takes input from the user and finds the nearby locations from the input (latitudes and longitude).

Although a simple solution I later used the same logic to write another program program2 

(which did not take much time to run once program 1 was running)   to generat  API based on the input 

```

# Program1
## Requirements to Run it successfully 
Program needs latest python installed and need sqllite to run it  sucessfully .It needs data.db file in the project to find the databazse and run it successfully 
Program checks for basic invalid input entries 
Finds and lists  5 nearby  location  (from your input loctions) of  Approved sites


## Steps 
1.First the csv is imported as databases  to sqllite to generate a db file 
2.That file is used to connect using database connectivity in program
3.SQl script calculates all the records from the input location and sorts it by distance and displays the first 5 (to get the nearby locations)


# 2nd Program
## Requirements to Run it successfully 
Program needs latest python version (3.10)  installed and need sqllite and FLASK  to run with it  sucessfully .Can be run from terminal and will use default port 5100 on localhost to call the api 
Uses the first program and demostantrates the possbility of converting it to api (using the same logic)

I noticed on the sfgov website they already group by location . So I have taken a different approach and  calculated distance based on Latitude and Longitude .

## Steps 
Uses the first 3 steps of program 1 and uses FLASK , flask comes with built in webserver. This just shows how we can see results from api call  .

Once the code is running one needs to modify the querystring to see the reults 


# Why I chose Python . 


Given the timeframe.Wanted to keep it simple.I chose Python as  I knew that it has lots of libraries and I will not need to re-invent wheel. 
I chose sqllite with it as it will allow to keep the data separate and give me more power to manipulate data on the client , which mean less line of code.If new sites are approved it will autmatically be picked by my code.

# What would I have done different if given more time ?

Being a Security enthu I would  have done more checks and would have done more testing (right now I did use the recommended way as otulined on sqllite website ) 
Would have spent more time on sql to make it more accurate and would have given GUI to the user to enter or choose the location.
