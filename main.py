"""
this program calculates employees productivity bonuses
"""
#constants
BONUS_1 = 50.00
BONUS_2 = 75.00
BONUS_3 = 100.00
BONUS_4 = 200.00

#variables
employee_name = " "
shift_number = 0
shift_number_productivity = 0
productivity_score = 0
productivity_bonus = 0

#input statements
employee_name = input("Enter employee's name: ")
shift_number = int(input("Enter number of shifts: "))
shift_number_productivity = int(input("Enter number of transactions: "))
td_value = float(input("Enter Transaction Dollar Value: "))
productivity_score = (td_value/shift_number_productivity)/shift_number
#calculations


if productivity_score <= 30:
  productivity_bonus = BONUS_1
if productivity_score > 30 and productivity_score <= 69:
  productivity_bonus = BONUS_2
if productivity_score > 69 and productivity_score <= 99:
  productivity_bonus = BONUS_3
if productivity_score > 99:
  productivity_bonus = BONUS_4


#output statements
print("Employee Name: ", employee_name)
print("Productivity Bonus: $", productivity_bonus)

