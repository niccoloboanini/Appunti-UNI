### STABILITA' E MODI NATURALI
![[Pasted image 20220606172943.png|600]]
Quindi:
![[Pasted image 20220606173306.png|600]]
- quindi l'asse Reale del piano complesso rappresenta il confine tra stabilità e instabilità: a sinistra abbiamo convergenza (al limite limitato se consideriamo anche l'asse stesso), a destra abbiamo divergenza
- si mantiene ancora il rapporto $\text{posizione dei poli } \longleftrightarrow \text{convergenza/divergenza}$

![[Pasted image 20220606174032.png|600]]
- nota: la stabilità dipende dalla molteplicità solo nel caso particolare in cui $Re\{\lambda_{i}\} = 0$: se la molteplicità è maggiore di $1$ allora abbiamo instabilità

#### RIASSUNTO COMPLETO
![[Pasted image 20220606180835.png|600]]

Inoltre ($\text{stabilita'} \implies x_{\ell(t)}\to 0$):
![[Pasted image 20220606181322.png|500]]

### ESERCIZI: STUDIO DI STABILITA' INTERNA DEL SISTEMA
#### ESERCIZIO
- Trovo $\varphi(s)$
- Trovo gli zeri di $\varphi(s)$, ovvero gli autovalori
- Osservo la posizione degli autovalori sul piano complesso e concludo sulla stabilità/instabilità
	- Eventualmente dimostro che è vero calcolando esplicitamente i modi naturali
- Se ho molteplicità $1$ non devo calcolare $m(s)$
![[Pasted image 20220606174413.png|500]]

#### ESERCIZIO: osservo (anche) la molteplicita'
- Poli (autovalori) complessi coniugati
- Hanno molteplicità $1$ (basta fattorizzare per vederlo meglio)
- Sono al margine della stabilità (i poli sono sull'asse reale)
	- La molteplicità di $\varphi(s)$ è $1$ quindi anche $m(s)$ ha molteplicità $1$, quindi non devo calcolare l'inversa esplicitamente
	- Posso concludere subito che abbiamo modi di evoluzione limitati, quindi *stabilità marginale*
- I modi sono seno e coseno essendo i poli complessi coniugati
![[Pasted image 20220606174812.png|500]]

#### ESERCIZIO: instabilita' causata dalla molteplicita'
- Abbiamo un autovalore in $0$ con molteplicità $2$ (caso limite)
	- Sicuramente non abbiamo stabilità asintotica, ma potrebbe esserci quella marginale se $m(s)$ avesse molteplicità $1$.
	- Calcolo $m(s)$ (conti già fatti in precedenza)
		- Si scopre che $m_{1} = 2$ quindi abbiamo divergenza: esiste almeno un modo naturale divergente. Infatti abbiamo: $1, t$ --> ovvero il gradino e la rampa
![[Pasted image 20220606175100.png|500]]

#### esercizio da confrontare col precedente
- Stesso $\varphi(s)$ del caso precedente, ma differente matrice
- Calcolo l'inversa di matrice (già fatto in passato per questa matrice)
	- Si scopre che $m_{1} = 1$, quindi *stabilità marginale*. Abbiamo un solo modo di evoluzione: il gradino $1(t)$ 
![[Pasted image 20220606175249.png|500]]

---

# RISPOSTA FORZATA E FUNZIONE DI TRASFERIMENTO
## FUNZIONE DI TRASFERIMENTO
Preso un sistema LTI TC:
$$
\begin{cases} \dot x = Ax +Bu  \\ y = Cx + Du \end{cases}
$$
Sappiamo che la risposta forzata in Laplace è data da:
$$
Y_{f}(s) = \underbrace{[C(SI-A)^{-1}B +D]}_{\text{\large funzione di trasferimento}} \ U(s)
$$
**Rinominiamo la funzione di trasferimento con $G(s)$**
- Ci dice nel dominio di Laplace come si evolve in rappresentazione ingresso uscita il sistema.
- In generale $G(s)$ è una matrice, dato che $U(s)$ e $Y_{f}(s)$ sono vettori colonna
	- Ciascun elemento della matrice ci dive la relazione tra l'ingresso e l'uscita corrispondenti alla riga e alla colonna di riferimento
		- Esempio: elemento $i,\ell \longleftrightarrow \text{relazione tra } \ell \text{-esimo ingresso e } i \text{-esima uscita}$ 

*Per semplicità consideriamo sistemi* **SISO**, quindi $U(s)$ e $Y_{f}(s)$ sono scalari. Avremo $Y_{f}(s) = G(s) U(s)$, quindi:
$$
\large \boxed{G(s) = \frac{b(s)}{a(s)}}
$$
- con i relativi *poli del sistema* (zeri di $a(s)$) e gli *zeri del sistema* (zeri di $b(s)$)
- $G(s)$ è una *funzione razionale*, infatti 
![[Pasted image 20220606183316.png|500]]


#### ESEMPIO SISTEMA MECCANICO
- Consideriamo finalmente anche l'ingresso $u(s)$, ovvero la forza che spinge il carrello
![[Pasted image 20220606182752.png|400]]
Passi:
- calcolo $\varphi(s)$
- calcolo l'aggiogata di $(sI-A)$
- sostituisco tutto nella definizione di $G(s)$
 ![[Pasted image 20220606183204.png|500]]
 - dove per comodità abbiamo riscritto $G(s)$ come: $$ G(s) = \frac{r(s)}{\varphi(s)}+D $$
 - Cfr. Con appunti dopo --> (non ci sono autovalori nascosti: $\varphi(s) = a(s)$)
	 - se invece della posizione prendiamo come uscita la velocità si ottiene (considerando lo stesso sistema):
	 ![[Pasted image 20220606184618.png|400]]
		 - cambia l'uscita --> cambia la funzione di trasferimento (essa non è una proprietà intrinseca, dipende dalle manovre che facciamo dall'esterno su di essa)
		 - scompare l'autovalore in $0$
## RELAZIONE POLI - AUTOVALORI
Abbiamo detto che:
$$
G(s) = \frac{r(s)+D \varphi(s)}{\varphi(s)}=\frac{b(s)}{a(s)}
$$
- $\varphi(s)$ ha molteplicità $\mu_{i}$
Allora:
- $G(s)$ ha molteplicità $v_{i}$

Possiamo facilmente dire che: 
$$
\boxed{0 \leq v_{i} \leq \mu_{i}}  \quad , \quad \text{perchè potrebbero esserci semplificazioni}
$$
- quindi l'**autovalore può scomparire**

Vale più in generale la seguente relazione tra le molteplicità relazione: $v_{i} \leq m_{i} \leq \mu_{i}$

Quindi: *i poli del sistema sono un sottoinsieme degli autovalori del sistema*
- Gli autovalori che non compaiono all'uscita (ma che internamente ci sono), sono detti **autovalori nascosti**
