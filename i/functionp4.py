def rem(l, word):
    n = []
    for item in l:
        if item != word:
            n.append(item.strip(word))
        return n
    
l = ["Aman", "Aditya","Ajay","ay"]

print(rem(l,"ay"))
