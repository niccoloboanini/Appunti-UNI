# OSSERVATORE DELLO STATO E REGOLATORE
- Azione di controllo alla retroazione dinamica sull'uscita

#### RIEPILOGO: RETROAZIONE SULLO STATO
Essa era applicabile quando l'intero vettore di stato era accessibile (informazione completa) ed era della forma: $$ u(t) = -F \ x(t) + H \ y^{\text{o}}(t) $$
--> era progettabile $F$ tale da rendere il sistema in ciclo chiuso stabilizzante (si arrivava a una situazione in cui si poteva scegliere autonomamente la posizione degli autovalori sul piano complesso, modificando i parametri $f_{i}$)
- si poteva anche garantire $H$ per rispettare la specifica $2$

In caso in cui non abbiamo informazione completa di $x$, era necessario applicare la retroazione dinamica (utilizzando cioè una funzione di trasferimento con ordine sufficientemente elevato che mi garantiva stabilità)


## RETROAZIONE SULLO STATO STIMATO
Ci chiediamo ora: *se non abbiamo accesso $x$*, ovvero lo stato non è visibile, possiamo applicare un approccio simile per stabilizzare
![[Pasted image 20220616082851.png|500]]
In questo caso si conoscono solo i parametri ingresso/uscita del sistema (ovvero solo $u$ e $y$), non sappiamo come è fatto dentro $\mathcal{P}$
--> *informazione parziale*, $x$ sconosciuto

**Idea:** progettare l'osservatore dello stato (nuovo blocco)
- riceve in ingresso i dati ingresso uscita del sistema
- elabora l'informazione in ingresso
- determina in tempo reale (per ogni istante) una **stima** dello stato $\hat x(t) \approx \dot x(t)$
- ci si applica sopra la retroazione $$ u(t) = -F \ \hat x(t) + H \ y^{\text{o}}(t) $$
![[Pasted image 20220616083451.png|500]]

- Il sistema di controllo composto da *osservatore + retroazione sullo stato stimato* è il cosiddetto **regolatore**

 > Metodo alternativo alla retroazione dinamica quando abbiamo informazioni parziali. Nota: quella dinamica è più utilizzata nei sistemi SISO; quando abbiamo invece più ingressi e uscite si verrebbe a formare una matrice di funzioni di trasferimento (potenzialmente complesse), quindi in quei casi è più utilizzato l'approccio della retroazione sullo stato stimato (certezza equivalente)


L'obiettivo è ovviamente il seguente:
![[Pasted image 20220616084302.png]]
- si inizia da una stima di tentativo e col crescere del tempo si cerca di *sincronizzare* $\hat x(t)$ con $x(t)$
![[Pasted image 20220616084412.png]]

## OSSERVATORE DI LUENBERGER
Modalità di progetto più semplice per l'osservatore
- Ma sufficientemente complessa per risolvere il problema

Si vuole stimare $$ \mathcal{P} = \begin{cases} \dot x = Ax +Bu  \\ y = Cx \end{cases}  \quad , \quad \text{dove lo stato } x \text{ non si conosce}$$
 *Prima idea:*
 - dato che $u,A,B$  si conoscono, potrei avere la stessa dinamica, ovvero $$ \dot{\hat x}=A \hat x + Bu $$
	 - Funzionerebbe se si conoscessero le condizioni iniziali (ma lo stato non si conosce, non si sa all'inizio com'è)
	 - In più in questa forma non si considerano segnali di disturbo che nella realtà ci sono

Ora, potremmo anche continuare con questo approccio, magari supponendo delle condizioni iniziali, ma poi la predizione iniziale andrebbe via via corretta.
Infatti, si definisce:
![[Pasted image 20220616085250.png]]

Quindi all'idea di base *dobbiamo aggiungere un nuovo elemento correttivo* che appunto aggiusta man mano la mira alla mia predizione iniziale

