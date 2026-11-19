# All execution happens in this main file

from discountstrategy import DiscountStrategy
from discountservice import DiscountService
from diwali import Diwali
from holi import Holi

diwali_strategy= Diwali()
holi_strategy = Holi()

discount_service = DiscountService(diwali_strategy) # the initial default is set to diwali strategy 
discount_service.process()
# Applying diwali discount of 20%

discount_service.set_strategy(holi_strategy)
discount_service.process()
# Applying holi discount of 10%