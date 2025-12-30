def is_pal(x):
    s = str(x)
    return s == s[::-1]


def palindrome_decomposition(n):
    if is_pal(n):
        return "Already a palindrome"

    palindromes = [i for i in range(1, n) if is_pal(i)]
    pal_set = set(palindromes)

    # 2-palindrome sum
    for p in palindromes:
        if n - p in pal_set:
            return (p, n - p)

    # 3-palindrome sum
    for i in range(len(palindromes)):
        for j in range(i, len(palindromes)):
            remainder = n - palindromes[i] - palindromes[j]
            if remainder in pal_set:
                return (palindromes[i], palindromes[j], remainder)

    return None


# ---- User input ----
try:
    n = int(input("Enter a number: "))
    result = palindrome_decomposition(n)
    print(result)
except ValueError:
    print("Please enter a valid integer.")
