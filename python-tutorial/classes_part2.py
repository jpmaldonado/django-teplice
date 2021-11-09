class Class2:
    def method(self, param):
        print(f"Method of class 2 {param}")
        print(self.__class__.__name__)

class Class1:
    x = 1
    def method(self):
        print("Method of Class 1")

    def sample_static():
        print("Static method")

class Class3(Class2, Class1):
    def test(self):
        Class1.method(self)

object = Class3()
object.method(3)

object.test()
Class1.sample_static()
print(Class1.x)