### TRATTAZIONE FORMALE: IPOTESI SEMPLIFICATIVE
Supponiamo che:
- Il sistema sia completamente controllabile (così che si può assegnare liberamente tutti gli autovalori in ciclo chiuso)
	- Posso scegliere come voglio i coefficienti di $\varphi^{*}(s)$ (polinomio caratteristico a ciclo chiuso) - con il vincolo che il primo sia $s^{n} \cdot \varphi^{*}_{n}$, con $\varphi^{*}_{n}=1$ (monico)
- $r(s)$ ha tutte radici con parti reali minori di zero ($r(s) = CAdj(sI-A)B$, va al numeratore di $G^{*}_{y^{o}\ y}(s)$)
- - In questo modo, essendo stabile ci sono possibili semplificazioni tra numeratore e denominatore di $G^{*}_{y^{o}\ y}(s)$

Abbiamo:
$$
\large \varphi^{*}(s) = s^{n} + \varphi^{*}_{n-1}s^{n-1} + \dots + \varphi^{*}_{1}s + \varphi^{*}_{0}
$$

Ora:
- $r(s)$ è un generico polinomio di grado $m$, con $m<n$ tale che: $$ r(s)=r_{m}s^{m}+r_{m-1}s^{m-1}+\dots+r_{1}s+r_0 $$
- $\varphi^{*}(s)$ è un polinomio di grado $n$, che scegliamo di questo tipo: $$ \varphi^{*}(s)=\frac{\overbrace{r(s)}^{\text{grado } m}}{r_{m}}\ \overbrace{a^{*}(s)}^{\text{grado }n-m} = \dots = \left(s^{m}+\frac{r_{m-1}}{r_{m}}+\dots+\frac{r_{0}}{r_{m}}\right)a^{*}(s) $$
	- Dove $a^{*}(s)$ è un polinomio scelto da me (monico)
	- Dividendo per $r_{m}$ diventa monico anche $r(s)$ 

Tutto questo è comodo perché:
$$
G_{y^{o}\ y}^{*}(s) = \frac{r(s)}{\varphi^{*}(s)}H= \frac{\cancel{r(s)}}{\frac{\cancel{r(s)}}{r_{m}}a^{*}(s)}H=\frac{r_{m}}{a^{*}(s)}H
$$
- Abbiamo i poli esclusivamente in $a^{*}(s)$, che è come detto un polinomio scelto appositamente e infine due termini costanti $r_{m}$ e $H$

Per garantire la specifica $2$, si sceglie $\displaystyle H=\frac{a^{*}_{0}}{r_{m}}$ (così che $G_{y^{o}\ y}^{*}(0)=1$)
E allora si giunge alla forma:
$$
\large \boxed{G_{y^{o}\ y}^{*}(s)=\frac{a^{*}_{0}}{a^{*}(s)}}
$$
- Con $a^{*}(s) =s^{n-m}+a^{*}_{n-m-1}s^{n-m-1}+\dots+a^{*}_{0}$ scelto da me (monico) - utile per dare l'andamento che vogliamo alla risposta a gradino a ciclo chiuso


Pertanto la risposta forzata al gradino in ciclo chiuso che abbiamo già visto in precedenza diventa:
![[Pasted image 20220614113418.png]]


> [!hint] Importante: stabilità di $r(s)$
>**Nota bene**: il polinomio **$r(s)$** si semplifica (cancella) $\iff$ $r(s)$ è stabile (altrimenti poi diventerebbe instabile anche $\varphi^{*}(s)$)
![[Pasted image 20220614113705.png]] 

Nell'esempio di progetto precedente avevamo $n-m=1$ 
- In questi casi la funzione di trasferimento si dice del **I ordine** ed è della forma:
- $$
G^{*}_{y^{o}\ y}(s)=\frac{a^{*}_{0}}{s+a^{*}_{0}}  \quad , \quad\text{ con } a^{*}_{0}>0 \text{ numero scelto da me}
$$
- Tale funzione di trasferimento dà luogo a una risposta al gradino $y^{o}(t)$ del tipo:
![[Pasted image 20220614114456.png|400]]
	- Dove l'esponenziale $e^{-a^{*}_{0}t}$ dipende dalla posizione del polo che abbiamo assegnato dove vogliamo per garantire una convergenza a $0$ di tale esponenziale sufficientemente alta
![[Pasted image 20220614114516.png]]

- la costante di tempo è utile per capire in quanto tempo si arriva alla risposta a regime
	- il tempo di assestamento in particolare mi dice esattamente in quanto tempo di arriva in un intorno sufficientemente piccolo della risposta a regime

**Se il grado relativo fosse $2$**, ovvero $n-m=2$ si ottiene:
![[Pasted image 20220614115714.png|600]]
dove infatti:
![[Pasted image 20220614115641.png|500]]
- lo smorzamento e la pulsazione naturale sono stati introdotti per caratterizzare il sistema perché ci daranno maggiori informazioni su esso

