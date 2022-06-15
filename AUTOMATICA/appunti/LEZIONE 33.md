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
Per generalizzare significa che $H$ e $K$ (guadagno in feedforward e in feedback) *non sono più scalari*, ma diventano *funzioni di trasferimento* (in modo tale da avere più margine di scelta)
Quindi:
$$
u(t) = -Ky(t)+Hy^{\text{o}}(t) \to U(s) = -H Y(s) +H Y^{\text{o}}(s) \to \boxed{U(s) = -K(s)Y(s)+H(s)Y^{\text{o}}(s)}
$$
- Viene detta *retroazione dinamica* sull'uscita (dinamica perché *il controllore diventa un sistema dinamico*, ovvero avente le sue funzioni di trasferimento)
	- Vogliamo controllare un sistema dinamico $\to$ scegliamo un controllore dinamico (stessa complessità)

### DIAGRAMMA A BLOCCHI
![[Pasted image 20220615124958.png|500]]
- $\mathcal{P}$: sistema da controllare (con accesso solo di $u$ e $y$)
- $H(s)$: funzione di trasferimento (ovvero un *filtraggio* [elaborazione] del segnale di riferimento $y^{\text{o}}$)
- $K(s)$: altro *filtro* che elabora l'uscita $y$

Sommando le due elaborazioni filtrate si genera *l'azione di controllo*
- Il controllore $\mathcal{C}$ quindi è un sistema dinamico e comprendere $H(s)$ e $K(s)$, avente una sua relazione ingresso uscita: $$  U(s)=-K(s)Y(s)+H(s)Y^{\text{o}}(s)=\underbrace{\begin{bmatrix} -K(s)  & H(s) \end{bmatrix}}_{\text{funzione trasferimento}}\begin{bmatrix} Y(s) \\ Y^{\text{o}}(s) \end{bmatrix} $$
> il controllore prende in ingresso il riferimento e l'uscita e genera il segnale $u$ attraverso la funzione di trasferimento


Il vantaggio è che, a partire da una $G(s)$ data dell'impianto $\mathcal{P}$, possiamo progettare appositamente $K(s)$ e $H(s)$ per avere il comportamento desiderato al sistema in retroazione
![[Pasted image 20220615124932.png|400]]


### SCELTA TIPICA DI H(F)
**Nota:** tipicamente si sceglie: $H(s)=H_{f}(s)K(s)$, dove $H_{f}(s)$ è un *prefisso* e $K(s)$ è un *guadagno in feedback*

- Quindi $$ U(s) = -K(s)Y(s)+H_{f}(s)K(s)Y^{\text{o}}(s)=K(s)[H_{f}(s)Y^{\text{o}}(s)-Y(s)] $$
Lo schema di controllo diventa:
- Riferimento in ingresso $y^{\text{o}}$
- Lo elaboro con il prefisso $H_{f}(s)$, ottenendo: $H_{f}(s)Y^{\text{o}}(s)$
- Sottraggo l'uscita $y$, ottenendo la parentesi quadra $[H_{f}(s)Y^{\text{o}}(s)-Y(s)]$
- Elaboro tale risultato con il guadagno in feedback $K(s)$, cos' da ottenenere *l'uscita di controllo $u$*
- Essa entrata nell'impianto $\mathcal{P}$ (processo) che elabora l'uscita $y$

Schema molto usato in ambito industriale (cambia rispetto a quelle viste prima solo la struttura interna che porta una formula di $H(s)=H_{f}K(s)$)
![[Pasted image 20220615125836.png|500]]

**Si distinguono $2$ casi:**
1) il prefisso non c'è, ovvero $H_{f}(s)=1$, quindi: $$  U(s) =K(s)[Y^{\text{o}}(s)-Y(s)]  $$![[Pasted image 20220615130012.png]]
È un sistema di controllo **a un grado di libertà** (basta progettare una sola funzione di trasferimento $K(s)$)
- L'azione di controllo $u$ dipende solo dell'errore d'inseguimento $y^{\text{o}}-y$

2) Se $H_{f}(s)\neq 1$ allora il sistema di controllo è a **due gradi di libertà**, quindi dovremo progettare due sistemi di controllo che sono dipendenti dal riferimento e dall'uscita secondo la legge di $U(s)$

## SISTEMA A CICLO CHIUSO
Si arriva a un risultato molto simile analogo a quello della retroazione algebrica già vista in precedenza (lezione scorsa), in cui avevamo:
![[Pasted image 20220615145133.png]]

Adesso invece cambia il nostro controllo $\mathcal{C}$, ma il risultato della funzione di trasferimento è lo stesso, solo che ci inseriamo le funzioni $H(s)$ e $K(s)$ al posto delle costanti $H$ e $K$:
![[Pasted image 20220615145251.png|400]]

Ponendo $H_{f}(s)$ costante (vedremo che basterà per le mie specifiche), ovvero $H_{f}$, si ottiene $H(s) = H_{f}(s)K(s)=H_{f}K(s)$, quindi:
$$
\boxed{G^{*}_{y^{\text{o}}y}(s)=\frac{K(s)G(s)}{1+K(s)G(s)}H_{f}}
$$, che rappresenta la *funzione di trasferimento in ciclo chiuso* che utilizzeremo per la retroazione dinamica per l'uscita

