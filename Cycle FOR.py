cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
for i in range(len(cars)):
    print('Я езжу на автомобиле марки', cars[i])

cars_count = 0
cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
for i in range(len(cars)):
    cars_count += 10
    print('Я езжу на автомобиле марки', cars[i], cars_count)
