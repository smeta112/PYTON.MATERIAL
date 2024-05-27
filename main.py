class Car:
    def __init__(self, color, speed, mark): #(указывает св-ва)
        self.color = color
        self.speed = speed
        self.mark = mark

    def drive(self, place):
        print(f"Машина марки {self.mark}, цвета{self.color}, едет в {self.place}, со скоростью{self.speed}")