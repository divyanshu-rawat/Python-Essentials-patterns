
# class OurClass:
#     def __init__(self, a):
#         self.OurAtt = a


# x = OurClass(10)
# print(x.OurAtt)


class P:

    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


p1 = P(1001)
print p1.x