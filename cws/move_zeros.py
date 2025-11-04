def move_zeros(lst):
    new_lst = []

    zeros = 0
    for e in lst:
        if e != 0:
            new_lst.append(e)
        elif e == 0:
            zeros += 1
    
    
    for zero in range(1,zeros+1):
        new_lst.append(0)

    print(new_lst)

move_zeros([1,2,0,0,0,0,0,3,4])
