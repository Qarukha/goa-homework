my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# ლუწი რიცხვები
even_numbers = [num for num in my_list if num % 2 == 0]
print("ლუწი რიცხვები:", even_numbers)

# 5ის ჯერადი რიცხვები
divisible_by_5 = [num for num in my_list if num % 5 == 0]
print("5ის ჯერადი რიცხვები:", divisible_by_5)

# რიცხვთა ჯამი
sum_of_numbers = sum(my_list)
print("რიცხვთა ჯამი:", sum_of_numbers)

# ლუწ რიცხვთა ჯამი
sum_of_even_numbers = sum(num for num in my_list if num % 2 == 0)
print("ლუწ რიცხვთა ჯამი:", sum_of_even_numbers)

# ახალი სია მხოლოდ კენტი რიცხვებით
new_list_odd = [num for num in my_list if num % 2 != 0]
print("ახალი სია მხოლოდ კენტი რიცხვებით:", new_list_odd)

# ახალი სია რომელშიც იქნება 3ის და 5ის ჯერადი რიცხვები
new_list_divisible_by_3_and_5 = [num for num in my_list if num % 3 == 0 and num % 5 == 0]
print("ახალი სია რომელშიც იქნება 3ის და 5ის ჯერადი რიცხვები:", new_list_divisible_by_3_and_5)