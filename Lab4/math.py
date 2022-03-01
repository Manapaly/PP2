import math 
# Write a Python program to convert degree to radian.
degree = float(input("Input degree: "))
radian = degree*(math.pi/180)
print('Output radian: ',round(radian,6))

print('-'*70)
# Write a Python program to calculate the area of a trapezoid.
height = float(input('Height: '))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area = ((base1 + base2)/2)*height
print("Expected Output: ", area)

print('-'*70)
# Write a Python program to calculate the area of regular polygon.
side_num = float(input('Input number of sides: '))
lenght_of_a_side = float(input('Input the length of a side: '))
area_of_the_polygon = (side_num * lenght_of_a_side**2)/(4*math.tan(math.pi/side_num))
print('The area of the polygon is: ', round(area_of_the_polygon,2))

print('-'*70)
# Write a Python program to calculate the area of a parallelogram.
base_len = float(input('Length of base: '))
parall_height = float(input("Height of parallelogram: "))
print('Output: ', base_len*parall_height)
