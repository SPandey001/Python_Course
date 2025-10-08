dic = {"Alice's": 85, 'Pandey': 89, 'Shubham': 90, 'Bob': 91}
print(dic)

name = input("Enter the student's name: ")
if name in dic:
    print(f"{name}'s marks:", dic[name])
else:
    print("Student not found")
