def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        print("Already a palindrome")
        return

    # Precompute palindromes up to n
    palindromes = [i for i in range(1, n) if str(i) == str(i)[::-1]]
    pal_set = set(palindromes)

    results = []

    # ---- 2-palindrome decompositions ----
    for p in palindromes:
        if (n - p) in pal_set:
            results.append((p, n - p))

    # ---- 3-palindrome decompositions ----
    for p1 in palindromes:
        remainder = n - p1
        for p2 in palindromes:
            if p2 >= remainder:
                break
            p3 = remainder - p2
            if p3 in pal_set:
                results.append((p1, p2, p3))

    if results:
        for combo in results:
            print(combo)
    else:
        print("No palindrome decomposition found")


# ---- function call ----
is_palindrome(5336)
