# Se tiene un n´umero natural n, crear una funci´on que retorne
# una lista de todos los pares de n´umeros naturales que sumen
# el n´umero n. n < 10^6

def ejercicio2(n): 

    if ( n < pow(10, 6) ): 

        # Lista de numeros pares que sumen n
        lista_pares_suma_n = []

        # Necesitamos todos los numeros pares.
        for i in range(0, n + 1, 2):
            # Luego todos los numeros pares nuevamente para verificar quien suma n
            for a in range(0, n + 1, 2):
                # Verificamos si la suma de uno de estos numeros da n
                if( a + i == n ): 
                    lista_pares_suma_n.append([ a, i ])

        return lista_pares_suma_n
    
    else: 

        return None

print(ejercicio2(14))