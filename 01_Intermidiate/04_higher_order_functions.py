
from functools import reduce

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


### Closures

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))

### Built-in higher order functions
numbers = [2, 5, 10, 21,3, 30, 5, 25, 95, 1, 87]
# Map
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))  #[4, 10, 20, 42]
print(list(map(lambda number: number * 2, numbers)))  #[4, 10, 20, 42]

# Filter

def greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(greater_than_ten,numbers)))
print(list(filter(lambda number:number > 10,numbers)))

# Reduce  Opera con un valor y el acumulado

def sum_two_values(first_value,second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values,numbers))