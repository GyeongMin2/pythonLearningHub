# 상속 예제 — 동물
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return '...'

class Dog(Animal):
    def speak(self):
        return '멍멍'

class Cat(Animal):
    def speak(self):
        return '야옹'

def introduce(pet: Animal):
    print(pet.name, pet.speak())

if __name__ == '__main__':
    introduce(Dog('바둑'))
    introduce(Cat('나비'))
