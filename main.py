def calculate_sum(number):
    d_sum = 0
    while number > 0:
        d_sum = d_sum + number%10
        number = number // 10
    return d_sum
 
def check_ticket(a, b):
    if a == b:
        return True
    else:
        return False
 
n = int(input("Enter the ticket number:"))
if check_ticket(calculate_sum(n//1000),calculate_sum(n%1000)):
    print('Lucky ticket!')