with open("input.txt", "r", encoding="utf8") as in_file:
    n = int(in_file.readline())
    Set_Nb = set(range(1, n + 1))
    temp = set()

    for line in in_file:
        if "YES" in line:
            Set_Nb &= temp
        elif "NO" in line:
            Set_Nb -= temp
        elif "HELP" not in line:
            temp = set(map(int, line.split()))

print(' '.join(map(str, sorted(Set_Nb))))
