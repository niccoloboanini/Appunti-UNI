
 ### ESERCIZI di PASSAGGIO ALLE EQ. DI STATO
 
#### 1)
$y(t) = 2 y(t-1) y(t-2) u(t-1)$ 
Avremo quindi:
$$
\begin{cases}
n=2 \\
m=1
\end{cases}
$$
Lo stato $x(t)$ ha dimensione $m+n = 3$ 
$$
x(t) = \begin{bmatrix} y(t-1) \\ y(t-2) \\ u(t-1) \end{bmatrix} = \begin{bmatrix} x_{1(t)} \\ x_{2}(t) \\ x_{3}(t) \end{bmatrix}   
$$
Da cui si può trovare una equazione di stato per ogni variabile:
- basta scorrere di un indice temporale
$$
\begin{align*}
&x_{1}(t+1) = y(t) =  2 \overbrace{y(t-1)} \overbrace{y(t-2)} \overbrace{u(t-1)} = 2 x_{1}(t) x_{2}(t) x_{3}(t)\\
&x_{2}(t+1) = y(t-1) = x_{1}(t)  \\
&x_{3}(t+1) = u(t)
\end{align*} $$
Riscrivendo:
$$
\begin{cases}
x_{1}(t+1)  = 2 x_{1}(t) x_{2}(t) x_{3}(t)\\
x_{2}(t+1) = x_{1}(t)  \\
x_{3}(t+1) = u(t)

\end{cases}
 \quad , \quad y(t) = 2 x_{1}(t)x_{2}(t)x_{3}(t)
$$
#### 2)
$$
y(t) -3y(t-2) = u(t) u(t-1)
$$
Riscrivo in forma normale, cioè $y(t) = \text{tutto il resto}$
$$
y(t) = +3y(t-2) + u(t) u(t-1)
$$
Abbiamo: $\begin{cases} n=2 \\ m=1 \end{cases} \Rightarrow x(t) \in \mathbb{R}^{3}$
Infatti (scrivendo anche $y(t-1)$ anche se non compare esplicitamente):
$$
x(t) = \begin{bmatrix} y(t-1) \\ y(t-2) \\ u(t-1) \end{bmatrix} = \begin{bmatrix} x_{1}(t) \\ x_{2}(t) \\ x_{3}(t)  \end{bmatrix}
$$
Posso scrivere le equazioni di stato, *traslando di $1$* al solito:
$$
\begin{cases}
x_{1}(t+1) = y(t) = 3y(t-2) + u(t) u(t-1) = 3 x_{2}(t) + u(t) x_{3}(t) \\
x_{2}(t+1) = y(t-1) = x_{1}(t)   \\
x_{3}(t+1) = y(t-2) = u(t)
\end{cases}
$$
Avente uscita: 
$$
y(t) = 3 x_{2}(t) + u(t)  x_{3}(t)
$$

## TEMPO CONTINUO (TC)
La rappresentazione ingresso uscita è data da una equazione differenziale:
$$
\large y^{(n)}(t) = g( t, y^{(n-1)}(t) , \dots , \dot y(t) , y(t), u^{(m)}(t), \dots, \dot u(t), u(t) )
$$
Quindi la forma normale dice che:
- la derivata di ordina massimo dell'uscita (ovvero $y^{(n)}(t)$) è una funzione di tutte le derivate dell'uscita, dell'ingresso $u(t)$ e di tutte le sue derivate

Dove $n$ e $m$ sono in questo caso *il massimo ordine di derivazione* rispettivamente degli ingressi e uscite. Vale il vincolo:
$$
m \leq n
$$
(nota: se il sistema è autonomo non compaiono $u(t)$ e le derivate)

### ESEMPIO: SISTEMA MECCANICO (CARRELLO)
Se abbiamo (dalle equazioni di Newton): $M \ddot y(t) = u(t) - b\dot y(t)$ 
Allora la rappresentazione è 
$$
\ddot y(t) = - \frac{b}{M} \dot y(t) + \frac{1}{M}u(t)
$$
Infatti in generale: $y(t) = g(\dot y(t) , y(t) , u(t))$
Quindi:
$$
\begin{cases}
n=2 \\
m=0
\end{cases}  \quad \Rightarrow \quad x(t) \in \mathbb{R}^2
$$

Troviamo le equazioni di stato, ricordando di mettere come uscite $y(t)$ e le sue derivate:
![[Pasted image 20220530122013.png|500]]

## PASSAGGIO ALLE EQUAZIONI DI STATO

### CASO IMMEDIATO: $m=0$ (il caso più complesso lo vediamo nei sistemi lineari)
- ovvero il caso in cui il sistema è **autonomo** oppure compare *l'ingresso non derivato*
Si ha un collegamento uno a uno tra le derivate dell'uscita e le variabili di stato: 
$$
x(t) = \begin{bmatrix} y \\ \dot y(t) \\ \vdots \\ y^{(n-1)}(t)\end{bmatrix}  = \begin{bmatrix} x_{1}(t) \\ x_{2}(t) \\ \vdots \\ x_{n}(t) \end{bmatrix}
$$
- cfr. Esempio del carrello

E poi riscrivo le equazioni di stato come $\dot x_{1}(t), \dot x_{2}(t), etc..$ 

![[Pasted image 20220530123813.png|500]]

#### ESEMPIO
#### 5) 
![[Pasted image 20220530123354.png|500]]

#### 6) (non in forma normale)
- nota: si scrive anche $\dot y(t)$ anche se non compare esplicitamente
![[Pasted image 20220530123650.png|600]]

