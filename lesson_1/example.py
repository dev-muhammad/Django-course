import os


class Animal:

    name: str
    title: str = "Title"

    def __init__(self, name: str) -> None:
        self.name = name

    def hello(self) -> str:
        print(f"Hello {self.name}")

    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def class_function(self) -> None:
        print("I'm a class function")

    @staticmethod
    def static_function() -> None:
        print("I'm static function")
    
    @property
    def help(self):
        print("Help me")

animal = Animal("kuku")
# animal.static_function()
animal.help
# print(animal)
# Animal.class_function()
