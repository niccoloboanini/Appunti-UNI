### ESEMPIO: CONTROLLO DI POSIZIONE
- L'uscita è rappresentata dalla posizione del carrello $y(t)$
- L'ingresso (da controllare) è la spinta da dietro $u$
- Esiste l'attrito (viscoso) $b$
- Il carrello ha massa $M$

Si vuole portare il carrello in una posizione desiderata $Y_{0}$ con il controllo $u$ a partire da una certa posizione di partenza $y(0)$
![[Pasted image 20220611125657.png|300]]
Dobbiamo quindi far accadere che: $$ \lim_{t \to \infty} y(t) \approx Y_{0} $$
Supponiamo di aver accesso allo stato per agire sulla legge del controllo
- Lo stato è come al solito: composto da due componenti $x(t)=\begin{bmatrix} x_{1}(t) \\ x_{2}(t) \end{bmatrix}=\begin{bmatrix} y(t)  \\ \dot y(t) \end{bmatrix}=\begin{bmatrix} \text{posizione}  \\ \text{velocita'} \end{bmatrix}$
	- Conoscere lo stato significa sapere a ogni istante $t$ la posizione e la velocità del carrello

Sappiamo già per questo sistema che:
(funzione di trasferimento in cui si vuole ricavare l'uscita, infatti $C=[1 \ \ 0]$)
![[Pasted image 20220611130253.png|500]]

Sappiamo per le specifiche di progetto che:
$$
u(t) = -F x(t) + Hy^{o}(t)
$$
- Il guadagno in feedback $F$ avrà la stessa dimensione del vettore di stato, quindi: $F=\begin{bmatrix} f_{1} & f_{2} \end{bmatrix}$
- $H$ invece è uno scalare (sistema SISO)
Totale: $3$ parametri da controllare $\to f_{1},f_{2},H$ 

#### PRIMO PASSO: polinomio caratteristico a ciclo chiuso (specifica 1)
![[Pasted image 20220611131014.png|600]]
Come si nota, abbiamo un polinomio a ciclo chiuso in cui possiamo agire direttamente sui parametri moltiplicativi alla variabile di riferimento $s$. In questo modo posso arbitrariamente gestire la stabilità perché posso modificare gli zeri (ovvero i poli della funzione di trasferimento a ciclo chiuso in questo caso)
- Se avessimo usato il polinomio ad anello aperto, avremmo ottenuto $$ \varphi(s) = s^{2}+s $$ su cui non avrei potuto far niente se non concludere che veniva un sistema marginalmente stabile (osservando gli zeri)
- Adesso invece con quelli che ho rinominato $a_{1}^{*}$ e $a_{2}^{*}$ posso regolarmi, perché dipendono da $f_{i}$ ovvero gli elementi della matrice $F$ di controllo/guadagno in feedback. Posso rendere il sistema *asintoticamente* stabile

Basta applicare il criterio algebrico di Cartesio a nostro favore, infatti basta che i coefficienti $a_{1}^{*}$ e $a_{2}^{*}$ siano entrambi positivi:
$$
\begin{cases}a_{1}^{*} > 0  \\a_{2}^{*} > 0\end{cases}\Rightarrow
\begin{cases}1+f_{2} > 0  \\f_{1} > 0 \end{cases}\Rightarrow
\boxed{\begin{cases}f_{2} > -1  \\f_{1} > 0 \end{cases}}
$$
Questi sono quindi i guadagni tali da ottenere *poli con parte reale minore di zero* e rispettare la specifica $1$
- Poi per la specifica $3$ questi poli dovranno essere posizionati in un certo modo sul semipiano sinistro così da ottenere un transitorio che scompare rapidamente

#### specifica 2
Applico la formula per trovare $H$:
![[Pasted image 20220611145629.png|400]]
Dove si nota che $H$ dipende da $f_{1}$ che avevamo trovato precedentemente
- $H=f_{1}=1$

#### SPECIFICA 3
Vogliamo che il transitorio "scompaia" velocemente, ovvero vogliamo che l'uscita converga il prima possibile (e senza troppe oscillazioni possibilmente) al regime permanente, che corrisponde al nostro $Y_{0}$ di riferimento.
- Ancora non abbiamo visto un modo quantitativo per soddisfare questa richiesta, ma sappiamo in generale che dipende dalla posizione dei poli del polinomio caratteristico a ciclo chiuso. Ci saranno alcuni casi in cui abbiamo un andamento soddisfacente, e altri in cui non si rispetta questa specifica.
##### ESEMPIO 1
Sappiamo che $\varphi(s)^{*} = s^{2}+(f_{2}+1)s+f_{1}$ 
- Poniamo $f_{1}=1$ e $f_{2}=-0.9$ e vediamo che succede
- $\varphi(s)^{*}$ diventa $$ \varphi(s)^{*}=s^{2}+0.1\ s+1 $$
- Se li calcoliamo, si ottengono poli *complessi coniugati*, posizionati naturalmente nel semipiano sinistro perché abbiamo scelto $f_{1}$ e $f_{2}$ conformi alla specifica $1$.
	- Questo causa una *risposta in ciclo chiuso oscillante*
![[Pasted image 20220611150642.png|600]]
- Fisicamente l'uscita (che rappresenta la posizione del carrello) non è ottimale al nostro caso: il carrello infatti prima di arrivare alla posizione desiderata $Y_{0}=1$, va avanti e indietro a questa (arrivando anche a valori vicino a $2$). Inoltre ci mette anche diverso tempo
	- Questo accade perché abbiamo autovalori sì stabili (parte reale minore di $0$), ma sono oscillanti (complessi coniugati) e *vicino all'asse verticale immaginario*, ovvero alla zona di "confine" per l'instabilità

##### ESEMPIO 2
Cambiamo solo $f_{2}$, facendolo diventare $0$
- Cambia quindi il polinomio caratteristico a ciclo chiuso e cambiano quindi i relativi autovalori
	- In questo caso sono posizionati più lontani dalla instabilità e hanno oscillazioni minori (e ci arrivo anche più velocemente)
![[Pasted image 20220611151301.png|500]]

##### ESEMPIO 3
Cambiamo $f_{1}$ e $f_{2}$ così *autovalori in ciclo chiuso reali*
- L'andamento è non oscillante, ma *ci mette tanto tempo ad assestarmi*
	- Transitorio non oscillante :) però lento :(


#### CONCLUDIAMO LA LEGGE DEL CONTROLLO con le specifiche
Con $f_{1}>0$ e $f_{2}>-1$ e $H=f_{1}$

![[Pasted image 20220611151918.png|600]]
Abbiamo un termine che *dipende dalla posizione* (in particolare dalla differenza tra la posizione desiderata e quella in cui siamo $y^{o}-y$) e dalla *velocità* ($\dot y$) - detto proporzionale derivativo (PD)
- Sulla base di queste due informazioni progettiamo il nostro controllo (forza che agisce sul carrello) 

**Nota:** esistono anche sistemi non controllabili (in cui non c'è la possibilità ad esempio di controllare gli autovalori di $\varphi(s)^{*}$ perché gli elementi di $F$ non compaiono nel polinomio stesso o sono configurati in maniera non concorde con le condizioni da imporre per altre specifiche (ad esempio per calcolare un $H$ adatto)
![[Pasted image 20220611152532.png|600]]
- Se $r(0)=0$ abbiamo $\displaystyle H=\frac{\varphi(0)^*}{\underbrace{r(0)}_{0}}$ (impossibile)
	- Quindi quando progetto il controllo devo prestare subito attenzione a questi vincoli, altrimenti le specifiche potrebbero non essere soddisfatte
		- Per la specifica $2$ come visto è facile, basta che $r(0)\neq 0$
		- Per la specifica $1$ è più complicato, e bisogna parlare di *controllabilità* (vedi dopo)

# CONTROLLABILITA' E STABILIZZABILITA'
### ESEMPIO 1 - sistema STABILIZZABILE
##### COMMENTI
- Il sistema inizialmente è internamente instabile, infatti il polinomio caratteristico "ad anello aperto" ha zeri (che sono gli autovalori) non tutti con parte reale minore di zero (ne ha uno che vale $+2$ addirittura)
- Ci calcoliamo così il polinomio caratteristico a ciclo chiuso:
	- Calcoliamo la matrice $A^{*}=A-BF$ della dinamica in ciclo chiuso
		- Nota: $F$ è un vettore riga di dimensione $2$, perché la matrice $A$ di partenza è $2 \times 2$
	- Calcolo $\varphi(s)^{*}$ 
- Osserviamo gli autovalori ottenuti con il controllo
	- Notiamo che solo uno dei due autovalori può essere "corretto"/modificato. Esso lo chiameremo *autovalore controllabile*
		- L'altro è non controllabile perché non posso modificarlo
			- Per questo il sistema si dice *non completamente controllabile* (a differenza per esempio del carrello)
![[Pasted image 20220611180706.png|600]]
- Dato che l'autovalore controllabile è relativo proprio all'autovalore di partenza con $\text{Re}>0$, allora con opportuni valori ($f_{1}>2$) si può rendere l'autovalore con parte reale negativa, così da *rendere il sistema stabile*. 
	- Quando questo è possibile il **sistema si dice stabilizzabile**, perché con il controllo posso agire sulla stabilità del sistema stesso (modificando i valori degli autovalori)

### ESEMPIO 2 - sistema NON STABILIZZABILE
- Analogo al precedente come procedimento (infatti cambia solo un elemento della matrice $A$)
	- Abbiamo un sistema con autovalori entrambi instabili
	- Proviamo allora ad applicare il controllo (cambia solo un elemento alla fine)
	- Calcolo anche il polinomio caratteristico a ciclo chiuso
![[Pasted image 20220611180735.png|500]]
![[Pasted image 20220611175039.png|600]]
- Seppur abbia la possibilità di controllare un autovalore (e quindi rendere esso stabile), rimangono altri autovalori che non si possono in nessun modo controllare (quindi rimangono autovalori con $\text{Re}>0$ che rendono il sistema instabile nonostante il controllo)
	- In questi casi si parla di **sistema non stabilizzabile**: non esiste alcun guadagno in feedback $F$ tale da rendere il sistema in ciclo chiuso stabile (*esistono dei valori instabili non controllabili*)
![[Pasted image 20220611175405.png|200]]


## DEFINIZIONI

### AUTOVALORE CONTROLLABILE E NON
![[Pasted image 20220611175816.png]]
- Nota sulla penultima cosa: gli autovalori se controllabili li posso posizionare a piacere ma se sono complessi compaiono coniugati e li devo spostare "a coppia"
- Nota sulla cosa finale: dipende dalla matrice $A$ e dalla matrice $B$, quest'ultima mi dice infatti come il controllo agisce sul sistema (era comunque ovvio osservando che in $\varphi(s)^{*}$ compaiono entrambe le matrici citate)


### POLINOMIO CARATTERISTICO DI CONTROLLO
Dato che abbiamo partizionato l'insieme degli autovalori in due parti (controllabili e non controllabili), allora possiamo suddividere anche il polinomio caratteristico in due sotto-polinomi:
$$
\large \varphi(s) = \varphi_{c}(s) \ \varphi_{\text{nc}}(s)
$$
Dove:
![[Pasted image 20220611180804.png]]
![[Pasted image 20220611181204.png|600]]

 ## STABILIZZABILITA'
 ![[Pasted image 20220611181252.png|600]]
#### STUDIO DELLA CONTROLLABILITà / STABILIZZABILITà
- Negli esempi visti studiavamo il polinomio caratteristico in ciclo chiuso e sulla base della fattorizzazione di esso si individuavano gli zeri e si concludeva a secondo di quanto valeva la parte reale sulla stabilità.
	- Questo metodo funziona per casi specifici e relativamente semplici, come nell'esempio $2$ qui riportato:
	![[Pasted image 20220611181825.png|500]]
	- In generale però non sempre viene un polinomio facilmente "gestibile" a livello di ricerca degli zeri (autovalori).
- Per tali ragioni esiste quella che si chiama **parte controllabile del sistema**, che si può calcolare facilmente (calcolo matriciale: $(sI-A)^{-1}\ B$)
![[Pasted image 20220611182043.png]]

## PARTE CONTROLLABILE

### ESEMPIO: prendiamo un sistema non completamente controllabile
- Calcoliamo il polinomio caratteristico $\varphi(s)$ e individuiamo gli autovalori controllabili del sistema
- Operazione inversa a quello che si fa di solito: si passa dalle matrici alle equazioni di stato (ricordando che la prima componente $\dot x_{i}$ è quella associata alla i-esima riga delle matrici $A$ e $B$)
- Si associa la i-esima equazione di stato all'i-esimo autovalore: se quest'ultimo è controllabile, allora l'equazione di stato rientra nel *sottosistema controllabile $\mathcal{S}_{c}$*
	- Se l'autovalore è non controllabile, allora l'equazione rientra in *$\mathcal{S}_{\text{nc}}$, sottosistema non controllabile*, perché evolve indipendentemente dal controllo
![[Pasted image 20220611183518.png|600]]

### DIAGRAMMA A BLOCCHI
Come si nota dal diagramma a blocchi, $\mathcal{S}_{\text{nc}}$ non ha ingressi, perché tanto non è controllabile (evolve *autonomamente*) 
- Pertanto la risposta forzata, che dice come l'ingresso influenza lo stato (e vale nel dominio di Laplace $X_{f}(s) = (sI-A)^{-1} Bu(s)$), non è influenzata da $\mathcal{S}_{\text{nc}}$.

La parte invece controllabile $\mathcal{S}_{c}$ ha come autovalori gli autovalori controllabili ed è per questa ragione *influenzata dal controllo* (e quindi è non autonoma)
![[Pasted image 20220611184318.png|600]]

### ESEMPIO DI SCOMPOSIZIONE PARTE CONTROLLABILE E NON
- Nella risposta forzata si vede solo la parte controllabile

![[Pasted image 20220611184735.png|600]]
**La risposta forzata ha come unico polo rimanente quello controllabile** (possono essere eventualmente di più)
- Gli autovalori non controllabili spariscono (si cancellano) --> sono gli *autovalori nascosti del sistema*
### GENERALIZZAZIONE e CALCOLO POLINOMIO CARATTERISTICO DI CONTROLLO
**I poli controllabili del sistema sono i poli di $(sI-A)^{-1}B$**
![[Pasted image 20220611185227.png]]

#### NELL'ESEMPIO PRECEDENTE
![[Pasted image 20220611185300.png|300]]

>*in questo modo si stabilisce con un metodo preciso quali sono gli autovalori controllabili e quali no, e capire così se il sistema è stabilizzabile oppure no*
