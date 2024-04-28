print ("ET0735 (DecOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    get_user_input()
    print("Average temperature ="+ calc_average_temperature())
    print("Minimum temperature="+ find_min_max(mintemp))
    print("Maximum temperature="+ find_min_max(maxtemp))

def get_user_input():
    numbers = input("numbers =")
    numbers = numbers.split (",")
    numbers = [int(num.strip()) for num in numbers]
    return [numbers]

def calc_average_temperature(numbers):
    average_temperature=sum(numbers)/len(numbers)
    return average_temperature
   
def find_min_max():
    x=0
    for x in get_user_input():
        prevtemp=0
        newtemp=get_user_input[x]
        if newtemp>prevtemp:
            maxtemp=get_user_input[x]
        if newtemp<prevtemp:
            mintemp=get_user_input[x]
        prevtemp=get_user_input[x]
    x=x+1
    return mintemp and maxtemp
mintemp, maxtemp = find_min_max()

def sort_temperature():
    print("sort_temperature")
def cale_median_temperature():
    print("cale_median_temperature")

display_main_menu()