# ======================================================================================
# Check exist in an array
# ======================================================================================
def check_variable_in_array(array, variable):
    if variable in array:
        return True
    else:
        return False

# Example usage
my_array = ["apple", "banana", "cherry"]
my_string = "banana"

result = check_variable_in_array(my_array, my_string)

if result:
    print(f"The string '{my_string}' exists in the array.")
else:
    print(f"The string '{my_string}' does not exist in the array.")