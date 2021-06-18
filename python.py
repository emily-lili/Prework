# Question 1
def hello_name(user_name):
    print('hello_' + user_name)

hello_name('USERNAME')
    
# Question 2
def show_odd():
    numbers = range(1,100)
    for n in numbers:
        if n % 2 != 0:
            print(n)

show_odd()

# Question 3
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))

# Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            return False
        return True
    return False

print(is_leap_year(2000))

year = 2022
print(is_leap_year(year))

# Question 5
def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
    print(status)
    
is_consecutive([2,3,4,5,6,7])
is_consecutive([1,2,4,5])