# function to input a valid and non negative integer
def input_int(message):
    while True:
        try:
            num = int(input(message))
        except ValueError:
            print("Please enter a valid integer!")
            continue
        if num < 0:
            print("Please enter a non negative integer!")
            continue
        else:
            break
    return num

# Function check existence string in list
def check_existence_string_in_list(list, string):
    for i in list:
        if i == string:
            return True
    return False

# Function to check input name vertices in graph: Name vertices must be string and not duplicate
def check_input_name_vertices_in_graph(list, message):
    name = input(message)
    while check_existence_string_in_list(list, name):
        print("Name vertices must be string and not duplicate")
        name = input(message)
    return name