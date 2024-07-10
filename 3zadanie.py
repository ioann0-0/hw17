class Airplane:
    def __init__(self, airplane_type, max_passengers):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers
        self.current_passengers = 0

    def __eq__(self, other):
        return self.airplane_type == other.airplane_type

    def __add__(self, passengers):
        if self.current_passengers + passengers <= self.max_passengers:
            self.current_passengers += passengers
        else:
            raise ValueError("Превышает максимальную пассажировместимость")
        return self

    def __sub__(self, passengers):
        if self.current_passengers - passengers >= 0:
            self.current_passengers -= passengers
        else:
            raise ValueError("Количество пассажиров не может быть отрицательным")
        return self

    def __iadd__(self, passengers):
        return self + passengers

    def __isub__(self, passengers):
        return self - passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __str__(self):
        return f"Тип самолета: {self.airplane_type}, Максимум пассажиров: {self.max_passengers}, Текущие пассажиры: {self.current_passengers}"

if __name__ == "__main__":
    plane1 = Airplane("Boeing 747", 416)
    plane2 = Airplane("Airbus A380", 555)

    print(plane1 == plane2) 
    print(plane1 < plane2)   
    print(plane1 > plane2)   
    
    plane1 += 200
    print(plane1.current_passengers)  

    plane2 += 100
    print(plane2.current_passengers) 
