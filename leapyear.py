#!/usr/bin/env python3
'classic problem of leap year'
def judgeleap(num):
    # if num%4!=0:
    # 	return 'non leap year'
    # elif num%100!=0 :
    # 	return 'leap year'
    # elif num%400!=0:
    # 	return 'non leap year'
    # else:
    # 	return 'leap year'
    if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0):
         return 'leap year'
    else:
        return 'non leap year'

year = int(input('enter a year\n'))
result = judgeleap(year)
print("" + year + result)