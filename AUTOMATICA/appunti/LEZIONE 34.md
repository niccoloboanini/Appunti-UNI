## RIASSUNTO E LINEE GUIDA
![[Pasted image 20220615160105.png]]
#### linee guida:
1) capisco se il problema è ben posto o meno
2) se è ben posto scelgo controllore con $n_{K} \underbrace{\geq}_{=} \text{grado }a(s)-1$
3) scelgo $H_{f}$ applicando la formula
![[Pasted image 20220615160355.png|600]]

## COSA VUOL DIRE APPLICARE UNA RETROAZIONE DINAMICA SULL'USCITA
- Cerchiamo di capire **nel dominio del tempo** cosa stiamo facendo

Supponendo $K(s)$ rapporto di polinomi di primo grado
![[Pasted image 20220615160607.png|500]]
Andiamo quindi ad **antritrasformare**:
- moltiplicare per $s$ in Laplace equivale a derivare nel tempo (se avessimo un controllore di ordine $100$ allora avrei la derivata centesima)
- applico linearità
![[Pasted image 20220615160738.png]]
- cambiando la notazione per la derivata, si giunge all'equazione differenziale:
![[Pasted image 20220615160914.png]]

Quindi il segnale di controllo viene calcolato risolvendo una equazione differenziale. In altre parole:
> il segnale di controllo è l'uscita di un sistema dinamico avente una relazione ingresso-uscita definita da una equazione differenziale i cui coefficienti dipendono dai parametri di progetto e sono $p_{0},q_{0},q_{1},\dots,H_{f}$

### COME SI RISOLVE?
Si discretizza il sistema:
- Convertiamo l'equazione differenziale in una equazione alle differenze (ad esempio applicando il Metodo di Eulero come abbiamo visto)
	- oppure si possono utilizzare delle funzioni in MATLAB/Python che eseguono la conversione con un certo passo di campionamento che diamo in ingresso

Quindi ci basiamo su una **conversione** da analogico a digitale (per poter implementare il problema ad esempio sul computer) dell'uscita $y$ e poi eseguiamo una conversione da digitale ad analogico solo dopo aver fatto tutte le operazioni per avre un ingresso $u$ da dare a $\mathcal{P}$
![[Pasted image 20220615162007.png]]

Per eseguire D/A si utilizza nei casi base il mantenitore a tempo discreto (a zero)
![[Pasted image 20220615162056.png]]

---

# CONTROLLORI PID
- "Proporzionale Integrale Derivata"
- Utilizzati in ambito industriale (struttura semplice)

Sia
$$
U(s) = K(s) \ [Y^{\text{o}}(s)-Y(s)]
$$
la legge di controllo in retroazione dinamica
Andiamo a **scegliere $K(s)$ in modo prefissato**, invece di sceglierlo col metodo visto fin ora (rapporto di polinomi di grado sufficientemente elevato)
- scegliamo dei parametri che mi garantiscono un comportamento soddisfacente (*tecniche di taratura*)
- Legge di controllo *semplice* (anche se non funziona sempre, ma in casi semplici funziona e in casi semplici si applica bene)

La *struttura prefissata* è dipendente da **3 parametri** di progetto (che dobbiamo scegliere noi):
- $K_{P}$
- $K_I$
- $K_D$

