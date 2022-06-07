#### DIMOSTRAZIONE DEL SE E SOLO SE
$\Leftarrow$ :
>> Tutti i poli di $G(s)$ con parte reale $<0$ implica stabilità esterna  [condizione sufficiente]

Premessa:
![[Pasted image 20220607150926.png|500]]

Passiamo quindi alla dimostrazione vera e propria, cercando di maggiorare ciò che abbiamo con una costante:
![[Pasted image 20220607151713.png|600]]
- l'ipotesi di avere poli con parte reale minore di zero implica che $C e^{At}B$ sia convergente a zero
	- Quindi nell'intervallo da zero a infinito l'area sottesa converge a una certa costante $N$
	- Poi ci rimane $D$ che è una costante
- Si nota che la risposta forzata è limitata, con le ipotesi di avere un ingresso limitato (stabilità esterna $BIBO$)
- Rinominiamo poi $N+|D|$ con $L$ che rapprsenta il *massimo guadagno* del sistema
![[Pasted image 20220607152111.png|600]]

---
$\Rightarrow$
>> Se vale la stabilità esterna, allora tutti i poli di $G(s)$ hanno parte reale $<0$
- Dimostriamo l'implicazione inversa, ovvero: $\overline B \implies \overline A$, quindi:
	- Se $G(s)$ ha almeno un polo con parte reale $\geq 0$ esistono ingressi limitati che fanno divergere l'uscita
Lo vediamo caso per caso (ovvero analizziamo gli scenari che rendono vera $\overline B \implies \overline A$ cioè i casi che ci vanno bene per dimostrare $A \implies B$)
- Nota: studiamo la posizione dei poli indipentemente dalla molteplicità
![[Pasted image 20220607152744.png]]

>> CASO 1: ingresso limitato porta uscita non limitata
![[Pasted image 20220607152818.png]]
- Perché abbiamo un polo con parte reale maggiore di zero (e questo implica stabilità esterna)

>> CASO 2: polo in zero porta instabilità esterna scegliendo opportuni ingressi
- Prendo ancora come ingresso limitato il gradino: $u(t) = 1(t)$
- Stesso polo della $G(s) \to \text{risonanza!}$
![[Pasted image 20220607153039.png|600]]

>> CASO 3: Poli puramente immaginari fanno divergere l'uscita scegliendo opportuni ingressi
- sollecito ancora il sistema con un ingresso che ha gli stessi poli di $G(s)$. In particolare con un ingresso sinusoidale che oscilla con la stessa pulsazione naturale dei modi del sistema 
- ancora fenomeno della risonanza
![[Pasted image 20220607153455.png|600]]
- $t \cos(\omega_{0}t)1(t)$ diverge (linearmente ma diverge)

## OSSERVAZIONI
Anche se il sistema è esternamente instabile, possono esistere ingressi per cui la risposta forzata non diverge!
Vediamo un esempio con poli puramente immaginari, provando dopo a prendere come ingresso un segnale sinusoidale con pulsazione diversa (poli non coincidenti)
- nel primo caso invece andiamo in risonanza (che confermano che il sistema è esternamente instabile)
![[Pasted image 20220607154326.png|600]]

## STABILITA' - RIASSUNTOZZO
![[Pasted image 20220607130427.png|600]]

> Per la stabilità interna devo guardare $\varphi(s)$ ed eventualmente $m(s)$ (non basta $G(s)$, perché potrebbero esserci poli nascosti)

> Per la stabilità esterna mi basta vedere $G(s)$ (funzione di trasferimento), senza interessi circa la molteplicità, a differenza della stabilità interna

Inoltre, vale anche la seguente importante relazione:
![[Pasted image 20220607154546.png|600]]

#### ESEMPIO: STUDIO STABILITà INTERNA E STABILITà ESTERNA
- Calcolo $\varphi(s)$
- Osservo i poli e concludo sulla stabilità interna
	- Se il sistema è internamente stabile allora posso concludere anche sulla stabilità esterna dicendo che è stabile anche esternamente, ma non è questo il caso dell'esercizio
