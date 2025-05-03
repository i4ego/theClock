import datetime, nums
import time as cat

now = datetime.datetime.now()
switch = {"1" : nums.one,
          "2" : nums.two,
          "3" : nums.three, 
          "4" : nums.four,
          "5" : nums.five, 
          "6" : nums.six, 
          "7" : nums.seven, 
          "8" : nums.eight, 
          "9" : nums.nine, 
          "0" : nums.zero, 
          ":" : nums.colon
         }

output_text = str()

for num in str(now.hour):
    output_text += num

output_text += ":"

for num in str(now.minute):
    output_text += num

output_list = list()

for number in output_text:
    output_list.append(switch[number])

first_ln = str()
second_ln = str()
third_ln = str()
fourth_ln = str()
fifth_ln = str()
sixth_ln = str()

for i in output_list:
    first_ln += i.split("\n")[0]
    second_ln += i.split("\n")[1]
    third_ln += i.split("\n")[2]
    fourth_ln += i.split("\n")[3]
    fifth_ln += i.split("\n")[4]
    sixth_ln += i.split("\n")[5]

print(first_ln)
print(second_ln)
print(third_ln)
print(fourth_ln)
print(fifth_ln)
print(sixth_ln)