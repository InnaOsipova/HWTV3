# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
# Какова вероятность того, что 3 мяча белые?


from math import factorial


# Нужно найти вероятность, это отношение благоприятных событий к числу всех  событий

def probability (m, n):
    return m/n

# функция по расчету сочетаний
def combinations (k, n):
    return factorial(n)/(factorial(k)*factorial(n-k))

var1 = probability(combinations(2,5),combinations(2,8)) * probability(combinations(1,5)*combinations(3,7), combinations(4,12))
var2 = probability(combinations(1,5)*combinations(1,3),combinations(2,8)) * probability(combinations(2,5)*combinations(2,7), combinations(4,12))
var3 = probability(combinations(0,5)* combinations(2,3),combinations(2,8))*probability(combinations(3,5)*combinations(1,7), combinations(4,12))

print(f'Вероятность , что три мяча белые = {round((var1 + var2+ var3)* 100, 2) } %')