In particolare:
- al variare dello smorzamento abbiamo poli reali oppure immaginari
> Se i poli sono reali abbiamo modi di evoluzione non oscillanti. Quindi la funzione al gradino al ciclo chiuso ha un andamento monotono quindi senza oscillazioni (che è buono per la specifica $3$)

> Nel caso sottosmorzato abbiamo comunque stabilità asintotica ($\text{Re}<0$), però è presente la parte immaginaria quindi ci saranno modi di evoluzione oscillanti

![[Pasted image 20220614120332.png]]

Da cui (evitando tutti i conti) si ottiene per il caso *sottosmorzato*:
- dove in rosso abbiamo il transitorio, infatti:
	- compare l'esponenziale reale (velocità di convergenza relativa ai poli)
	- compare anche la parte immaginaria (velocità delle oscillazioni)
- in blu invece il regime permanente (a gradino)
![[Pasted image 20220614120703.png|600]]

**Nota:** Smorzamento piccolo $\to$ tante oscillazioni
- il transitorio non converge se abbiamo poli puramente immaginari
![[Pasted image 20220614121913.png|600]]
- compaiono *sovra elongazioni* (supera il valore del permanente) 
![[Pasted image 20220614121121.png|600]]
- di quanto supero in percentuale il valore asintotico della risposta a regime
	- dipende dallo smorzamento: tanto più è piccolo, tanto più è grande la sovraelungazione (vedi grafico)
		- se lo smorzamento vale più di $1$ come già detto non c'è sovraelungazione
Valgono le formule:
![[Pasted image 20220614121341.png]]
- dove il tempo di assestamento dipende come già detto dalla parte reale dei poli: tanto più essi sono lontani dall'asse immaginario, tanto più è veloce (piccolo) il tempo di assestamento del transitorio


Nei progetti si assegnano $T_{a,\large \upvarepsilon}$ e $S$  e si determinano la posizione dei poli (smorzamento e pulsazione naturale) per soddisfare le specifiche
![[Pasted image 20220614122015.png|600]]

