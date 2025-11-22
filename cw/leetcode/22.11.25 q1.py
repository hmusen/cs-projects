def minimum_flips(n):
    s = bin(n)[2:]
    flipped = 0

    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            flipped += 2
        left += 1 
        right -= 1

    print(flipped)

minimum_flips(6)