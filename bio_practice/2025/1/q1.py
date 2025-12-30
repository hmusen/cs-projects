def is_palindrome(n):
    palindrome_pairs = []

    
    if str(n) == str(n)[::-1]:
        print('Already a palindrome')
        return
        
    else:
        for i in range(1, n):

            if str(i) == str(i)[::-1]:
                difference = n-i

                if str(difference) == str(difference)[::-1]:
                    palindrome_pairs.append( (i, difference) )
                    

    if not palindrome_pairs:
        for j in range(1,n):

            if str(j) == str(j)[::-1]:
                num1 = j
                just_two = n - j

                for k in range(1,just_two):

                    if str(k) == str(k)[::-1]:
                        difference = n-j-k

                        if str(difference) == str(difference)[::-1]:
                            palindrome_pairs.append( (num1, k, difference) )
                            

    print(palindrome_pairs[0])
        
is_palindrome(54)

# b) (1,9,44)

    
