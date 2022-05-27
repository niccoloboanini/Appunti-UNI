#### NOTAZIONE VATTORIALE E MATRICI A,B,C
Il modello corso di laurea magistrale che abbiamo visto lo possiamo scrivere in forma vettoriale in questo modo:
![[Pasted image 20220527113128.png|400]]
![[Pasted image 20220527113803.png|400]]
- Dove sono state individuate le matrici $\text{A}$ e $\text{B}$, $\text{C}$ sfruttando implicitamente il prodotto matrice per vettore (cfr. argomenti successivi)


#### NOTAZIONE GENERALE
Un modello compartimentale TD si può descrivere in questo modo:
$$
\large \boxed{x_{i}(t+1) = x_{i}(t)+f_{i}^{in}(t)-f_{i}^{out}(t)}
$$
Dove:
$$
f_{i}^{in}(t) = u_{i}(t) + \sum_{j \neq i}^{} a_{ji}x_{j}(t)+\gamma_{i}x_{i}(t)
$$
$$
f_{i}^{out}(t) = \sum_{j\neq i}^{} a_{ij}x_{i}(t) + \beta_{i}x_{i}(t)
$$



