first_input = input("Input : ")
number_1= first_input.split(",")[0]
number_2= first_input.split(",")[1]
operator= first_input.split(",")[2]
if operator == "+":
    Result = int(number_1) + int(number_2)
    print(f"Result : {Result}")

elif operator == "-":
    Result = int(number_1) - int(number_2)
    print(f"Result : {Result}")
elif operator == "*":
    Result = int(number_1) * int(number_2)
    print(f"Result : {Result}")
elif operator == "/":
    Result = int(number_1) / int(number_2)
    print(f"Result : {Result}")

if Result > 0:
    print("Result is positive") 
elif Result < 0:
    print("Result is negative")
else:
    print("Result is zero")