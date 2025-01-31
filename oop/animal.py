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
