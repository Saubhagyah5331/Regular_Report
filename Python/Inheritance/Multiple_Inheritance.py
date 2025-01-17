# Multiple Inheritance: 
# When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class. 

class Mother:
    def mother(self, mothername):
        self.mothername = mothername

class father:
    def father(self, fathername):
        self.fathername = fathername

class son:
    def son(self, sonname):
        self.sonname = sonname
        print(f"Son Name: {self.sonname}\nFather Name: {self.fathername}\nMother Name: {self.mothername}")

m1 = Mother("Sonali Devi")
m2 = father("Ramlal")
s1 = son("Saam")
