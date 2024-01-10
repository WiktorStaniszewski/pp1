def f(d):
    carsin = []
    for item in d:
        if item[1] == "in":
            carsin.append(item[0])
        if item[1] == "out":
            carsin.remove(item[0])
    return sorted(carsin)

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))
cars1 = [["KR234","in"],["KR234","out"]]
print(f(cars1))
