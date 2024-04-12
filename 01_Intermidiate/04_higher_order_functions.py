
def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(first_value,second_value):
    return sum_one(first_value + second_value)

print(sum_two_values_and_one(5,2))



def sum_two_values_and_add(first_value,second_value, function):
    return function(first_value + second_value)

print(sum_two_values_and_add(5,2, sum_one))
print(sum_two_values_and_add(5,2, sum_five))


# Closures

