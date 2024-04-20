class ErrorVacancies(ValueError):
    pass


class Parking:
    def __init__(self, car):
        self.car = car
        self.vacancies = 5
        self.cars_num = []

    def car_parking(self, cars, num=1):
        if self.vacancies <= 0:
            raise ErrorVacancies('There are no more vacancies available')
        self.cars = cars
        self.vacancies -= num
        self.cars_num.append(cars)
        self.cars_num.append(num)

    def __repr__(self):
        return (f'{self.car} [{self.vacancies}] Vacancies Remaining, '
                f'Parked cars : {self.cars_num}')


parking_lot = Parking('Vitapark')
parking_lot.car_parking('Agile')
parking_lot.car_parking('Etios')
parking_lot.car_parking('Palio')
parking_lot.car_parking('Bravo')

print(parking_lot)