#### RISCRITTURA IN TERMINI DI POLINOMI
Possiamo riscrivere il risultato ottenuto in termini di polinomi invece di $G(s)$ e $K(s)$.

(Nota: simile a quanto già visto: ![[Pasted image 20220615145738.png]])

Quindi:
- Posso riscrivere $G(s)$ come rapporto di polinomi (con $b(s)$ e $a(s)$ polinomi dati dal problema)
- Posso riscrivere $K(s)$ come rapporto di polinomi (con $q(s)$ e $p(s)$ **polinomi scelti da me**)
(semplificazione: moltiplico per $p(s)$ e $a(s)$)
![[Pasted image 20220615150635.png|600]]

Scegliendo $q(s)$ e $p(s)$ posso associare i poli in ciclo chiuso che mi servono

Note:
- al numeratore rimangono gli zeri di $G(s)$ e $K(s)$ [quindi cambia poco]
- al denominatore abbiamo un nuovo polinomio dei poli in ciclo chiuso, che dipende da $a(s)$, $b(s)$, $q(s)$, $p(s)$
	- per questo di rinomina il denominatore con $a^{*}(s)$
	- la cosa buona adesso è che possiamo agire su $p(s)$ e $q(s)$ per modificare i poli come vogliamo (abbiamo più gradi di libertà sul polinomio)

### POLINOMIO CARATTERISTICO IN CICLO CHIUSO
Per il polinomio caratteristico in ciclo chiuso, si sottolinea che la parte di $\varphi_{h}(s)$ rimane inalterata (perché come detto non si modificano i poli nascosti). Discorso diverso invece per $a(s)$, che diventa $a^{*}(s)$. Quindi:
$$
\overbrace{\varphi(s)=\varphi_{h}(s)a(s)}^{\Large \text{anello aperto}} \implies \overbrace{\varphi^{*}(s) =\varphi_{h}(s)a^{*}(s)=\varphi_{h}(s)\ [p(s)a(s)+q(s)b(s)]}^{\Large \text{ciclo chiuso}}
$$

##### RIASSUMENDO
![[Pasted image 20220615151429.png]]

Quindi per il progetto dovremo costruire appositamente per rispettare le specifiche:
- $q(s)$, $p(s)$   (specifica $1$ e $3$)
- $H_{f}$  (specifica $2$)

Procedimento simile solo che adesso per progettare $K(s)$ abbiamo un *rapporto di polinomi* (quindi è un po' più complesso)

## ESEMPIO (quello che non riuscivamo a stabilizzare)
- Non poteva essere stabilizzato con la retroazione algebrica $u=-Ky+Hy^{\text{o}}$
- Ci proviamo allora con le retroazione dinamica: $U(s)=K(s)[H_{f}Y^{\text{o}}(s)-Y(s)]$
	- Scegliamo $K(s)$ come rapporto di polinomi di primo grado (così da avere $3$ parametri liberi $p_{0},q_{0},q_{1}$)
	- Riscrivo $\varphi^{*}(s)$ e vedo un po'
	- Impongo coefficienti $\varphi^{*}(s)$ in modo arbitrario (ora ne ho la possibilità)
		- Così da avere le radici (non nascoste) posizionate dove vogliamo
![[Pasted image 20220615152449.png|600]]
- Posizioniamo i poli in ciclo chiuso in $-1,-10,-10$ (numeri scelti)
	- Basta fattorizzare $\varphi^{*}(s)$ per capire la forma in generale
	- Vado a eguagliare i coefficienti

![[Pasted image 20220615152735.png|600]]

Possiamo inserirli in $K(s)$ così da ottenere:
![[Pasted image 20220615152844.png]]

Da cui, la funzione di trasferimento in ciclo chiuso:
![[Pasted image 20220615152914.png]]

Per la specifica $2$, imponiamo inseguimento costante uguale a $1$, ovvero:
![[Pasted image 20220615153011.png]]

Quindi possiamo esplicitare la legge di controllo in Laplace
![[Pasted image 20220615153135.png]]


## SCELTA DELL'ORDINE DEL CONTROLLORE
Siano
$$
G(s) = \frac{b(s)}{a(s)}
$$e
$$
K(s) = \frac{q(s)}{p(s)}  \quad , \quad \text{con grado }p(s) = \text{grado }q(s)=n_{K} \textbf{ ordine del controllore}
$$
Allora abbiamo **$2n_K+1$ parametri liberi**

>Se scegliamo $n_{K} \geq \text{grado }a(s)-1$ allora possiamo scegliere i coefficienti di $a^{*}(s)$ arbitrariamente per garantire il posizionamento che vogliamo nei poli a ciclo chiuso (quindi abbiamo un controllore adatto)

- Come nell'esempio precedente: avevamo $\text{grado }a(s)=2$ quindi abbiamo scelto $K(s)$ come rapporto di polinomi di primo grado (grado $n_K=a(s)-1=2-1=1$)


