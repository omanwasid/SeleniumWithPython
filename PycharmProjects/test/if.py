"""
aa=['apple','Banana','Orange','Coconut']
for fruit in aa:
    print ('The current fruit: %s' % fruit)
"""
"""
for num in range(1,10):
    print('I am at:%d' % num)
    if num > 5:
     print('I am Below 5')
    else:
     print('I am above 5')
"""
"""
my_nums =[100,200,300,400]
for ak in my_nums:
    result=ak/2
    print(' The result is:%d'%result)
"""
"""
counter=5
while counter<=10:
    counter+=1
    print('The current counter is:%d'%counter)
    if counter==8:
        break
"""
"""
my_classes=['biology','chemistry','english','physics','mathematics']
for c in my_classes:
    print(c)
    if c== ('physics'):
        print( 'I got it')
        break
"""
"""
my_classes=['biology','chemistry','english','physics','mathematics']
for c in my_classes:
    print(c)
    if c!= ('physics'):
        print('I got it')
        continue
"""
"""
prices = [{'iPhone': '200'}, {'samsung': '80'}, {'nokia': '100'}, {'ericsson': '120'}]
for i in prices:
    print(i)
    key = list(i.keys())[0]
    print(key)
    if key == 'nokia':
        prices = i['nokia']
        print('The price of nokia is:%s' % prices)
        break

"""
"""
def adder(a, b):
    total = a + b
    print(total)


adder(3, 1)


def state(user_state):
    approved_state = ["CA", "DK", "NOG", "FIN", "SWE"]
    if user_state in approved_state:
        return 'true'
    else:
        return 'false'


print(state('FIN'))
"""
"""
def state(user_state):
    approved_state=["CA","DK","NOG","FIN","SWE"]

    if user_state in approved_state:
        print('true')
    else:
        print('false')
state("SWE")

"""
""" 
def get_full_name(first_name, l_name):
    if not l_name:
        l_name == ""


full_name = first_name + " " + last_name
get_full_name('oman', 'wasid')
print(full_name)

full_name = get_full_name('AK', 'PK')
print(full_name)
full_name = get_full_name('RAJ', 'MIA')
print(full_name)
def my_function(*kids):


    def kids(args):
        pass


print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def calculare_area(width =0, height=0):
    area=width*height
    return area
calculare_area(4,3)
print calculare_area)
"""
"""

import math
x=math.sin(30)
y=math.sqrt(81)
print(x)
print(y)
from math import sin,sqrt
x=sin(30)
y= sqrt(9)
print(x)
print(y)
from datetime import datetime
print(datetime.now())

def divide(x,y):
    try:
print(f'{x}/{y} is {x/y}')
        except ZeroDivisionError as e:
print(e)
"""

def retry_with_counter_until_status_is_success_2(max_retry=10, sleep_time=3):

    is_success = False
    counter = 0
    while counter < max_retry:
        counter += 1
        print("Retry no: {}".format(counter))
        is_success = is_status_success()

        print("The succcess status is: {}".format(is_success))

        if is_success:
            print("The process is success.")
            break
        else:
            time.sleep(sleep_time)

    else:
        raise Exception("The process did not succeed after trying for {} seconds.".format(max_retry * sleep_time))


retry_with_counter_until_status_is_success(max_retry=2, sleep_time=1)