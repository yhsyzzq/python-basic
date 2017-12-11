class User:
    '''用户类'''
    # 用户姓名
    userName = ""
    # 用户编码
    userCode = ""

    # 私有属性
    __age = 0

    # 构造函数
    def __init__(self, userName, userCode, age):
        self.userName = userName
        self.userCode = userCode
        self.__age = age

    # 自定义函数
    def sayHell(self):
        print("Hello, I am " + self.userName + ", Nice to meet you!")
        self.__tellAge()

    def __tellAge(self):
        print("I am %d years old" % self.__age)


user = User('曾志琦', '332406', 30)
print(user.userName + ":" + user.userCode)

user.sayHell()