---
### FORMULA
Si ottiene così l'osservatore di Luenberger
$$
\Large \mathcal{O} = \underbrace{A \hat x + B u}_{\text{predizione}} + \underbrace{L(y-C\hat x)}_{\text{correzione}}
$$
### TERMINE DI CORREZIONE
Dipende da:
- **Guadagno dell'osservatore $L$**: è un parametro di progetto (matriciale)
- **Differenza uscita e uscita predetta $y-C\hat x$**, detta *innovazione*
	- Dato che al tempo $t$ abbiamo una stima dello stato detta $\hat x$, possiamo predire quale sarà il valore dell'uscita sfruttando l'equazione di uscita classica $y=Cx$, quindi $\hat y(t)=C \hat x (t)$
		- Si osserva quindi la differenza tra l'uscita vera $y$ e l'uscita predetta $\hat y(t)$
			- Vorremmo stimare lo stato vero con lo stato stimato, ma il primo non lo conosciamo!
		- Quindi: $$ y- \hat y(t) = Cx(t) - C \hat x(t) $$, ovvero: $$ y-\hat y(t)=C [x(t)-\hat x(t)] $$
		- Quindi abbiamo una equivalenza tra due membri, di cui uno (la differenza tra gli stati, che vorrei calcolare) non la conosco, però è uguale a un'altra cosa (differenza tra le uscite) che si conosce, quindi riusciamo a trovare ciò che vogliamo
		- Nota: se $x(t)=\hat x(t)$ allora la stima è corretta al 100% e quindi anche il termine di correzione è nullo, cioè $y(t)-\hat y(t)$
			- Altrimenti se la stima non coincide, dovremo *correggere*
		- In altre parole, $y-C \hat x$ serve per vedere se la stima che facciamo è appurata oppure no: se la differenza non viene zero, allora dobbiamo correggere


## PROGETTARE IL GUADAGNO L
Si vuole sincronizzare lo stato dell'osservatore con lo stato del processo $\mathcal{P}$, ovvero, rendere lì errore ci stima asintoticamente a zero:
$$
\text{Vogliamo: } \hat x \approx \dot x \implies \lim_{t \to \infty} e = x(t)- \hat x(t) \approx 0
$$
Si studia come varia nel tempo l'errore di stima (facendo la derivata), possiamo farlo perché sappiamo come varia lo stato (ovvero $\dot x = Ax+Bu$) e abbiamo anche un modello per la stima $\dot{\hat x}$ 

Quindi:
(calcoliamo la derivata dell'errore, per sapere cioè come sarà l'immediato futuro per ogni istante $t$, cioè avere una stima sufficientemente precisa dell'evoluzione)
![[Pasted image 20220616092055.png]]
- La dinamica (evoluzione) della stima $e(t)$ non dipende dall'ingresso $u(t)$

Possiamo riscrivere $y$ in termini di uscita e poi osservare in ciò che ci rimane l'errore di stima:
![[Pasted image 20220616092320.png]]

Abbiamo ottenuto **la dinamica dell'errore di uscita**, ovvero come evolve nel tempo l'errore di stima (cioè la differenza tra stato vero e stato stimato supponendo che quello vero evolva con la dinamica $Ax+Bu$ e che quello stimato sia generato con l'osservatore $\mathcal{O}$):
$$
\Large \dot e = (A-Lc)\ e
$$
- Che è un **sistema LTI autonomo** con matrice della dinamica $A-LC$

Quindi il modo formale per vedere se il sistema funziona, è andare a vedere come varia l'errore di stima
#### IDEA
Ci rimane da scegliere $L$ (parametro di progetto) apposito tale da rendere la matrice della dinamica $A-LC$ **asintoticamente stabile** (tutti gli autovalori con $\text{Re}<0$)
- Se lo facciamo, allora *l'errore di stima* tende a zero
- Quindi dobbiamo trovare la soluzione del sistema LTI autonomo che viene qualcosa del tipo: $$ \exp[(A-LC)t] \ e(0) \to \underbrace{e^{(A-LC)t}}_{\text{esponenziale}}\ \underbrace{e(0)}_{\text{errore}}$$ - ovvero: esponenziale di matrice per condizione iniziale (data dall'errore di stima al tempo zero essendo un sistema TI)

![[Pasted image 20220616093526.png]]

**Nota:**
Situazione simile alla retroazione sullo stato in cui avevamo $A-BF$ e dovevamo trovare $F$
- Qui invece abbiamo $A-LC$ e dobbiamo trovare $L$

