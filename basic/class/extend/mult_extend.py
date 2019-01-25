# 一般不推荐多重继承，可能会出现集成混乱，导致程序出现严重bug

class Base1:
    def foo1(self):
        print("我是foo1")

class Base2:
    def foo2(self):
        print("我是foo2")

class C(Base1, Base2):
    pass

if __name__ == "__main__":
    c = C()
    c.foo1()
    c.foo2()
