

## Summary

For this excercise I have created two program files simpleprogram1 and program2

**simpleProgram1** uses  **Python with sqllite** to find the closest locations from Input locations. 

simpleProgram1 accepts  input from the user (via cmdline) and calculates the nearby locations from the input (latitudes and longitude).It then displays the result on the command line itself.

**Program2**  adds flask library and  displays  the JSON results on a web browser. It takes querystring parameters to display results.As the result can be called via an API we can exploit it further to display the results as we like (i.e on maps or on Web Interface ) 

**simpleProgram3** I did this as I was not too happy on how I was calculating the distances of food trucks from the input locations.I have left the other 2 programs in repo to discuss on my approach and how I ended with third program. If I have to choose one program to demo I will be choosing simpleprogram3.



## Program1 -simpleProgram1
## Prerequisites 
Program needs latest python version (3.10)  installed and need sqllite to run it  successfully. It needs data.db file in the project to query  the data  


  ## Detailed Steps
  ```
Install Python on your macbook or windows 
run on cmd prompt (macbook)> pip install sqllite
run on cmd prompt (macbook) >pip install flask
create a directory and create project 
Open pycharm(or any other IDE) and import the project directory
pull project from the repo and run simpleprogram1
```


## Verifying simpleprogram1

```
Run simpleprogram1 
Enter the Latitude and Longitude value as input (and when prompted ,choose correct working latitudes to see the program working)
Result of 5 closest locations  will be displayed on cmd line 
```


## Program2 - program2
  ## Prerequisites
  Program needs latest python version (3.10)  installed and need sqllite and FLASK  to run it  sucessfully .Can be run from terminal and will use default port 5000 on    localhost to call the api 
  

  Note: *I noticed on the sfgov website they already group by location . So I have taken a different approach and  calculated distance based on Latitude and Longitude* 


## Detailed Steps
  ```
Install Python on your macbook or windows 
run on cmd prompt (macbook)> pip install sqllite
run on cmd prompt (macbook) >pip install flask
create a directory and create project 
Open pycharm(or any other IDE) and import the project directory
pull project from the repo and run program2
```

## Verifying Program2
## Once the program is running goto  all locations to verify API results
```
http://127.0.0.1:5000/api/v1/resources/food/all
```

## Goto below location and modify the Latitude and Longitude value to check the results
```
http://127.0.0.1:5000/api/v1/resources/food/all?Latitude=37.76&Longitude=-122.42730642251331

```

### Program 3 -- Simple Program3
I found some more time  on weekend to fix the core logic on how the distance was getting calculated and this program gives a very precise output. This program uses Geopy python libraries.Logic involves creating a temporary database and appending  a new distance column to it . I then use this column to store the distance (calculated from the input location) and then sort the location based on the distances ,and then display the top 5 clostest locations.I have left the the other 2 programs to discuss my approach and how I ended up coding simpleprogram3.

## Why I chose Python . 


Given the timeframe.I wanted to keep it simple.I chose Python as  I knew that it has lots of libraries and I will not need to re-invent a wheel creating unnecessary methods. 
I chose sqllite with it as it will allow to keep the data separate and give me more power to manipulate data on the client , which mean less line of code.If new food location  are added or approved in database it will automatically be picked by my code.

## What would I have done different if given more time ?

I would have designed an interface  for the user to enter or choose the location.Although the program demonstrates what was asked its not complete.Some more code can  added for API checks and I am sure we can break the program one way or another. 
Being a Security enthusiat I would  have done incorporated more tests (besides the input validation and sql injection checks ) and would have done more testing.

