def sum_squares():
    sum = 0
    for i in range(1, 667001):
        if i % 2 == 1:
           sum = sum + (i**2) 
    
    print(sum)
sum_squares()

