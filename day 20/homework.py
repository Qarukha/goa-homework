#for i in range(1, 101):
    #if i % 5 == 0 and i % 3 == 0:
        #print(i)




        #names = []

#while True:
    ##last_name = input("შეიყვანეთ გვარი (გასაგებია ცარიელი შეტყობინებაც): ")

    #if not first_name and not last_name:
       # break

    #names.append((first_name, last_name))

#print("შეტყობინებები დამატებულია სიაში:")
#for name in names:
    #print(f"{name[0]} {name[1]}")





    # რიცხვის შეტანა მომხმარებლისგან
#number = int(input("შეიყვანეთ რიცხვი: "))

# რიცხვების ჩათვლა და დაბეჭდვა
#total = 0
#count = 0
#for i in range(1, number + 1):
    #print(i)
    #total += i
    #count += 1

# ჯამი და საშუალო არითმეტიკული
#average = total / count
#print("რიცხვების ჯამი:", total)
#print("საშუალო არითმეტიკული:", average)







# ცარიელი სია ლუწი რიცხვებით
#even_numbers = []

# ლუწი რიცხვების დამატება სიაში
#for i in range(2, 51, 2):
    #even_numbers.append(i)

# სიის დაბეჭდვა
#print(even_numbers)






# რიცხვის შემოწმება
#number = int(input("შეიყვანეთ რიცხვი: "))

# მარტიცის შემოწმება
#if number > 1:
    #for i in range(2, number):
        #if (number % i) == 0:
            #print("თქვენი რიცხვი არ არის მარტივი")
           # break
   # else:
   #     print("თქვენი რიცხვი მარტივია")
#else:
    #print("თქვენი რიცხვი არ არის მარტივი")




#a = int(input("შეიყვანეთ a: "))
#b = int(input("შეიყვანეთ b: "))

# ცარიელი სია
#numbers = []

# რიცხვების დამატება ახალ სიაში
#for i in range(a, b):
   # numbers.append(i)

# შედეგის დაბეჭდვა
#print("შედეგი:", numbers)








my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# ცარიელი სია
reversed_list = []

# სიის შეტრიალება
for i in range(len(my_list)-1, -1, -1):
    reversed_list.append(my_list[i])

# დაბეჭდვა
print(reversed_list)