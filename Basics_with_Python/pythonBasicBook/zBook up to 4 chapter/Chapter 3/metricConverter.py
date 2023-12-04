import math
number = float(input())
sourceMetric = input().lower()
outputMetric = input().lower()
meters = 0
output = 0

if sourceMetric == "mm":
    meters = number/1000
elif sourceMetric == "cm":
    meters = number/100
elif sourceMetric == "m":
    meters = number
elif sourceMetric == "mi":
    meters = number / 0.000621371192
elif sourceMetric == "in":
    meters = number / 39.3700787
elif sourceMetric == "km":
    meters = number * 1000
elif sourceMetric == "ft":
    meters = number / 3.2808399
elif sourceMetric =="yd":
    meters = number / 1.0936133

if outputMetric == "mm":
    output = meters * 1000
elif outputMetric == "cm":
    output = meters * 100
elif outputMetric == "m":
    output = meters
elif outputMetric == "mi":
    output = meters * 0.000621371192
elif outputMetric == "in":
    output = meters * 39.3700787
elif outputMetric == "km":
    output = meters / 1000
elif outputMetric == "ft":
    output = meters * 3.2808399
elif outputMetric == "yd":
    output = meters * 1.0936133
print(output)