#def calculate_rectangle_area(length, width):
    #area = length * width
    #return area

#length = float(input("Enter the length of the rectangle: "))
#width = float(input("Enter the width of the rectangle: "))

#area = calculate_rectangle_area(length, width)
#print("The area of the rectangle is:", area)












#def print_goa_best():
    #return "Goa best"

#for _ in range(10):
    #print(print_goa_best())





def calculate_rectangle_perimeter(a, b, c, d):
    perimeter = a + b + c + d
    return perimeter

a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))
d = float(input("Enter the length of the fourth side: "))

perimeter = calculate_rectangle_perimeter(a, b, c, d)
print("The perimeter of the rectangle is:", perimeter)