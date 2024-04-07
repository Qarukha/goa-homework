#correct_password = "თქვენი_სწორი_პაროლი"

#while True:
    #password = input("გთხოვთ, შეიყვანეთ პაროლი: ")
    #if password == correct_password:
        #print("პაროლი სწორია. წამების დროა!")
        #break
   #else:
        #print("პაროლი არასწორია. გთხოვთ, სცადოთ თავიდან.")

number = int(input("შეიყვანეთ რიცხვი: "))

if number <= 0:
    print("შეცდომა: რიცხვი უნდა იყოს 1-ზე მეტი.")
else:
    for i in range(1, number + 1):
        print(i)



