#def check_number(number):
    #if number > 0:
        #print("რიცხვი დადებითია")
   #elif number < 0:
        #print("რიცხვი უარყოფითია")
    #else:
        #print("რიცხვი ნულია")

# რიცხვის შემოწმება
#number = float(input("შეიტანეთ რიცხვი: "))

# შედეგის ბეჭდვა
#check_number(number)






def check_age_category(age):
    if age < 13:
        print("ბავშვი ხარ")
    elif age >= 13 and age <= 19:
        print("შენ ხარ მოზარდი")
    else:
        print("სრულწლოვანი ხარ")

# ასაკის შემოწმება
age = int(input("შეიტანეთ თქვენი ასაკი: "))

# შედეგის ბეჭდვა
check_age_category(age)