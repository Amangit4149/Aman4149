with open("file.txt") as f:
    content1 = f.read()

with open("this.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these ffiles are identical")

else:
    print("No these  file are not identical")
    