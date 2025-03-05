def rem(l, word):
    for item in l:
        l.remove(word)
        return l
    
l = ["Harry", "Shubham", "an"]

print(rem(l, "an"))
