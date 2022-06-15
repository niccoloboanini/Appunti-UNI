### BUONA POSIZIONE DEL PROBLEMA DI CONTROLLO
Come visto la retroazione sull'uscita non modifica gli autovalori nascosti, pertanto il polinomio $\varphi_{h}(s)$ rimane inalterato nel passaggio da anello aperto a ciclo chiuso
Polinomio in anello aperto:
$$ \varphi(s) = \underbrace{\varphi_{h}(s)} \ a(s)  $$
Polinomio in ciclo chiuso:
$$
\varphi^{*}(s) = \underbrace{\varphi_{h}(s)} \ [a(s) +K \ b(s)]
$$
Dato che il nostro obiettivo è quello di rendere il sistema in ciclo chiuso *asintoticamente stabile*, ovvero avere radici di $\varphi^{*}(s)$ con $\text{Re}<0$, allora:
- $\varphi_{h}(s)$ dato che rimane inalterato, dovrà essere stabile asintoticamente

>Allora si dice che un problema in retroazione sull'uscita è **ben posto** (cioè più facilmente risolvibile), quando $\varphi_{h}(s)$ ha tutte radici con $\text{Re}<0$ - ovvero quando gli autovalori nascosti sono già stabili (non potendo essere modificabili)

- Quindi se per la retroazione sullo stato si studia "solo" controllabilità e stabilizzabilità, in questo caso è necessario lo studio anche dell'*osservabilità*

**Nota:** il fatto che il problema sia ben posto è condizione necessaria per avere $K$ guadagno stabilizzante ma in generale **non è sufficiente** con la legge di controllo $u=-Fy+Hy^{\text{o}}$
- Nel caso del carrello era possibile, ma abbiamo già visto un altro esempio in cui non era possibile

## PROGETTO DELLA RETROAZIONE ALGEBRICA SULL'USCITA
Sappiamo che:
![[Pasted image 20220615004934.png|500]]
Dove:
- Per la specifica $1$ e $3$ si cerca $K$ adatto
- Per la specifica $2$ si sceglie $H$ adatto
	- Con $$ G^{*}_{y^{\text{o}}y}(0)=\frac{b(0)}{a(0)+Kb(0)}H=1 $$
	- Quindi $$ H = \frac{a(0)+Kb(0)}{b(0)} $$

Quindi, riassumendo:
![[Pasted image 20220615005337.png|600]]
- Se fallisce al caso $2$, vedremo che ci saranno altre soluzioni

### QUANDO L'ALGORITMO PUO' FALLIRE: COSA FARE
1) Problema non ben posto
	1) Agisco sulle matrici $B$ (aggiungere/modificare variabili di controllo) e $C$
2) Autovalori nascosti 
	1) Non ho abbastanza informazioni interne del sistema
3) Se fallisce anche se ben posto
	1) La retroazione algebrica sull'uscita non è sufficiente: devo considerare un controllore dinamico --> retroazione dinamica sull'uscita (con leggi di controllo non generali)
4) Caso particolare $b(0)=0$ --> cerco di modificare $b(s)$ modificando $B$ e/o $C$

![[Pasted image 20220615010206.png|600]]
Si fa un passo indietro quindi se l'algoritmo fallisce


### ESEMPIO
- Supponendo al solito che non ci siano parti nascosti (sempre vero quando ci viene dato $G(s)$)
- Si vuole progettare una retroazione sull'uscita del tipo $u=-Ky+Hy^\text{o}$

- Dato che non ho autovalori nascosti, allora problema ben posto
- Calcolo quindi $\varphi^{*}(s) = \varphi_{h}(s) \ a^{*}(s)$
- Uso Cartesio se il polinomio è di secondo grado per capire quando abbiamo tutte radici con $\text{Re}<0$
	- Quindi cerco i casi in cui abbiamo stabilità asintotica in ciclo chiuso (specifica $1$)
		- Per la specifica $3$ si disegna il luogo delle radici (per scegliere smorzamento e parte reale appositi)
- Calcolo $H$ secondo la formula per la specifica $2$ (guadagno in ciclo chiuso unitario)

Specifiche $1$ e $2$:
![[Pasted image 20220615010912.png|600]]

Specifica $3$:
![[Pasted image 20220615010654.png|500]]

Esempio sulle slide (in cui si sceglie $K=6$ che comunque rispetta le specifiche):
![[Pasted image 20220615010956.png|500]]

--- 

# RETROAZIONE DINAMICA SULL'USCITA
- Quando la retroazione algebrica non basta

Idea: *generalizzare la legge di controllo precedentemente vista nel dominio di Laplace*
$$
u(t) = -Ky(t)+Hy^{\text{o}}(t) \to U(s) = -H Y(s) +H Y^{\text{o}}(s) \to \text{da generalizzare}
$$
Per generalizzare significa che $H$ e $K$ *non sono più scalari*, ma diventano *funzioni di trasferimento* (in modo tale da avere più margine di scelta)
Quindi:
$$
u(t) = -Ky(t)+Hy^{\text{o}}(t) \to U(s) = -H Y(s) +H Y^{\text{o}}(s) \to \boxed{U(s) = -K(s)Y(s)+H(s)Y^{\text{o}}(s)}
$$
- Viene detta *retroazione dinamica* sull'uscita (dinamica perché *il controllore diventa un sistema dinamico*, ovvero avente le sue funzioni di trasferimento)
	- Vogliamo controllare un sistema dinamico $\to$ scegliamo un controllore dinamico (stessa complessità)

### DIAGRAMMA A BLOCCHI
- $\mathcal{P}$: sistema da controllare (con accesso solo di $u$ e $y$)
- $H(s)$: funzione di trasferimento (ovvero un *filtraggio* [elaborazione] del segnale di riferimento $y^{\text{o}}$)
- $K(s)$: altro *filtro* che elabora l'uscita $y$

Sommando le due elaborazioni filtrate si genera *l'azione di controllo*
- Il controllore $\mathcal{C}$ quindi è un sistema dinamico e comprendere $H(s)$ e $K(s)$, avente una sua relazione ingresso uscita: $$  U(s)=-K(s)Y(s)+H(s)Y^{\text{o}}(s)=\underbrace{\begin{bmatrix} -K(s)  & H(s) \end{bmatrix}}_{\text{funzione trasferimento}}\begin{bmatrix} Y(s) \\ Y^{\text{o}}(s) \end{bmatrix} $$
> il controllore prende in ingresso il riferimento e l'uscita e genera il segnale $u$ attraverso la funzione di trasferimento

