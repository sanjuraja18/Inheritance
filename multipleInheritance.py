class Father:
    a=21
    b=32
    c=87
    def property(self):
        self.name="f_sanju"
        self.bank="f_sbi"
        print(self.name)
        print(self.bank)
class Mother:
    p=99
    q=88
    r=66
    def property1(self):
        self.name1="M_hhhh"
        self.bank1="M_axix"
        print(self.name1) 
        print(self.bank1) 
class Son(Father,Mother):
    pass
obj=Son()
obj.property()
print("hello bro")
obj.property1()
print(obj.a)
