n = int(input())
n = n % 1440
hours = n // 60
minutes = n % 60
print(hours, minutes)