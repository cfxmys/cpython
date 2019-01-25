class Parent:
    def hello(self):
        print("正在调用父类的方法……")


class Child(Parent):
    pass
    # def hello(self):
    #     print("正在调用子类的方法……")

if __name__ == "__main__":
    p = Parent()
    p.hello()

    c = Child()
    c.hello()