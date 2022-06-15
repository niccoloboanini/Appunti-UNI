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
L'azione integrale introduce un polo in $0$ nella funzione di trasferimento del controllore
Quindi in generale:
![[Pasted image 20220615170729.png]]
