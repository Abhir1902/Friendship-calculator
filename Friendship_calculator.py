#Friendship calculator
class student:
    def __init__(self,name,roll_no,class_name):
        self.name = name
        self.roll_no = roll_no
        self.class_name = roll_no
        self.l=list()
    def make_a_friend(self,friend):
        self.l.append(friend)
        friend.l.append(self)
    def closeness(self,friend):
        flag=0
        for i in self.l:
            if i == friend:
                flag=1
                return 1
        if flag == 0:
            for i in self.l:
                for j in i.l:
                    if j==friend:
                        flag=1
                        return 2
        if flag == 0:
            return 3
    def remove_friend(self,friend):
        self.l.remove(friend)
        friend.l.remove(self)
A=student('A','20BCE1076','Mango')
B=student('B','20BCE1077','Blue')
C=student('C','20BCE1011','Red')
A.make_a_friend(B)
B.make_a_friend(C)
print("THE CLOSENESS OF A WITH B IS: ")
print(A.closeness(B))
print("THE CLOSENESS OF A WITH C IS: ")
print(A.closeness(C))
print("THE CLOSENESS OF B WITH A IS: ")
print(B.closeness(A))
print("THE CLOSENESS OF C WITH A IS: ")
print(C.closeness(A))
print("THE CLOSENESS OF C WITH B IS: ")
print(C.closeness(B))
A.remove_friend(B)
print("THE CLOSENESS OF A WITH B IS: ")
print(A.closeness(B))
print("THE CLOSENESS OF A WITH C IS: ")
print(A.closeness(C))
print("THE CLOSENESS OF B WITH A IS: ")
print(B.closeness(A))
print("THE CLOSENESS OF C WITH A IS: ")
print(C.closeness(A))
print("THE CLOSENESS OF C WITH B IS: ")
print(C.closeness(B))
                        
        
        
        
        


