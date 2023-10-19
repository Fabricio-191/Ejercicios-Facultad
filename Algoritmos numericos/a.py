a = 0.16
x0 = 0
h = 0.2
diff = [0.55561, -0.09598, -0.04647, 0.16689, -0.29911]

theta = (a - x0) / h

[delta1, delta2, delta3, delta4, delta5] = diff


valor  = (delta1 / h) * ( 1/1)
valor += (delta2 / h) * (-1/2 + theta)
valor += (delta3 / h) * ( 1/3 - theta             + theta ** 2 * (1/2))
valor += (delta4 / h) * (-1/4 + theta * (11/12)   - theta ** 2 * (3/4)   + theta ** 3 * (1/6))
valor += (delta5 / h) * ( 1/5 - theta * (5/6)     + theta ** 2 * (17/20) - theta ** 3 * (1/3)  + theta ** 4 * (1/24))
# valor += (delta6 / h) * (-1/6 + theta * (137/180) - theta ** 2 * (11/12) + theta ** 3 * (7/15) - theta ** 4 * (5/48) + theta ** 5 * (1/120))

print(f'Theta = {theta}')
print(f"Valor de la derivada en x = {a}")
print(valor)

valor2 = delta2
valor2 += delta3 * theta
valor2 -= delta3
valor2 += delta4 * ( 1/2 ) * theta ** 2
valor2 -= delta4 * ( 3/2 ) * theta
valor2 += delta4 * (11/12)

valor2 /= h ** 2

print(f"Valor de la derivada segunda en x = {a}")
print(valor2)
