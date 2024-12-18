# class GF:
#     def name(self,gf_name):
#         self.n=gf_name

# class P(GF):
#     # def __init__(self,p_name):
#     #     self.x = p_name

#     def p_properties(self, home, bank):
#         self.h=home
#         self.b=bank

# class C(P):
#     def c_properties(self, quali):
#         self.q=quali
#         print(self.h)
#         print(self.b)
#         print(self.q)
#         # print(self.x)
#         # self.name("sanju chauhan")
#         # print(self.n)
# obj=C("sanju")
# obj.p_properties('bhopal','sbi')
# obj.c_properties('M.tech')
# obj.name("chauhan")
# print(obj.n)




class GF:
    def gf_name(self,name):
        self.gf_name = name
class P(GF):
    def __init__(self,p_name):
        self.x=p_name

    def p_properties(self,home,bank):
        self.h=home
        self.b=bank

class C(P):
    def c_properties(self, quali):
        self.q=quali
        print(self.h)
        print(self.b)
        print(self.q)
        print(self.x)
        self.gf_name("rajaji chauhan")
        print(self.gf_name)

obj = C("sanju")
obj.p_properties("jhansi","SBI")
obj.c_properties("b.com")
    