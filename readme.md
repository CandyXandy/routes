# Routes
## A. Robertson.
## 2/5/2022
## Preface:
Routes.py is a program developed for the mayor of CodeTown for the purpose of aiding the decision making process of which routes require
an extra bus. The program is designed to be run on a personal computer and reads data from a text file called 'Routes.txt' which contains the route number as well as a ratio of happy to unhappy customers.
This program iterates on data collected by BusStops.py.

## Contents
- Pre-requesites
- How to run
- How to use it
- How it works

## Pre-requisites


To run this program you will need a computer that has Python3 installed.<br>
You can find python3 [here](http://python.org/downloads/).
Make sure you install the correct version for your operating system.

## How to run

In your terminal, navigate to the directory where you have Routes saved.  
Then, type python3 routes.py into the terminal. 
The program should begin to run.

## How to use it
This program is quite concise and easy to use.  
The program will display a line of text to your screen.

> How many routes can have an extra bus?

This is the only question you will be asked by the program.
You must enter a non-negative integer or you will be prompted to enter a valid integer.

>Invalid input. Please enter a positive integer.

Or, if you input a number greater than the amount of routes, another error message will be displayed.

>Invalid input. Please enter a number less than or equal to the amount of routes.

Upon succesful entry, the program will display the number of routes that would benefit most from an extra bus equal to the number you entered. The routes displayed will be in the ascending order of ratio of happy to unhappy customers that are not 0.
Routes that have a ratio of 0 will only be displayed if you have leftover busses to use as they would benefit least. 

For example:

>You should add busses for the following routes:  
&emsp;&emsp;412  
&emsp;&emsp;991  
&emsp;&emsp;988  
&emsp;&emsp;773    

That's it! Nice and simple.

The real crux of using this program is the fact that the file the program reads from, the 'Routes.txt' file; must be in the correct format.  
The file must contain the route number as well as the ratio of happy to unhappy customers, seperated by a comma.  
The route number must come first, followed by a comma with no whitespaces trailing or leading. Following the comma a ratio must come next, followed by a newline.    
Failure to folow this format will result in an error message, and the program will terminate upon your next press of 'Enter' or 'Return'.
You will also run into this error if you have multiple lines with the same route number.

>The file is not in the correct format.  
Please ensure each line has the route number followed by a comma and then followed by the happy ratio.
Please also ensure all route numbers are positive integers, and that no route numbers are repeated.
Press enter to exit.

The program terminates so that you may navigate to your routes.txt file and edit it into the correct format.

### Just to be clear, the program will not read from a file that is not in the correct format.
### Please edit your file into the correct format and then run the program again.  
### The correct format is as follows:  
### Route number, happy ratio, newline.

    Route Number,Happy Ratio
    Route Number,Happy Ratio
    799,1.63
    991,6.50


## How it works

### Data
The program reads from the file 'Routes.txt' which contains the route number as well as the ratio of happy to unhappy customers.
This is the data that the program will use to determine which routes benefit from an extra bus.
This data is read into the program and stored in a list of dictionaries.
This is handled by the function 'read_route_data'.

This function takes a key argument of 'file_name' which is the name of the file to read from.

```python
def read_route_data(file_name):
    global route_data
    route_data = []

    try:
        if file_name != 'routes.txt':  # Checks if the file name is correct
            raise ValueError

    except ValueError:  # If the file name is incorrect, the program terminates
        print('The file name must be routes.txt')
        input('Press enter to exit.')
        sys.exit()

    try:
        with open(file_name, 'r') as file:
            for line in file:
                if ',' not in line:  # Checks if there is a comma in the line
                    raise ValueError

                line = line.strip()
                line = line.split(',')
                if len(line) != 2:  # Checks if there are 2 items in the line
                    raise ValueError

                route_number = int(line[0])
                list_of_values = [value for elem in route_data
                                  for value in elem.values()]
                if route_number in list_of_values:  # Checks if the route number is already in the list
                    raise ValueError
                if route_number < 1:
                    raise ValueError

                # Converts the happy ratio to a float
                happy_ratio = float(line[1])
                if happy_ratio < 0:
                    raise ValueError
                if happy_ratio > 100:
                    raise ValueError
                # formats the happy ratio to 2 decimal points
                happy_ratio = f'{happy_ratio:.{2}f}'

                route_data.append(  # Appends the route number and happy ratio to the list
                    {'route_number': route_number, 'happy_ratio': happy_ratio})

    except FileNotFoundError:  # If the file is not found
        print('The file could not be found.')
        input('Press enter to exit.')
        sys.exit()

    except ValueError:  # If the data in the file is not valid
        print('The file is not in the correct format.')
        print('Please ensure each line has the route number followed by a comma and then followed by the happy ratio.')
        print('Please also ensure all route numbers are positive integers, and that no route numbers are repeated. ')
        input('Press enter to exit.')
        sys.exit()

    return route_data
```

As the largest function in the program, we'll break it down into snippets.  
To begin with, the function assigns the variable 'route_data' to an empty list and makes it global so other functions can access it.

```python
    global route_data
    route_data = []
```

It then checks the file name.  If the file name is not 'routes.txt', the program terminates.

```python
    try:
        if file_name != 'routes.txt':  # Checks if the file name is correct
            raise ValueError

    except ValueError:  # If the file name is incorrect, the program terminates
        print('The file name must be routes.txt')
        input('Press enter to exit.')
        sys.exit()
```

It then opens the file.  If the file is not found, the program terminates.

```python
    try:
        with open(file_name, 'r') as file:
            for line in file:
```

It then checks if there is a comma in the line.  If there is not, the program terminates.

```python
                if ',' not in line:  # Checks if there is a comma in the line
                    raise ValueError
```

It then strips the line of whitespaces, and splits the line into two on the ','.  If there are not two items in the line, the program terminates.

```python
                line = line.strip()
                line = line.split(',')
                if len(line) != 2:  # Checks if there are 2 items in the line
                    raise ValueError
```

The program then converts the first of the split lines into an integer, terminating the program if the conversion fails.
We also check if the route number is already in the list of dictionaries.  If it is, or the route number is less than 1, the program terminates.

```python
route_number = int(line[0])
                list_of_values = [value for elem in route_data
                                  for value in elem.values()]
                if route_number in list_of_values:  # Checks if the route number is already in the list
                    raise ValueError
                if route_number < 1:
                    raise ValueError
```

We then convert the second of the split lines into a float, terminating the program if the conversion fails, or if the value is below 0 or above 100, as those ratios should be impossible given that the max number of customers per bus is 47. The program also formats the ratio to 2 decimal places.

```python
                # Converts the happy ratio to a float
                happy_ratio = float(line[1])
                if happy_ratio < 0:
                    raise ValueError
                if happy_ratio > 100:
                    raise ValueError
                # formats the happy ratio to 2 decimal points
                happy_ratio = f'{happy_ratio:.{2}f}'
```

It then appends the data obtained to the list of dictionaries and returns the list.


```python
route_data.append(  # Appends the route number and happy ratio to the list
                    {'route_number': route_number, 'happy_ratio': happy_ratio})
return route_data
```

Most of the errors caught by the program will be handled as ValueErrors. The program will terminate if the file is not in the correct format, or if the route number is already in the list of dictionaries.

```python
  except ValueError:  # If the data in the file is not valid
        print('The file is not in the correct format.')
        print('Please ensure each line has the route number followed by a comma and then followed by the happy ratio.')
        print('Please also ensure all route numbers are positive integers, and that no route numbers are repeated. ')
        input('Press enter to exit.')
        sys.exit()

```

### Sorting
Routes.py sorts the data obtained by the function 'read_route_data'. It sorts the data by the lowest to highest ratio, but it leaves the route numbers with a ratio of '0' at the end of the list as they are bus routes with no unhappy customers and would benefit least from an extra bus.
This sorting is handled by the sort_route_data function.
This function takes a key argument of 'list_of_dict' which is the list of dictionaries obtained from the function 'read_route_data'.

```python
def sort_route_data(list_of_dict):

    global sorted_route_data
    sorted_route_data = []

    for dictionary in list_of_dict:
        happy_ratio = dictionary['happy_ratio']
        if happy_ratio != '0.00':  # If the happy ratio is not 0, it is added to the sorted list
            sorted_route_data.append(dictionary)
            # Sorts the list by happy ratio
            sorted_route_data.sort(key=lambda x: x['happy_ratio'])

    for dictionary in list_of_dict:
        happy_ratio = dictionary['happy_ratio']
        if happy_ratio == '0.00':  # If the happy ratio is 0, it is added to the end of the sorted list
            sorted_route_data.append(dictionary)

    return sorted_route_data
```

This isn't a particularly complex function, but take note of the if statements.  The first if statement checks if the happy ratio is not 0.  If it is, the happy ratio is added to the sorted list.  The second if statement checks if the happy ratio is 0.  If it is, the happy ratio is added to the end of the sorted list.
This function also makes use of an anonymoys function to sort the list by happy ratio.  

### Front-End
The front-end of the program is handled by the function 'front_end'.
Again, not complex but arguably the most important function in the program. After all, what functionality would we have without a front end?
The program takes an input from the user, assigning the input to the variable 'n'.
It then checks if the input is an integer. If it is not, the program asks for input again.
It then checks if the input is less than 1. If it is, the program asks for input again.
It also asks for input again if the input is greater than the number of routes.

```python
def front_end():

    while True:
        try:
            n = int(input('How many routes can have an extra bus? '))
            if n < 0:
                raise ValueError
            # Checks if the number of routes is less than the number of routes in the list
            if n > len(sorted_route_data):
                raise TypeError

            print('You should add busses for the following routes: ')

            for i in range(n):   # Displays the top n route numbers
                # Gets the route number from the sorted list
                route_number = sorted_route_data[i]['route_number']
                print(route_number)
            break

        except ValueError:   # If the input is not a positive integer
            print('Invalid input. Please enter a positive integer.')
            continue

        except TypeError:   # If the input is greater than the length of the sorted list
            print(
                'Invalid input. Please enter an integer less than or equal to the number of routes.')
            continue
```

The program displays no more and no less than 'n' upon successful input.

### Main
The main function of the program is the function 'main'.
Everything is brought together here, and the program is run.

```python
def main():

    global route_data
    global sorted_route_data
    route_data = read_route_data('routes.txt')
    sort_route_data(route_data)
    front_end()
```

Thank you for reading!   :)   
A. Robertson.