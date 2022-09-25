# actual = 1023.453
#bonus = 20
# bonus = (20/100) * actual
# gross = actual + bonus 
# print(("%.2f"%gross))

def gross_salary(actual,bonus):
    bonus /= 100
    return "%.2f" %(bonus*actual + actual)

print(gross_salary(100,20))