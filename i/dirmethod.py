marks={"Aman":100, "Rahul":90, "Rohit":50}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Aman":90, "Ajay": 85})
print(marks)
print(marks.get("Aman"))  #print none
print(marks["Aman"])   #return an error