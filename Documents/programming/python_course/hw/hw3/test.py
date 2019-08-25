while True:
    cows = 0
    s = input()
    for i in range(4):
        for j in range(4):
            if '1234'[i] == s[j] and i != j:
                cows = cows + 1
    print(cows)