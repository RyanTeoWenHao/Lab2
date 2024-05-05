print ("ET0735 (DecOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("Enter some wnumbers separated by commas (e.g. 5, 67, 32)")
    user_input = get_user_input()
    average_temperature = calc_average_temperature(user_input)
    print("Average temperature =", average_temperature)
    min_temp, max_temp = find_min_max(user_input)
    sort_temp= sort_temperature(user_input)
    median_temp=calc_median_temperature(sort_temp)
    print("Minimum temperature =", min_temp)
    print("Maximum temperature =", max_temp)
    print("The list of temperature in ascending order :", sort_temp)
    print("The median is :", median_temp)
    
def get_user_input():
    numbers = input("numbers =")
    numbers = numbers.split(",")
    numbers = [int(num.strip()) for num in numbers]
    return numbers

def calc_average_temperature(numbers):
    total_sum = sum(numbers)
    count = len(numbers)
    average_temperature = total_sum / count
    return average_temperature

def find_min_max(numbers):
    min_temp = min(numbers)
    max_temp = max(numbers)
    return min_temp, max_temp

def sort_temperature(numbers):
    sort_temp=sorted(numbers)
    return sort_temp

def calc_median_temperature(sorted_temp):
    middle_index = len(sorted_temp) // 2
    if len(sorted_temp) % 2 == 1:
        median_temp = sorted_temp[middle_index]
    else:
        median_temp = (sorted_temp[middle_index - 1] + sorted_temp[middle_index]) / 2
    
    return median_temp


display_main_menu()