### NEL TEMPO
Nella forma più semplice il PID ha un *solo grado di libertà* (quindi l'azione di controllo dipende dall'errore d'inseguimento $y^{\text{o}}(t)-y(t)$)
Il PID è dato dalla *combinazione* di $3$ *azioni*:
- Proporzionale (tanto più grande quanto mi allontano dal valore di riferimento)
- Integrale (integrale valore di riferimento)
- Derivata (derivata valore di riferimento)
![[Pasted image 20220615163043.png|500]]

### IN LAPLACE
In maniera equivalente, il PID si può vedere anche nel dominio di Laplace
(integrare: dividere per $s$ || derivare: moltiplicare per $s$)
![[Pasted image 20220615163418.png]]Dove nell'ultimo passaggio è stata evidenziata quella che è la **funzione di trasferimento $K(s)$**, che successivamente è stata riscritta in modo più semplice facendo il mcm: $$ \boxed{K(s) = \frac{K_{D}s^{2}+K_{P}s+K_I}{s} }$$, che rappresenta il **PID ideale**, perché è una funzione *impropria* (grado num $>$ grado den)

- *Non è possibile realizzare nella realtà tale $K(s)$ ideale*
	- Il problema è causato dall'azione derivativa $K_{D}$ che porta un termine di grado più elevato. Inoltre è irrealizzabile la derivata perché dovremmo conoscere l'immediato futuro per esplicitarla correttamente..

### PID REALE
Nella pratica si implementa il **PID reale**
- Si aggiunge un polo al denominatore
$$
 \Large \boxed{K(s) = \frac{K_{D}s^{2}+K_{P}s+K_I}{s(1+s\tau)}}  \quad , \quad \tau>0
$$
- in questo modo: grado numeratore $=$ grado denominatore
![[Pasted image 20220615164233.png]]
- Prima si progetta come se avessimo il caso ideale, poi si aggiunge un polo con $\tau$ sufficientemente piccolo così da soddisfare le specifiche di controllo
	- $\tau$ piccolo $\equiv$ avere un polo posizionato "lontano" dall'asse immaginario e sul semipiano sinistro così da avere un transitorio rapido (che asintoticamente non influenza il controllore)



## RUOLO DELLE 3 AZIONI

### AZIONE PROPORZIONALE
Si cerca di *correggere* il segnale di controllo limitando l'errore d'inseguimento
- Nota: se l'errore d'inseguimento è $0$, allora $K_P=0$ (no azione proporzionale)
![[Pasted image 20220615170153.png|400]]

### AZIONE DERIVATIVA
Si cerca di *anticipare* il trend, ovvero prevedere quello che succede sull'uscita
![[Pasted image 20220615165810.png]]
Se abbiamo una situazione del genere, $y$ una volta raggiunto $y^{\text{o}}$ continua a crescere se non abbiamo una azione di controllo derivativa, che appunto interviene cercando di adattarsi alla situazione:
- Quando $y$ arriva a $y^{\text{o}}$ si corregge, perché in prospettiva l'uscita tende a crescere
	- Nella realtà come detto non è del tutto realizzabile perché appunto dovremmo cercare di prevedere il (prossimo) futuro
- Nota: l'azione proporzionale non mi aiuta perché mi fa crescere $y$ prima di $y^{\text{o}}$, ma una volta raggiunto tale valore, l'azione proporzionale vale $0$
![[Pasted image 20220615170211.png|400]]

### AZIONE INTEGRALE
Utile per garantire la specifica $2$ (inseguimento perfetto del riferimento costante), senza la necessità di avere un (pre)filtro $H_{f}$, che impostiamo a $1$
- Non c'è bisogno del filtro perché la specifica $2$ è già garantita dalla sola azione integrale
Inoltre, se il sistema è affetto da *disturbi costanti*, allora l'azione integrale va ad annullare tali effetti
![[Pasted image 20220615170431.png|400]]


## LEGGE DI CONTROLLO CON AZIONE INTEGRALE
L'azione integrale introduce un polo in $0$ nella funzione di trasferimento del controllore (cfr. conti d'introduzione)
Quindi in generale:
![[Pasted image 20220615170729.png]]
Questo perché $$ K(s) = \frac{q(s)}{p(s)} = \frac{q_{nk}s^{nK}+\dots+q_{1}s+q_{0}}{s^{nK}+\dots+p_{1}s}  $$
, quindi per avere un polo il denominatore si deve annullare in zero (vero quando il polinomio al denominatore non ha il termine noto)

Andiamo a capire qual è l'effetto dell'azione integrale sul sistema.
### EFFETTO DI UN DISTURBO SUL SISTEMA IN CICLO CHIUSO
![[Pasted image 20220615173558.png|400]]
- Il disturbo $d$ agisce in ingresso. Cosa cambia nel sistema?
> Avere un disturbo significa avere nel sistema un **nuovo ingresso**
- L'ingresso classico è corrotto da un disturbo $d$

Quindi il sistema in ciclo chiuso ora ha $2$ ingressi:
- Il riferimento $y^{\text{o}}$ e il disturbo $d$

Si cerca di capire l'evoluzione dell'uscita per il sistema in ciclo chiuso
- Si aggiunge il disturbo ai conti già fatto
![[Pasted image 20220615173906.png]]

Si sono ottenute **$2$ funzioni di trasferimento**, perché ci sono due ingressi e una uscita:
- Una è quella già vista (con $H_{f}=1$)
- L'altra invece è la funzione di trasferimento tra l'ingresso e l'uscita: ovvero come il disturbo agisce sull'uscita, che chiamiamo $G^{*}_{dy}$
![[Pasted image 20220615174052.png]]

