## POTENZA DI MATRICE
Per calcolare $A^{t}$ è conveniente anche in questo caso passare dall'operatore di trasformata, ottenendo:
$$
\mathcal{Z}\{A^{t}\} = (zI-A)^{-1}\ z = \frac{1}{\varphi(z)}Adj(zI-A)\ z$$
Così come: $\mathcal{L}\{e^{At}\} = (sI-A)^{-1}$

Analogamente al caso dei sistemi TC:
![[Pasted image 20220610120204.png|600]]


>> Quindi gli autovalori del polinomio caratteristico sono ancora i poli dell'inversa, ovvero $(zI-A)^{-1}$

## CONFRONTO LAPLACE - Z (TC-TD)
- Il polo del gradino in TD è $1$
- Al posto del modo evoluzione esponenziale, nel TD abbiamo modo evoluzione potenza (con i relativi sviluppi (moltiplica per $t$) quando aumenta la molteplicità)
![[Pasted image 20220610121149.png|600]]

## MODI NATURALI
Quindi nella potenza $A^{t}$ abbiamo i modi di evoluzioni, con molteplicità associata ai poli di $\varphi(z)$:
![[Pasted image 20220610121304.png|550]]

- I modi in Laplace erano esponenziali: $e^{\lambda_{1}t},te^{\lambda_{1}t},\dots$

### MODULO E FASE (ARGOMENTO)
Invece di guardare parte reale e immaginaria per stabilire rispettivamente convergenza oppure oscillazioni, *si va a guardare il modulo e la fase* di un certo polo $\lambda_{i}$
![[Pasted image 20220610122917.png]]
- Utile perché posso riscrivere la potenza di matrice $\lambda_{i}^{t}$ in modo più semplice
Infatti un certo $\lambda_{i}$ lo si può riscrivere come: $$ \boxed{\lambda_{i}= \rho_{i}e^{j\theta_{i}} } \quad , \quad \text{avente } \rho_{i}=|\lambda_{i}| \ \ , \ \ \theta_{i}=\angle{\lambda_{i}}$$
La relativa potenza è data da:
$$
\Large \lambda_{i}^{t}= (\rho_{i}e^{j\theta_{i}})^{t} = \rho_{i}^{t}e^{j\theta_{i}t} = \underbrace{\rho_{i}^{t}}_{\text{}} \ \{ \cos(\theta_{i}t)+j \sin (\theta_{i}t) \}
$$

