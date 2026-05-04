import sys
from fractions import Fraction
from decimal import Decimal as D

ideal_temp = 95.5 
current_temp = 95.99999

print(f"Ideal temp {ideal_temp}")
print(f"current temp {current_temp}")
print(f"difference temp {ideal_temp - current_temp}")

print(sys.flote_info)