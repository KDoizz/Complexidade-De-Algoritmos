def troca(vetor, i, j): 
    aux = vetor[i]               # C4.1 
    vetor[i] = vetor[j]          # C4.2 
    vetor[j] = aux               # C4.3 

def bolha(vetor): 
    for i in range(0, len(vetor) - 1, 1):       # C1 
        for j in range(i+1, len(vetor), 1):     # C2 
            if vetor[i] > vetor[j]:             # C3 
                troca(vetor, i, j)              # C4

X = [99,88,77,66,55,44,33,22,11] 
bolha(X)