La convergenza o meno dipende dal modulo $\Large \rho_{i}^{t}$ (ovvero il termine di esponenziale reale)
- In generale quindi dipende dal modo di ciascun autovalore, ovvero: $\rho_{i}=|\lambda_{i}|$
##### * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
![[Pasted image 20220610123616.png|500]]
##### * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
#### POLO $\lambda_{i}$ reale positivo
- Quanto $\theta_{i}=0$ (no parte immaginaria, il polo sta sull'asse orizzontale reale)
![[Pasted image 20220610122100.png|500]]

##### POLO $\lambda_{i}$ REALE NEGATIVO
- il seno va a $0$
- il coseno vale $\pm 1$
>> componente oscillatoria (seni alterni)

![[Pasted image 20220610122444.png|500]]
- Rispettivamente oscillante convergente, oscillante limitato, oscillante divergente

#### $\textcolor{green}{AUTOVALORI \ COMPLESSI \ CONIUGATI}$
- Quando $\theta_{i}\neq 0$ e $\theta_{i}\neq \pi$
![[Pasted image 20220610123731.png|400]]


### RIASSUMENDO
![[Pasted image 20220610123947.png|550]]
Quindi la molteplicità diventa importante quando abbiamo autovalori con modulo $1$, ovvero il caso $|\lambda_{i}|=1$

![[Pasted image 20220610124050.png|500]]

#### CONFRONTO MODI TC-TD
![[Pasted image 20220610124500.png|500]]
- da una parte abbiamo come "confine" il semipiano sinistro, dall'altra la circonferenza unitaria
> i modi del TC sono esponenziali $e^{\lambda_{i}t}$ mentre in TD sono potenze $\lambda_{i}^{t}$

## STABILITA' DEI SISTEMI TD
 ### INTERNA
 Stabilità interna: proprietà intrinseca del sistema (non dipende dalla traiettoria)
 In generale, in maniera simmetrica rispetto al caso TC:
![[Pasted image 20220610124926.png|600]]

### ESTERNA
Necessita del calcolo della funzione di trasferimento $G(z) = C(zI-A)^{-1}B+D$
- Si fanno eventuali semplificazioni
- Si studia il denominatore $a(z)$ e i suoi poli (che sono un sottoinsieme di tutti i poli del sistema come del caso TC)
	- Abbiamo (bibo)stabilità esterna se i poli di $a(z)$ hanno tutti modulo $<1$
- Stabilità asintotica implica stabilità esterna (ma non vale il contrario)
![[Pasted image 20220610125300.png|500]]

![[Pasted image 20220610125558.png|500]]


## STABILITA' SISTEMI NON LINEARI
### PUNTI DI EQUILIBRIO
Coppia stato ingresso tale per cui se partiamo dallo stato della coppia e applichiamo tale ingresso, allora rimaniamo nello stesso stato (analoga definizione)
$$
x(0) = x_{e}, \ \ u(t)= u_{e} \ \ \implies x(t) = x_{e} \ \ \forall t \geq 0 
$$
Il punto di equilibrio rappresenta dunque una *traiettoria costante* del sistema

**Cambia solo il modo con cui calcolo i punti di equilibrio**
- nel caso TC si annulla la derivata
- nel caso TD si deve garantire che lo stato successivo $x(t+1)$ coincida con quello corrente $x(t)$. Ovvero il punto $x_{e}$ deve essere un *punto fisso* dell'equazione transizione di stato cioè $\boxed{x_{e}= f(x_{e},u_{e})}$ (caso non autonomo)
	- Da cui si derivano tutte le considerazioni fatte per la stabilità asintotica (Lyapunov, attrattività locale...)
![[Pasted image 20220610130152.png|600]]

### STABILITA': METODO INDIRETTO DI LINEARIZZAZIONE
La stabilità di un punto di equilibrio (dato un sistema non lineare) si studia anche in questo caso con il metodo della linearizzazione
- Si studia quindi il comportamento del sistema linearizzato
	- Calcolando la matrice $A_{e}$ Jacobiana delle derivate parziali $$ A_{e}= \frac{\partial f}{\partial x}  \quad , \quad \text{calcolata in }(x,u)=(x_{e},u_{e}) $$
- Dove cambia solo la $ROC$, quindi bisogna guardare il modulo degli elementi della matrice $A_{e}$
In particolare:
![[Pasted image 20220610130619.png|600]]

#### NOTA: all'esame non ci sono esercizi di analisi dei sistemi non lineari, ma bisogna sapere la teoria per l'orale

---
---

# **SISTEMI DI CONTROLLO**
- Far comportare un sistema in un modo desiderato
- Lo vediamo solo per il tempo continuo e per sistemi lineari (ma vale anche lo stesso per il tempo continuo e per i sistemi non lineari nell'intorno dei punti di equilibrio)

Il sistema da controllare si chiama impianto o processo ($\mathcal{P}$)
 $$
\mathcal{P}: \begin{cases} \dot x(t) = Ax(t) +Bu(t)  \\ y(t) = Cx(t) + \cancelto{0}{Du(t)} \end{cases}
$$
- Ipotizzando $D = 0$ (perché il controllo non può influenzare l'uscita $y$ istantaneamente, ma andremo ad agire sull'ingresso e poi dopo un certo ritardo l'uscita viene influenzata anche con quello che abbiamo dato in ingresso)

- Lo *scopo* del controllo è quello di *agire sul sistema mediante il segnale di controllo/ingresso $u$, in modo tale che l'andamento in uscita del sistema (valore delle variabili che vogliamo controllare) sia il più vicino possibile al segnale $y^{0}$ detto di riferimento*
	- $y-y^{0}$ viene detto **errore d'inseguimento**. L'obiettivo è renderlo il più piccolo possibile


- La classe di problemi che auspica a una uscita di riferimento pari a zero, ovvero $y^{0}=0 \ \ \forall t$ viene chiamata *problema di regolazione a zero*. Si raggiunge uno stato di *quiete*
- Gli altri problemi sono invece *problemi d'inseguimento*, in cui si cerca di controllare il sistema per ottenere un riferimento $y^{0}(t)$ generico, non nullo. Esso rappresenta la *traiettoria desiderata del sistema*
	- Ci occuperemo di questi solo parlando dei *problemi d'inseguimento con riferimento costante*, ovvero tali che $$ y^{0}(t) = Y_{0} \cdot 1(t) $$
	- che è un riferimento a gradino (costante). Vogliamo cioè portare l'uscita a un valore costante (esempio: cruise control/termostato...)
	- $Y_{0}$ è detto **set-point**, e rappresenta il valore/valori a cui vogliamo portare l'uscita (velocità macchina, temperatura della stanza...)

## CONTROLLO IN ANELLO APERTO :(
Si predetermina un segnale di ingresso $u$ sulla base delle esigenze $y^{0}$ e lo si applica al sistema.
- Non si controlla più: si suppone che non ci siano disturbi anche imprevisti che potrebbero interferire con l'ingresso scelto. Modello per questo in un certo senso *ideale*
![[Pasted image 20220610155932.png|400]]

- Sarebbe un po' come impostare a priori il miscelatore della doccia in una certa posizione "sperando" che poi l'acqua sia alla temperatura desiderata.
	- Con il controllo in retroazione invece avremmo la possibilità di regolare la manopola sulla base di com'è la temperatura in un certo istante (la porto verso destra se l'acqua e calda e viceversa - in tal caso $w$ sono i sensi sulla pelle che misurano la temperatura)

## CONTROLLO IN RETROAZIONE :)
 **Feedback control**
 Tengo conto in tempo reale del comportamento del sistema.
 - Suppongo di conoscere le variabili $w$ che danno informazioni sulla configurazione del sistema in un certo istante $t$.
 - Quindi l'azione del controllo $u$ non è predeterminata, ma è generata in ogni istante di tempo sulla base dei dati forniti da $\mathcal{P}$ con il **vettore informativo $w$**
 ![[Pasted image 20220610160350.png|400]]
- detto anche controllo in *catena aperta* (ad anello)

Se il vettore informativo coincide con l'intero stato, allora si parla di *controllo in retroazione sullo stato*. Abbiamo una informazione completa dello stato (conosco tutto quello che sta succedendo in $\mathcal{P}$) $$ \boxed{w(t) = x(t)}  \quad \to \quad \text{controllo in retroazione sullo stato} $$
Se invece abbiamo a disposizione solo una parte delle variabili, guardiamo il caso in cui conosciamo solo l'uscita di $\mathcal{P}$. Si parla perciò di *controllo in retroazione sull'uscita*. Abbiamo quindi solo una informazione parziale di quello che sta succedendo $$  \boxed{w(t) = y(t)}  \quad \to \quad \text{controllo in retroazione sull'uscita}  $$
- Non posso guardare cosa succede dentro $\mathcal{P}$, ma guardo solo cosa esce ovvero $y$.