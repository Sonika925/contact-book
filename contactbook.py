names = []
contacts= []
n=int(input("How many contact no. you wanna save: "))
for i in range(n):
    name = input("Name: ")
    contact= input("Contact Number: ")
    names.append(name)
    contacts.append(contact)
print("---------------------------------")
print("Name\t\tContact Number")
print("---------------------------------")
for i in range(n):
    print(*names[i],"\t\t",*contacts[i],sep="")
search= input("\nEnter search: ")
print("You are searching for:",search)
print("wait a sec....")
if search in names:
  index=names.index(search)
  contact=contacts[index]
  print(*contact,sep="")
else:
    print("oops you have not save this entity")