- Se necessario procedo con lo studio di $G(s)$ per studiare la stabilità esterna
	- Cerco di calcolare il prodotto tra matrici nell'ordine più comodo
- Cerco i poli di $G(s)$, notando eventuali poli nascosti
	- Se i poli di $G(s)$ sono tutti negativi allora il sistema è esternamente stabile (BIBO)
![[Pasted image 20220607155124.png|600]]

# CRITERI ALGEBRICI PER LA STABILITA'
Utili perché non è sempre facile determinare tutte le radici di un polinomio $p(s)$
- Non esistono formule analitiche per polinomi di grado molto elevato (e spesso anche gli algoritmi iterativi non bastano)

Cerchiamo quindi dei criteri per rispondere alla domanda: *dato un polinomio, le sue radici hanno tutte parte reale minore di $0$ oppure no?*. In altre parole, le radici di un generico polinomio $p(s)$ appartengono tutte alla regione di stabilità interessata?
$$
\mathbb{C}_{s} = \{ s \in \mathbb{C} \text{ tali che Re[}s \text{]} <0\}
$$
- senza calcolare esplicitamente le radici

## CONDIZIONE NECESSARIA PER LA STABILITA'
Preso un polinomio "completo" avente tutti i coefficienti (moltiplicati da $s$ con potenze da $0$ a $n$)  non nulli e dello stesso segno, allora le radici hanno tutte parte reale minore di $0$
- Questa è una *condizione necessaria per la stabilità*
![[Pasted image 20220607160526.png|500]]
#### ESEMPI
Pertanto, se ho un cambio di segno tra un addendo e l'altro si può subito concludere che **non** tutte le radici hanno $\text{Re} < 0$. Lo stesso se manca un termine
![[Pasted image 20220607160415.png|500]]

Invece nel caso in cui la condizione necessaria è soddisfatta, non posso concludere sulla stabilità perché non è una condizione sufficiente per $p(s)$ con grado $> 2$. Mi serviranno metodo più avanzati per farlo
![[Pasted image 20220607160513.png|600]]

### REGOLA DI CARTESIO
In caso di polinomi con grado al più $2$, la condizione necessaria sopra descritta **è anche sufficiente**
![[Pasted image 20220607160716.png|600]]
#### ESEMPI
![[Pasted image 20220607160938.png|500]]

#### DIMOSTRAZIONE
![[Pasted image 20220607161228.png|600]]

## TABELLA DI ROUTH
Nel caso in cui sia verificata la condizione necessaria per polinomi di grado maggiore di $2$, come detto non possiamo dire niente sulla stabilità (perché la condizione proposta è necessaria ma non sufficiente).
- Per questo utilizziamo un semplice algoritmo, detto *tabella di Routh*
![[Pasted image 20220607161602.png|600]]
 Una volta costruita la tabella, osserviamo il **segno della prima colonna**, in particolare ogni variazione di segno corrisponde a una radine con parte reale maggiore di zero mentre ogni permanenza di segno corrisponde a una radice con parte reale minore di zero.
 - Se tutti i coefficienti sono diversi da zero e hanno lo stesso segno allora il polinomio è stabile
 - Se c'è un coefficiente è zero o c'è una variazione di segno allora il polinomio non è stabile 
![[Pasted image 20220607161902.png|600]]

### ESEMPIO: POLINOMIO DI TERZO GRADO (usato negli esercizi)
![[Pasted image 20220607172358.png|400]]

### CASO GENERALE
- Metto al denominatore il primo elemento della riga precedente e poi si moltiplica per il determinante della matrice composta nella prima colonna dagli elementi della prima colonna e poi gli elementi della colonna successiva rispetto all'elemento di riferimento
![[Pasted image 20220607172902.png|500]]
- negli esercizi al massimo avremo il grado $3$

### CRITERIO DI ROUTH-HURWITZ
![[Pasted image 20220607173036.png]]

