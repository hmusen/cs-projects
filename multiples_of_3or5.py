def solution(number):
        good_nums = []
        for i in range(number):
            if (i % 3 == 0) or (i % 5 == 0):
                good_nums.append(i)

        print(good_nums)

        sum = 0
        for i in good_nums:
            sum = sum + i
        print(sum)

solution(15)

# Alternative method is to use list comprehension where take values where mod x is 0 when divided by 3 or 5.

# def alt_solution(number): 
#      print(sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])) 

# alt_solution(15)
