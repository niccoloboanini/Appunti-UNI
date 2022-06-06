# STABILITA'
## INTRO
Studia la tendenza a resistere di un sistema (robustezza) rispetto a *perturbazioni*.
Le perturbazioni possono derivare da più parti, in particolare si parla di:
![[Pasted image 20220606161540.png]]
- studieremo solo le prime due (interna ed esterna)

>Un sistema è robusto se date piccole perturbazioni la sua soluzione varia di poco

## STABILITA' INTERNA
Può essere di tre tipi:
![[Pasted image 20220606162038.png|600]]

### MAPPA TRANSIZIONE GLOBALE
Partendo da un sistema LTI TC e conoscendo la condizione iniziale $x(0)  = x_{0}$ e il segnale d'ingresso $u(t)$
- Definiamo la mappa di transizione di stato una funzione che dice qual è la condizione dello stato per ogni tempo $t$, a partire dalla condizione iniziale e l'ingresso. In formule: $$ \Large x(t) = \Phi(t,x_{0},u) $$
Essa come già visto in passato vale:
$$\Phi(t,x_{0},u) = \underbrace{e^{At} x_{0}}_{\Large x_\ell(t)} + \underbrace{\int_{0}^{t} e^{A(t-\tau)} B u(\tau) \,d\tau}_{\Large x_f(t)}  $$

- "Mappa di transizione" perché ci fa capire la transizione da una certa condizione iniziale a un generico tempo $t$
- "Di stato" perché è relativa allo stato del  sistema generico $\begin{cases} \dot x = Ax +Bu  \\ y = Cx + Du \end{cases}$

### EFFETTO DELLA PERTURBAZIONE
Consideriamo a partire dalla traiettoria nominale $x(t)$ sopra descritta una **traiettoria perturbata**, del tipo:
$$
\large x(t) = \Phi(t,x_{0}+\tilde x_{0},u)
$$
**L'effetto della perturbazione si trova facendo la differenza tra le due traiettorie:**
![[Pasted image 20220606163328.png]]
- Ci si accorge che la perturbazione non modifica l'evoluzione forzata $x_{f}(t)$ (perché si semplifica)
- Rimane *soltanto la differenza tra le evoluzioni libere*

Quindi l'effetto della perturbazione dipende da:
- matrice $A$ (che descrive la dinamica del sistema)
- perturbazione $x_{0}$ (ovvero come perturbiamo)
Ovvero, **non dipende né dalla condizione iniziale $x_{0}$ né dall'ingresso $u$**

> [!important] Proprietà Intriseca
> Quindi la stabilità interna per sistemi *lineari* è una **proprietà intrinseca del sistema stesso**
> Inoltre la perturbazione influenza solo l'evoluzione libera
> 	Pertanto possiamo già studiarla

### FORMULE PER LA STABILITA' INTERNA
![[Pasted image 20220606164202.png|600]]
- Come si vede gli effetti si valutato solo guardando l'evoluzione libera, ovvero l'esponenziale di matrice $e^{At}$ (moltiplicato per una certa perturbazione $\tilde x_{0}$)
