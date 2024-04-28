# სხვაობის დამრგვალების ფუნქცია
def subtract(x, y):
    return x - y

# ჯამის ფუნქცია
def add(x, y):
    return x + y

# ნამრავლის ფუნქცია
def multiply(x, y):
    return x * y

# გაყოფის ფუნქცია (შემდეგი პარამეტრი გამოიყენება შესაბამისი შეცდომების გასწორებაში)
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

# ფუნქციების გამოძახება და შემადგენლობა
print("Subtraction:", subtract(10, 5))
print("Addition:", add(3, 7))
print("Multiplication:", multiply(4, 6))
print("Division:", divide(8, 2))