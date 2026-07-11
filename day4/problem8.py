# student's average

marks = {
    "Math": 90,
    "Physics": 80,
    "Chemistry": 85,
    "English": 95
}

total = 0

for k,v in marks.items():
    total += v
    
average = total / (len(marks))
print("Average is " , average)