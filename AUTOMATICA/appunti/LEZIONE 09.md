## CALCOLO DELL'ESPONENZIALE DI MATRICE

### CASO 1) $A$ è DIAGONALE
- Calcolo immediato: **basta fare l'esponenziale dei termini sulla diagonale**
	- questo risultato deriva dalla definizione:
![[Pasted image 20220603110946.png]]
	- Da cui poi i termini finali sulla matrice si possono riscrivere in maniera "esponenziale" osservando che abbiamo lo sviluppo di Taylor
Quindi:
![[Pasted image 20220603111002.png|400]]

### CASO 2) $A$ è DIAGONALIZZABILE
$A \in \mathbb{R}^{n\times n}$ ha $n$ autovalori: $\lambda_{1},\lambda_{2},\dots,\lambda_{n}$
Gli autovalori sono gli zeri del polinomio caratteristico, così definito:
$$
\varphi(\lambda) = \det (\lambda I - A)
$$
Dal teorema fondamentale dell'algebra, ne deriva che $\varphi(\lambda)$ si può così scomporre:
$$
\varphi(\lambda) = (\lambda-\lambda_{1}) (\lambda-\lambda_{2}) \dots (\lambda-\lambda_{n}) 
$$
#### ESEMPIO
![[Pasted image 20220603111841.png|500]]

Un altro possibile modo di definire gli autovalori è il seguente:
$$
\lambda_{i} \text{ autovalore di } A \iff \text{esiste almeno un autovettore } v_{i}  \text{ t.c. } Av_{i} = \lambda_{i}v_{i}
$$
	- ne preserva la direzione


Una matrice $A$ è diagonalizzabile se esiste $T \in \mathbb{R}^{n\times n}$ invertibile tale che:
$$
A = T \begin{bmatrix} \lambda_{1} & 0 & \dots \\ 0 & \ddots  \\ \vdots  &  & \lambda_n\end{bmatrix} T^{-1} \quad \Rightarrow \boxed{A = T \Lambda T^{-1}} 
$$
- La matrice $T$ è proprio quella che diagonalizza
- Sulla diagonale ci sono proprio gli autovalori


**Adesso quindi:**
Supponiamo $A$ diagonalizzabile, ovvero $A = T \Lambda T^{-1}$
Posso facilmente calcolare $A^{k}$, in questo modo:
$$
A^{k}=  \underbrace{T \Lambda \overbrace{T^{-1} \quad T}^{I} \Lambda T^{-1} \quad \dots \quad T \Lambda T^{-1}}_{A^{k}}
$$
- Dove tra le varie matrici si nota il prodotto $T \cdot T^{-1} = I$ , quindi posso riscrivere:
$$
A^{k} = T\underbrace{\Lambda \Lambda \dots \Lambda}_{k \text{ volte}} T^{-1} 
$$
Quindi se sappiamo diagonalizzare $A$, possiamo facilmente *trovare la diagonalizzazione di qualsiasi potenza per qualsiasi $k$ della matrice di partenza $A$*, in questo modo:
$$
A^{k} = T \ \Lambda^{k}\ T^{-1}
$$

Dalla definizione di esponenziale di matrice con le serie di Taylor possiamo riscrivere il termine $A^{k}$:
$$e^{At} = \sum_{k=0}^{\infty} \frac{(At)^{k}}{k!} = \sum_{k=0}^{\infty} \frac{A^{k} \ t^{k}}{k!} = \sum_{k=0}^{\infty} T \Lambda^{k}T^{-1} \ \frac{t^{k}}{k!}
$$
da cui:
$$
e^{At} = T\big( \underbrace{\sum_{k=0}^{\infty} \Lambda^{k} \frac{t^{k}}{k!}}_{e^{\Lambda t}}  \big)= T e^{\Lambda t} T^{-1}
$$
- basta avere un algoritmo per diagonalizzare la matrice così da trovare l'esponenziale di matrice e capire così l'evoluzione del sistema

Riassumendo:
![[Pasted image 20220603114725.png|500]]
- da cui posso calcolare appunto $x_{\ell}(t) = e^{At}x_{0}$

### ESEMPIO: SISTEMA MECCANICO
Sappiamo che:
![[Pasted image 20220603115008.png|400]]

