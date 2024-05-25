# სია, რომელშიც დაამატებთ ყველა მნიშვნელობას სიის ბოლოში
my_list = [1, 2, 3, 4, 5]
new_value = 6
my_list.append(new_value)

# შემდეგ ამოშლით შემდეგ გაიგებთ ამ სიაში არსებული მნიშვნელობების რაოდენობას
count_before_removal = len(my_list)
# წაშლა
removed_value = my_list.pop()

# შემდეგ ჩაამატებთ ახალ მნიშვნელობას მეორე ინდექსზე
new_value_2 = 7
my_list.insert(1, new_value_2)

# გამოიტანეთ სიის რაოდენობა და არსებული მნიშვნელობები
count_after_operations = len(my_list)
print("სიაში არსებული მნიშვნელობები:", my_list)
print("მნიშვნელობების რაოდენობა:", count_after_operations)