#### CASO GENERALE $n-m>2$
Ci si cerca di ricondurre ai casi precedenti fattorizzando $a^{*}(s)$, dopo aver posizionato i *poli dominanti* e gli altri poli con alta frequenza (lontani dall'asse immaginari), così che la funzione dipende solo dai ($2$) poli dominanti (asintoticamente - perché hanno transitorio molto rapido)
![[Pasted image 20220614122413.png|500]]


##### LIMITI FISICI
Se vogliamo avere un transitorio molto rapido (ad esempio nell'ordine dei millisecondi), è necessario scegliere un guadagno $F$ molto grande $\to$ guardando la legge di controllo però ci si accorge che non possiamo scegliere $F$ arbitrariamente grande perché l'azione di controllo diventerebbe molto elevata (al punto da essere ingestibile)
- Nella pratica si sceglie un compromesso
	- Esempio: tranvia $\to$ si sceglie una via di mezzo per portare il mezzo in una certa posizione in un tempo relativamente buono per i miei scopo senza "sovraccaricare" il controllo
![[Pasted image 20220614122943.png|500]]

Un modo alternativo per scegliere $F$ (invece di posizionare i poli in modo da avere transitorio soddisfacente) è il *controllo ottimo*
- Tiene conto del compromesso sopra descritto (transitorio rapido pur rientrando nei limiti fisici)
	- Idea: tenere basso l'errore d'inseguimento e l'azione di controllo - sulla base di un parametro $\rho$ a seconda delle mie esigenze (se preferisco avere un po' di più di errore o di controllo)
![[Pasted image 20220614123319.png|500]]

### ZERI INSTABILI (cioè se r(s) non è stabile)
- ci sono zeri non cancellabili - rimangono nella funzione di trasferimento a ciclo chiuso
- abbiamo una sottoelongazione (perché avremo un polo con $\text{Re}>0$)
![[Pasted image 20220614123615.png|400]]
- come si vede c'è uno zero al numeratore in $1$

---

# CONTROLLO IN RETROAZIONE SULL'USCITA
- Fin ora abbiamo visto il controllo in retroazione sullo stato, supponendo nella maggior parte dei casi che tutto il vettore $x(t)$ dello stato fosse accessibile per il controllo
- Supponiamo adesso che sia accessibile *solo l'uscita*, ovvero abbiamo una *informazione parziale*
	- cioè possiamo osservare solo l'uscita dello stato, senza osservare la sua conformazione interna (appare come una "scatola chiusa")

## OSSERVABILITA'
Proprietà che descrive cosa stiamo osservando del comportamento interno del sistema osservando solo l'uscita $y$
- In figura, $x$ è lo stato interno del sistema, che supponiamo di non poter osservare (nascosto)
![[Pasted image 20220614154233.png|200]]
- Proprietà duale della controllabilità, che ci diceva come l'ingresso influenzava l'uscita

## EVOLUZIONE LIBERA E FORZATA
Sappiamo già che per un sistema LTI TC (supponendo $D=0$):
$$
\begin{cases} \dot x = Ax +Bu  \\ y = Cx + Du \end{cases}
$$
Possiamo trovare la soluzione algebricamente passando da Laplace, e scomponendo le trasformate in evoluzione libera ed evoluzione forzata, sappiamo che:
![[Pasted image 20220614154700.png|500]]
- Se torniamo nel tempo, sappiamo che $\mathcal{L}^{-1}\{X_{\ell}(s)\} = \mathcal{L}^{-1}\{(sI-A)^{-1}x(0)\} = e^{At}x(0)$, ovvero dalla evoluzione libera dello stato si vedono tutti i modi naturali del sistema (basta antitrasformare)
	- e attraverso il polinomio minimo $\varphi(s)$ vedo gli autovalori del sistema che sono gli zeri

- l'evoluzione forzata invece *dipende soltanto dalla parte controllabile del sistema*, infatti: $$ X_{f}(s) = (sI-A)^{-1}BU(s) $$
	- se prendiamo i poli di $(sI-A)^{-1}B$ essi sono gli *autovalori controllabili* del sistema (ovvero gli zeri di quello che poi abbiamo definito come $\varphi_{\text{c}}(s)$)
		- Questo perché **alcuni autovalori si cancellano moltiplicando per $B$** (infatti nell'evoluzione libera questa moltiplicazione per $B$ non c'è e vediamo tutti gli autovalori)
		- Abbiamo poi definito $\varphi_\text{nc}(s)$ come il complementare di $\varphi_{\text{c}}(s)$

#### L'USCITA E I SUOI AUTOVALORI OSSERVABILI
Guardando l'uscita $Y(s)$ invece, osserviamo che abbiamo una **premoltiplicazione per la matrice $C$**.
- Tale operazione dal punto di vista matematico, può andare a *cancellare alcuni autovalori* che non compariranno come autovalori dell'*evoluzione libera* $C(sI-A)^{-1}$ dell'uscita
	- Quindi guardando l'uscita *non si vedono tutti gli autovalori*, ma rimangono soltanto i cosiddetti **autovalori osservabili**
		- Quelli che si cancellano sono detti autovalori non osservabili
![[Pasted image 20220614160031.png|600]]

## POLINOMIO CARATTERISTICO DI OSSERVAZIONE
Allo stesso modo dell'evoluzione forzata dello stesso, definiamo una nuova fattorizzazione del polinomio caratteristico: $$ \large \varphi(s) = \varphi_{\text{o}}(s) \ \varphi_{\text{no}}(s) $$
Dove:
![[Pasted image 20220614160222.png|600]]

#### TIPOLOGIE DI AUTOVALORI
![[Pasted image 20220614160426.png|200]]
Gli autovalori quindi possono essere di $4$ tipi:
- osservabili
- controllabili
- osservabili e controllabili
- né osservabili né controllabili
## FUNZIONE DI TRASFERIMENTO
Dato che abbiamo: $$ Y_{f}(s) = \underbrace{C(sI-A)^{-1}B}_{\large G(s)}\ \ U(s) $$
- gli autovalori che rimangono sono quelli che non si cancellano né moltiplicando per $C$ (quindi controllabili) né moltiplicando per $B$ (quindi osservabili)
- **Perciò quelli che rimangono sono sia osservabili che controllabili**

Pertanto, dato che i poli di $G(s)=C(sI-A)^{-1}$ sono i *poli del sistema* vale la seguente: $$ \large \{ \text{Poli del sistema} \} = \{ \text{Autovalori controllabili}  \}  \cap \{ \text{Autovalori osservabili}\} $$
Nei sistemi siso, $G(s)$ come sappiamo ha una forma semplice: $$ G(s) = \frac{b(s)}{a(s)} $$
- quindi i poli del sistema sono gli zeri di $a(s)$

Quindi:
- evoluzione libera stato $\to$ tutti gli autovalori come poli
- evoluzione forzata stato $\to$ solo autovalori controllabili (resistono alla moltiplicazione per $B$)
- evoluzione libera uscita (risposta libera) $\to$ solo autovalori osservabili (resistono a moltiplicazione per $C$)
- evoluzione forzata uscita (risposta forzata) $\to$ solo autovalori sia osservabili che controllabili (resistono a moltiplicazione per $B$ e per $C$) 

## AUTOVALORI NASCOSTI
In rosso (relativi a perdita di osservabilità, controllabilità o entrambe):
![[Pasted image 20220614161717.png|600]]

> Quindi nella relazione ingresso-uscita (passaggio da $u$ a $y$ attraverso il sistema), quello che si vede alla fine su $y$ è solo la parte **controllabile** (quindi può essere modificata dal controllo) e **osservabile** (perché si vede in uscita)
- Il resto è nascosto

Abbiamo come mostrato una nuova fattorizzazione del polinomio (caso siso): $$ \varphi(s) = a(s) \ \varphi_{h}(s) \implies \varphi_{h}(s) = \frac{\varphi(s)}{a(s)}$$
Fattorizzazioni viste finora (a seconda della proprietà che vogliamo):
![[Pasted image 20220614162640.png|250]]
