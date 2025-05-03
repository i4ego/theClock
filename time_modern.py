import datetime, nums
def getTime():
    now = datetime.datetime.now()


    output_text = str()

    for num in str(now.hour):
        output_text += num

    output_text += ":"

    for num in str(now.minute):
        output_text += num

    output_list = list()

    for number in output_text:
        output_list.append(nums.switch[number])

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
    return [first_ln, second_ln, third_ln, fourth_ln, fifth_ln, sixth_ln]