#Faturamento de cada estado de acordo com cada exércicio
faturamento_SP = 67836.43
faturamento_RJ = 36678.66
faturamento_MG = 29229.88
faturamento_ES = 27165.48
faturamento_OUTROS = 19849.53


#Calculo do faturamento total
faturamento_total = faturamento_ES + faturamento_MG + faturamento_RJ + faturamento_SP + faturamento_OUTROS

#Calculo da porcentagem de cada estado
print("""Porcentagem de cada estado em relação ao total:
        SP: {:2f}
        RJ: {:2f}
        MG: {:2f}
        ES: {:2f}
        OUTROS: {:2f} 
        """. format(faturamento_SP*100/faturamento_total,
                    faturamento_RJ*100/faturamento_total,
                    faturamento_MG*100/faturamento_total,
                    faturamento_ES*100/faturamento_total,
                    faturamento_OUTROS*100/faturamento_total))


