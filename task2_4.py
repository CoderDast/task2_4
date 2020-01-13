Hour1 = int(input('Hour = '))
Minute1 = int(input('Minute = '))
Sec1 = int(input('Second = '))
Hour2 = int(input('2Hour = '))
Minute2 = int(input('2Minute = '))
Sec2 = int(input('2Second = '))
print('Result of time = ',
(Hour2 * 3600 + Minute2 *60 + Sec2)
  - 
(Hour1 * 3600 + Minute1 * 60 + Sec1))