# 1: Convert nis to dollars
# rate это курс
nis = float(input("Enter amount in nis>>> "))
rate = float(input("Enter dollar exchange rate>>> "))
dollars  = nis / rate
# print("You will get dollars amount", round(dollars, 2), "USD")
# round(..., 2) — округляет до двух знаков после запятой, как принято в финансах
print(f"you will get dollars amount = {dollars:.2f} USD")

# 2: Subtraction of two numbers вычетание
number1 = float(input("Enter the first number>>> "))
number2 = float(input("Enter the second number>>> "))
result = number1 - number2
print("The result of subtraction is:", result)

# Advanced 3: Salary calculation with tax
hours = float(input("enter working hours>>>"))
wage = float(input("Enter hourly wage>>>"))
tax_percent = float(input("Enter tax percent>>> "))

# gross_salary размер заработной платы до вычета всех налогов. брутто
# net_salary сумма, которую получает работник после вычета налогов
gross_salary = hours * wage
tax_amount = gross_salary * tax_percent / 100
net_salary = gross_salary - tax_amount
# print("Your net salary after tax is:", round(net_salary, 2), "nis")
print(f"Your net salary after tax is: = {net_salary:.2f} nis")

# Extension: Add bonus
bonus_percent = float(input("Enter bonus percent>>> "))
bonus = gross_salary * bonus_percent / 100
net_salary_with_bonus = gross_salary + bonus - tax_amount

# print("Your net salary with bonus is:", round(net_salary_with_bonus, 2), "nis")
print(f"Your net salary with bonus is: = {net_salary_with_bonus:.2f} nis")

