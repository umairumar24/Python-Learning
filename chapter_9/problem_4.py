word = "Donkey"

with open("hefile.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("hefile.txt", "w") as f:
    f.write(contentNew)