class Car:
    count_of_wheels = 4
    def __init__(self, color, speed, mark):            #(указывает св-ва)
        self.color = color
        self.speed = speed
        self.mark = mark

    def drive(self, place):
        print(f"Машина марки {self.mark}, цвета {self.color}, едет в {place}"+f"со скоростью{self.speed}")

car_1 = Car("Синий", 30, "Матиз")

car_1.drive('Mac.by')

car2 = Car("Чёрный", 50, "BMV")
print(car_1.mark)
print(car_1.speed)
print(car_1.count_of_wheels)