from abc import ABC, abstractmethod
#Informal Interface
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount : int):
        pass

#Concrete Classes - 
class UPIPayment(PaymentMethod):
    def pay(self, amount: int):
        print(f"Paying through UPI of Rs. {amount}")

class DebitCardPayment(PaymentMethod):
    def pay(self, amount: int):
        print(f"Paying through Debit Card of Rs. {amount}")

class NetBankingPayment(PaymentMethod):
    def pay(self, amount: int):
        print(f"Paying through NetBanking of Rs. {amount}")

#Executing Class - This class remains unchanged even if there's 10 more payment methods available later.
class PaymentProcessor :
     def process_payment(self, payment_method :PaymentMethod, amount :int):
         payment_method.pay(amount)

debit = DebitCardPayment()
netbanking = NetBankingPayment()
payment_processor = PaymentProcessor()

payment_processor.process_payment(debit,500)
payment_processor.process_payment(netbanking,1000)
# Paying through Debit Card of Rs. 500
# Paying through NetBanking of Rs. 1000

#--------------

class PaypalPayment(PaymentMethod):
     def pay(self, amount: int):
         print(f"Paying through Paypal of Rs. {amount}")

paypal = PaypalPayment()
payment_processor.process_payment(paypal,3000)
# Paying through Paypal of Rs. 3000
