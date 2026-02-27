information = input("input : ")
name = information.split(",")[0]
marks=[]
marks.append(int(information.split(",")[1]))
marks.append(int(information.split(",")[2]))
marks.append(int(information.split(",")[3]))

total= sum(marks)
percentage = (total/300)*100
##grade calculation
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
elif percentage<40:
    grade="F"
print("Name : ", name)
print("Total Marks : ", total)
print("Percentage : {} %".format(percentage))
print("Grade : ", grade)