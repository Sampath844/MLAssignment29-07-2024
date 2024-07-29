def find():
    a = eval(input("Enter the array elements"))
    if(len(a)) < 3:
        print("Range not possible")
    else:
        for i in range(0,len(a)):
            for j in range((i+1),len(a)):
                if(a[i]<a[j]):
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
        range = a[len(a) - 1] - a[0]
        print("The Range of the array is",range)
find()
