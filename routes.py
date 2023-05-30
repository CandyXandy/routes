################################################################
#################### routes.py #################################
################################################################
#   Developed by: A. Robertson                                 #
#    Date: 2/05/2022                                           #
#    Develoeped for the mayor of CodeTown.                     #
#    This program reads the data from the routes.txt file      #
#    and sorts the data by happy ratio.                        #
#    Asks the user for the amount of extra busses available    #
#    and displays the routes that would benefit the most from  #
#    the extra busses.                                         #
################################################################
#   This program is designed to be run on Python 3 and higher  #
################################################################


import os  # imports the os module for handling file reading
import sys  # imports the sys module for handling program termination


def read_route_data(file_name):
    ''' Reads the route data from the file name given.

        Key Arguments:
                file_name - The name of the .txt file needing to be read

        This function reads the data from the file and stores each line in
        a new dictionary. It then stores the dictionary in a list.
        Each dictionary contains the keys 'route_number" and "happy_ratio" if
        the data read from the .txt file is valid.
        Each line in routes.txt must contain a route number and a happy ratio
        separated by a comma. Any ratio with more than 2 decimal points is
        rounded down to 2 decimal points. If a route number appears twice an
        error is also thrown. The file_name must be routes.txt.
        Any errors in this function will result in the program terminating.
        '''
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


def sort_route_data(list_of_dict):
    ''' Sorts the route data by happy ratio.

            Key Arguments:
                    list_of_dict - A list of dictionaries containing the route number and happy ratio

        This function sorts the route data by happy ratio.
        It then stores the sorted list in a new list.
        The list is sorted in ascending order, but happy_ratio's with values
        of 0 are sorted to the bottom.
        '''
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


def front_end():
    ''' Displays the front end of the program.

        This function asks the user how many routes need
        an extra bus. This value is assigned as 'n'.
        It then displays the top n route numbers as per
        sorted_route_data, and indicates to the user that
        those route numbers would benefit most from an
        extra bus.
        '''
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


def main():
    ''' This function calls the other functions in the program.
        '''
    global route_data
    global sorted_route_data
    route_data = read_route_data('routes.txt')
    sort_route_data(route_data)
    front_end()


if __name__ == '__main__':
    main()
