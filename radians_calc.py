#Calculator to convert between degrees and radians
#Lori Ramey, August 2022

from cmath import pi

input_unit = input("Please enter either 'degrees' or 'radians' and hit Enter:\n")
print(f"You entered {input_unit}")
input_value = input("Please enter the value you would like to convert and hit Enter:\n")
input_value = int(float(input_value))
print(f"You entered {input_value}")

result = 0

#function to convert between rad and deg
def convert(input_unit, input_value):
    
    if input_unit == "degrees":
       result  = input_value * pi / 180
       print(str(round(result,2)) + " radians")
    else: 
       result = input_value * 180 / pi
       print(str(round(result,2)) + " degrees")

convert(input_unit, input_value)