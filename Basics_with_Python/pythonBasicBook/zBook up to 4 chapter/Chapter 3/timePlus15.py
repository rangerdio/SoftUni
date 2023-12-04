hh = int(input())
mm = int(input())
mmsum = mm + 15
if mmsum < 60:
 mm = mmsum
elif mmsum >= 60:
 hh = hh + 1
 mm = mmsum - 60
 if hh == 24:
  hh = 0
if mm < 10:
 print(f"{hh}:0{mm}")
else:
 print(f"{hh}:{mm}")

