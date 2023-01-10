def reverse(woord):
    s = " "
    for i in woord:
        s = i + s
    return s
woord = "Python"
print("Het normale woord:",woord)
print("Het omgedraaide woord:", reverse(woord)) 