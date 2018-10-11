
favourite = "FishC"
for each in favourite:
   print(each, end='\t')

for i in range(10):
    print("for each time is " + str(i))
    if i % 2 != 0:
        print(i)
        continue
    i += 2
    print(i)