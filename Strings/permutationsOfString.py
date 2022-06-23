def permute(s, result):
    if s is None:
        return

    if len(s) == 0:
        print(result)

    for element in range(0, len(s)):
        add = s[element]
        rest = s[0:element] + s[element + 1:]
        permute(rest, result + add)


s = "ABCD"
permute(s, "")