Capiamo l'evoluzione dello stato, calcolando l'esponenziale di matrice:
![[Pasted image 20220603115747.png|650]]

Possiamo quindi calcolare l'evoluzione libera (ovvero come si evolve il sistema in assenze di sollecitazioni esterne):
$$
x_{\ell} = e^{At}x(0)
$$
- dove $x(0)$ è il vettore dello stato di dimensione $2$:
$$
\begin{bmatrix} x_{1}(t) \\ x_{2}(t) \end{bmatrix} = \begin{bmatrix}\text{posizione} \\ \text{velocita'}\end{bmatrix}
$$
Quindi:
![[Pasted image 20220603120407.png|500]]

Graficamente (ricordando che l'attrito c'è):
![[Pasted image 20220603120826.png|600]]

- Abbiamo ottenuto una evoluzione libera che nel tempo dipende dai segnali $e^{\Lambda t}$, ovvero i segnali sulla diagonale di tale matrice. Essi prendono il nome di *modi naturali* di evoluzione del sistema
![[Pasted image 20220603121310.png|400]]

Nel caso del carrello:
- $\lambda_{1}= 0$ quindi $e^{\lambda_{1}t} = 1$
- $\lambda_{1}= -1$ quindi $e^{\lambda_{2}t} = e^{-t}$


Se fossero tutte diagonalizzabili le matrici sarebbe già fatto tutto.
- Il problema è che in molti casi queste non lo sono
	- Per questo, la *trasformata di Laplace* permette di calcolare $e^{At}$ in modo alternativo (e permette anche di calcolare l'evoluzione forzata oltre che quella libera)


---
# TRASFORMATA DI LAPLACE

### INTRO
Studiamo solo i casi di **segnali causali** (perché consideriamo solo sistemi causali con istante iniziale $0$, essendo anche TI)
$$
f(t) = 0  \quad , \quad t <0
$$
Ad esempio: il segnale *gradino unitario $1(t)$*
![[Pasted image 20220603121837.png|400]]


## DEFINIZIONE
Permette di passare da dominio di variabile reale (del tempo) $f(t)$ a un dominio trasformato $s$, dove $s$ è un generico numero complesso $s = \sigma + jw$. In questo modo:
$$
\large \boxed{F(s) = \mathcal{L} \{ f(t)\} = \int_{0}^{\infty} f(t) e^{-st} \,dt}
$$
- è una generalizzazione della trasformata di Fourier (basta considerare solo la parte immaginaria, ovvero porre $s = j \omega$), quindi: $\displaystyle F(s)_{s=j \omega} = \int_{0}^{\infty} f(t) e^{-j \omega t} \,dt$

## TRASFORMATA DEL GRADINO UNITARIO (unico conto con la definizione)
- avendo un integrale improprio, è corretto studiare prima la convergenza di esso
	- La complicazione è che $s$ è complesso quindi dobbiamo guardare il suo modulo
		- In particolare dobbiamo prestare attenzione all'esponenziale immaginario $e^{-jwt}$ che viene fuori. Possiamo riscriverlo come combinazione di seni e coseni, ovvero: $e^{j \omega} = \cos \omega + j\sin \omega$
![[Pasted image 20220603123725.png|600]]

Dobbiamo quindi studiare per la convergenza i vari casi dell'esponenziale che abbiamo ottenuto
- per avere convergenza, l'area sottostante deve tendere a $0$, quindi:
![[Pasted image 20220603123949.png|550]]
- abbiamo così trovato la $ROC$ (regione di convergenza) della trasformata del gradino sul piano $s$
Posso adesso calcolare l'integrale nella relativa regione di convergenza (facile perché abbiamo un esponenziale):
![[Pasted image 20220603124144.png|600]]

Quindi:
$$
\mathcal{L}\{1(t)\} = 1/s
$$
Ovvero:
$$
\large \boxed{1(t) \longleftrightarrow \frac{1}{s}}
$$
- d'ora in avanti consideriamo l'operatore trasformata come "simbolico", ovvero lo useremo come strumento per passare da un dominio all'altro (senza preoccuparci della definizione attraverso l'integrale)