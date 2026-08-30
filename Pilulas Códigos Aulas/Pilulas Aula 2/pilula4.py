import statistics as st
Lote1 = int(input( 'Produção Lote 1:'))
Lote2 = int(input( 'Produção Lote 2:'))
Lote3 = int(input( 'Produção Lote 3:'))
media = st.mean ((Lote1,Lote2,Lote3) )
desvio = st.stdev ( (Lote1,Lote2,Lote3))
print(f'Media: {media:.2f}')
print(f'Desvio padrão:{desvio:.2f}') 