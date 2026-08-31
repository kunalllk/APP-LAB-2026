class CreditCard:
    def payment(self):
        print("Payment Done using Credit Card")
        
class DebitCard:
    def payment(self):
        print("Payment Done using Debit Card")
        
class UPI:
    def payment(self):
        print("Payment Done using UPI")
        
class Cash:
    def payment(self):
        print("Payemnt Done using Cash")
        
class Payment:
    def __init__(self,strategy):
        self.strategy = strategy
        
    def process(self):
        self.strategy.payment()
        
print("Choose Payment Option")
print("1.Credit Card")
print("2.Debit Card")
print("3.UPI")
print("4.Cash")

choice= int(input("Enter Your Choice:"))

if choice==1:
    p=Payment(CreditCard())
elif choice==2:
    p=Payment(DebitCard())
elif choice==3:
    p=Payment(UPI())
elif choice==4:
    p=Payment(Cash())
else:
    print("Invalid Input")
        
p.process()