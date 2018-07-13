from math import pi
from mpmath import mp

#x = int(input('How many digits would you like to see pi to?   '))
user_pi = '{:.{}f}'.format(pi, x)

mp.dps = int(input('How many digits would you like to see pi to?   '))

#print(f'Here is pi to {x} digits: {user_pi}')

print(f'Here is pi to {mp.dps} digits: {mp.pi}')