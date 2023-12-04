workDaysM = int(input())
earnedDailyN = float(input())
kurs = float(input())
monthly = workDaysM*earnedDailyN
yearly = monthly*12+ monthly*2.5
danak = yearly*25/100
dohod = yearly - danak
dailyProfit = round (dohod/365*kurs, 2)
print (dailyProfit)

