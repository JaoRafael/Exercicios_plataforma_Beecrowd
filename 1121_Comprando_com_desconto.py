valor = float(input())
qtd = int(input())
total = qtd * valor
valor_final = total - (total * (0.10 + qtd * 0.01))
print(f'{total:.2f}')
print(f'{valor_final:.2f}')
