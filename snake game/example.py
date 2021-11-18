class Animal:
    def __init__(self) -> None:
        self.no_of_eyes=2
    def breathe(self):
        print("inhale exhale")

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
    def breathe(self):
        super().breathe()
        print("doing under water")
    def swim(self):
        print("swim swim")

nemo=Fish()
nemo.swim()
nemo.breathe()

