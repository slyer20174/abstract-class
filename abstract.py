from abc import ABC, abstractmethod
class absclass(ABC):
    def print(self,x):
        self.x=x
        print("the passed value is", self.x)

    @abstractmethod 
    def task(self):
        print(" i am inside the abstract method")
class testclass(absclass):
    def task(self):
        print("i am outside")
object=testclass()
object.task()
object.print(573)
