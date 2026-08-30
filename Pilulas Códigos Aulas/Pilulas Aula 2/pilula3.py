import datetime
#entrada
data_compra = input('Digite a data da compra d/n/aaaa: ')
meses = int(input('Prazo de garantia:'))
#processamento
data_inicial = datetime.datetimes.striptime(data_compra,'%d/%m/%Y')
data_final = data_inicial + datatime.timedelta(days=meses * 30)
#saida
print(f'Garantia válida até{data_final.striftime(%d/%m/%Y')}')
print(f'Dia da semana:{data_final.striftime(%A')}')