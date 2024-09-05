def subcadena(cadena1, cadena2):
    m,n=len(cadena1),len(cadena2)
    zero_table=([0] * (n+1) for _ in range (m+1))
    max_length=0
    inicial_position:0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if cadena1[i-1] == cadena2[j-1]:
                zero_table[i][j]=zero_table[i-1][j-1]+1
                if zero_table[i][j]> max_length:
                    final_position=i


    inicial_position = final_position - max_length + 1
    return inicial_position, final_position