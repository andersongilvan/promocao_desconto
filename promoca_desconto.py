# 10% de desconto para compras acima de 100R$ #
# 20% de desconto para compras acima de 200R$ #
# 30% de desconto para compras acima de 300R$ #

valor_total = float(input('Digite o valor total do vaor de suas compras R$: '))
                    
if valor_total > 300:
    desconto = 0.3   # 30% de desconto #

elif valor_total > 200:
    desconto = 0.2 # 20% de desconto #

elif valor_total > 100:
    desconto = 0.1 # 10% de desconto #


else:
    desconto = 0 # sem desconto #

# calcular o valor do desconto #
valor_com_desconto = valor_total - (valor_total * desconto)

# exibir o valor total com desconto #
print('O valor total da sua compra após o desconto é de R${:.2f}'.format(valor_com_desconto))



