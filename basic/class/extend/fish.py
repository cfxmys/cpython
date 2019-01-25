import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("我的位置是", self.x, self.y)

class GoldFish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        # 调用未绑定的父类方法，传入的是子类的实例对象
        #Fish.__init__(self)
        # super 方法，推荐super 方法
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有吃的")
            self.hungry = False
        else:
            print("太撑了，吃不下了")

if __name__ == "__main__":
    fish = Fish()
    fish.move()
    fish.move()

    goldFish = GoldFish()
    goldFish.move()
    goldFish.move()

    shark = Shark()
    shark.eat()
    shark.eat()
    # 如果在__init__ 方法中，不调用父类的__init__方法，或者不调用super方法，直接调用move 方法会报错
    shark.move()
