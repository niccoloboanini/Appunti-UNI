#### NOTAZIONE VATTORIALE E MATRICI A,B,C
Il modello corso di laurea magistrale che abbiamo visto lo possiamo scrivere in forma vettoriale in questo modo:
![[Pasted image 20220527113128.png|400]]
![[Pasted image 20220527113803.png|400]]
- Dove sono state individuate le matrici $\text{A}$ e $\text{B}$, $\text{C}$ sfruttando implicitamente il prodotto matrice per vettore (cfr. argomenti successivi)


### NOTAZIONE GENERALE (TD)
Un modello compartimentale TD si può descrivere in questo modo:
$$
\large \boxed{x_{i}(t+1) = x_{i}(t)+f_{i}^{in}(t)-f_{i}^{out}(t)}
$$
Dove:
$$
f_{i}^{in}(t) = u_{i}(t) + \sum_{j \neq i}^{} a_{ji}x_{j}(t)+\gamma_{i}x_{i}(t)
$$
- $a_{ji}$ rappresenta la percentuale di risorse $x_{j}(t)$ che passano dal compartimento $j$ a $i$.
- $\gamma_{i}$ rappresenta la percentuale di risorse generate all'interno del compartimento $i$ (come erano gli interessi nell'esempio della banca)
- $u_{i}$ naturalmente sono gli ingressi esterni che vanno in $i$
![[Pasted image 20220527115628.png]]
$$
f_{i}^{out}(t) = \sum_{j\neq i}^{} a_{ij}x_{i}(t) + \beta_{i}x_{i}(t)
$$
- $a_{ij}$ percentuale di risorse che vanno verso il compartimento $j$
- $\beta_{i}, x_{i}(t)$ sono le risorse che escono definitivamente dal sistema (vanno verso l'esterno)
![[Pasted image 20220527115815.png]]


Mettendo tutto insieme si giunge alla **equazione di stato**:
![[Pasted image 20220527115956.png|500]]
- Esistono ovviamente anche alcuni vincoli. Ad esempio: la somma delle risorse che escono dovrà essere inferiore o uguale alle risorse presenti in un compartimento

#### ESEMPIO: CATENA DI PRODUZIONE (TD)
Supponiamo che una catena di produzione abbia $4$ stati collegati tra loro. Si può scrivere l'equazione di bilancio per ciascuno stato.
Guardando l'equazione per lo stato $2$ (più ingressi):
![[Pasted image 20220527121041.png|400]]

Per lo stadio $3$ invece (più uscite):
![[Pasted image 20220527121245.png|400]]


Si possono riscrivere tutte le equazioni di stato anche in forma matriciale, ottenendo:
![[Pasted image 20220527121857.png|500]]

- In $x_{1}$ non compare nessuno stato, quindi la prima riga è comporta da tutti $0$. Compare invece l'ingresso $u_{1}(t)$ e vale $1$, quindi questo lo scriviamo nella matrice $B$ degli ingressi $u(t)$
	- si ripete questo ragionamento per ciascuna equazione di stato
Abbiamo riscritto il problema quindi nella forma generale:
$$
x(t+1) = \text{A} \ x(t) + \text{B} \ u(t)
$$
- dove $\text{A}$ e $\text{B}$ rappresentano in modo univoco il mio sistema
	- Lo studio di queste matrici sarà l'elemento centrale per lo studio del sistema dinamico


### NOTAZIONE GENERALE (TC)
Un modello compartimentale TD si può descrivere in questo modo:
$$
\large \boxed{\dot x_{i}(t) = f_{i}^{\text{in}}(t)-f_{i}^{\text{out}}(t)}
$$
- abbiamo quindi delle variazioni istantanee (tassi) in ingresso e in uscita
- È analogo al caso TC, dato che: $$\underbrace{x_{i}(t+1)-x_{i}(t)}_{\Large \dot x_{i}} = f_{i}^{in}-f_{i}^{out}$$ 
# MODELLO DI TRANSIZIONE DI STATO
Abbiamo ancora un modello con $n$ stati. Tra uno stato e l'altro non vengono più trasferite risorse, bensì, *attributi (o qualità)*, solitamente di tipo **probabilistico**
- Indicano la *probabilità di trovarsi in un certo stato $x_{i}(t)$*

#### ESEMPIO: PREVISIONI DEL TEMPO
![[Pasted image 20220527130908.png|500]]

- si descrive *come si passa da uno stato all'altro*, tenendo conto della probabilità di passaggio da uno stato all'altro
	- si studia quindi la probabilità di trovarsi in uno stato, tenendo conto della probabilità di transizione tra gli stati
Ovviamente vale il vincolo: 
$$
x_{1}(t) + x_{2}(t) + x_{3}(t) = 1
$$

Sfruttando la teoria della probabilità condizionata, si può calcolare ad esempio:
La *probabilità di trovarsi nello stato piovoso al tempo $t+1$* è la seguente:
![[Pasted image 20220527131359.png|600]]

Analogamente:
$$
x_{1}(t+1) = x_{1}(t) \frac{1}{2} + x_{2}(t) \frac{1}{2}
$$
$$
x_{2}(t+1) = x_{1}(t) \frac{1}{2} + x_{2}(t) \frac{1}{4} + x_{3}(t) \frac{1}{2}
$$



