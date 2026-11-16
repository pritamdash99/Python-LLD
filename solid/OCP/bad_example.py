class PaymentProcessor:
    def pay(self, payment_method : str, amount : int):
        if payment_method == "UPI":
            print(f"Starting UPI transaction of Rs.{amount}")
            print("UPI transaction finished")
        elif payment_method == "credit_card":
                    print(f"Starting credit_card transaction of Rs.{amount}")
                    print("credit_card transaction finished")
        elif payment_method == "net_banking":
                    print(f"Starting net_banking transaction of Rs.{amount}")
                    print("net_banking transaction finished") 

pay_p = PaymentProcessor()
pay_p.pay("UPI", 200)

# Starting UPI transaction of Rs.200
# UPI transaction finished

"""
This code works for now but if another payment method were to be introduced - 
"Paypal" for example, then we would have to - 
Add another elif block thus MODIFYING the original tested code.

This violets Open Close Principle [Open for addition Closed for modification]
"""