Le possiamo riscrivere in termini di **polinomi** come segue:
![[Pasted image 20220615174204.png|600]]
- cambia solo il numeratore (in un caso abbiamo $q(s)$ e in un caso $p(s)$)
	- Questo causa dei cambiamenti per la risposta in ciclo chiuso

### REGIME PERMANENTE
- Vediamo come varia la risposta in ciclo chiuso

Supponiamo riferimento e disturbo costanti (a gradino)
$$
y^{\text{o}}(t)=Y_{0}\ 1(t)  \quad , \quad d(t)=D_{0}\ 1(t)
$$
Se abbiamo stabilità asintotica in ciclo chiuso del controllore, allora sappiamo che il sistema a ciclo chiuso converge al regime permanente, che provo a calcolare ricordando che:
- dato che il sistema è lineare, il regime permanente complessivo è la somma dei singoli regimi (sovrapposizione degli effetti), quindi $$ t_{f}^{RP}(t) = t_{f}^{Y^{\text{o}}}(t)+y_{f}^{D}(t) $$
	- $t_{f}^{Y^{\text{o}}}(t)$ regime permanente in risposta al riferimento $y^{\text{o}}$
	- $t_{f}^{D}(t)$ regime permanente in risposta al disturbo $d$

La situazione che abbiamo come schema a blocchi è la seguente:
![[Pasted image 20220615175130.png|300]]

Quindi (dato che in ingresso abbiamo segnali costanti):
![[Pasted image 20220615175225.png|300]]

Dal teorema della risposta in frequenza (ingresso costante: allora il regime permanente è ancora un segnale a gradino pari al segnale d'ingresso per un guadagno in continua)
![[Pasted image 20220615175350.png]]
- dove in blu abbiamo la parte relativa al riferimento e che avevamo già calcolato (per la specifica $2$)
- in rosso invece abbiamo la parte "nuova" relativa al disturbo $d$

>Questa forma qui vale sempre quando abbiamo un sistema a ciclo chiuso su cui agisce un disturbo costante. Permette di misurare l'effetto del disturbo a regime.


### PROPRIETA' AZIONE INTEGRALE
Vediamo cosa comporta avere un polo in $0$ sul regime permanente. Calcoliamo quindi i guadagni in continua (con $p(0)=0$):

- Il guadagno in continua in ciclo chiuso *diventa unitario*, infatti
![[Pasted image 20220615175953.png]]
	- Quindi l'azione integrale va a soddisfare automaticamente la specifica $2$

- il guadagno in continua a ciclo chiuso tra disturbo e uscita si *annulla*, infatti:
![[Pasted image 20220615180126.png]]
	- Quindi l'azione integrale fa sì che l'effetto del disturbo (costante) sparisce (quindi *non ha effetto sull'uscita*)

Pertanto, in termini di **regime permanente**:
![[Pasted image 20220615180303.png]]
	-  Quindi l'azione integrale mi permette di avere un *regime permanente coincidente con il set-point*, ovvero di raggiungere l'obiettivo del progetto


Quindi con l'azione integrale sono garantite:
- specifica $2$
- annullamento del disturbo (reiezione perfetta)


##### RIASSUMENDO
- Un grado di libertà $\to$ $H_{f}=1$
![[Pasted image 20220615180818.png]]

![[Pasted image 20220615180847.png|600]]


### COME SI MODIFICA IL PROGETTO
Il polinomio deve annullarsi in zero al denominatore, quindi non metto il termine noto al denominatore, pertanto:
- con l'azione integrale i parametri liberi calano da $2 n_{K}+1$ a $2 n_{K}$
![[Pasted image 20220615181155.png]]

Quindi, **devo aumentare l'ordine del controllore**
- si chiede che $n_{K}\geq \text{grado }a(s)$
![[Pasted image 20220615181506.png]]

Quindi le buone proprietà dell'azione integrale le pago nella realizzazione del progetto nell'essere costretto a scegliere $n_K$ con un grado un po' più alto rispetto al progetto senza azione integrale
- In questo modo però posso posizionare i poli a mio piacimento (come volevamo)

**Nota:** inoltre deve valere anche $b(0)\neq 0$, infatti:
![[Pasted image 20220615181706.png|500]]
Se avessi $b(0)= 0$ non posso stabilizzare con l'azione integrale