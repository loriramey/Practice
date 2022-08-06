#Calculator to convert between degrees and radians in angle measurements
#Lori Ramey, August 2022

from cmath import pi

input_unit = "radians"
input_value = 2*pi/3
result = 0

#function to convert between rad and deg
def convert(input_unit, input_value):
    
    if input_unit == "degrees":
       result  = input_value * pi / 180
       print(str(rount(result,2)) + " radians")
    else: 
       result = input_value * 180 / pi
       print(str(round(result,2)) + " degrees")

convert(input_unit, input_value)