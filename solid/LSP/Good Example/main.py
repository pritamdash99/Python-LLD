#We execute the code here

from savings import SavingsAccount
from fixedDeposit import FixedDeposit

s = SavingsAccount(1000)
s.deposit(100)
s.withdraw(50)
# Amount deposited, current balance = 1100
# Amount Withdrawn, current balance = 1050

fd = FixedDeposit(2000)
fd.deposit(200)
# Amount Deposited, current balance = 2200