## ATTRATTIVITA'
Fin ora con la stabilità alla Lyapunov abbiamo visto la stabilità della traiettoria a livello locale (piccole perturbazioni di $x(0)$).
Estendiamo adesso il concetto con l'attrattività, che *studia il comportamento asintotico*

>> L'attrattività ci dice che dopo una perturbazione iniziale la traiettoria tende a convergere nello stato di equilibrio di partenza

Si prende quindi come riferimento un $x_{e}$ di equilibrio e da lì si prende un punto iniziale $x(0) = x_{e}+\tilde x_{0}$ e si studia il comportamento della traiettoria
- Se dopo un certo tempo converge al punto di equilibrio allora vale l'attrattività

Può essere **locale** o **globale**
##### LOCALE
- Esiste un "bacino di equilibrio" intorno al punto di equilibrio.
	- Se perturbiamo con un $\tilde x_{0}$ tale che $||\tilde x_{0}|| < \delta$ allora esiste attrattività locale se poi la traiettoria ritorna nel punto di equilibrio $x_{e}$
 ![[Pasted image 20220608145046.png|200]]
- Qui si vede bene: $x(0)$ è interno all'intorno di $\delta$ quindi è interno al "bacino di attrazione/equilibrio" e pertanto la traiettoria convergerà a $x_{e}$
	- Esempio: pendolo --> se partiamo da una condizione non perfettamente verticale, dopo un po' di tempo in presenza d'attrito il pendolo torna nella posizione di equilibrio
$$
\boxed{||x_{0}|| \leq \delta \implies \Phi(t,x_{e}+\tilde x_{0},u_{e}) = x_{e}}
$$
#### GLOBALE
Indipendentemente da quanto è grande la perturbazione $\tilde x_{0}$, la traiettoria converge al punto di equilibrio $x_{e}$
$$
\boxed{\lim_{t \to \infty} \Phi(t,x_{e}+\tilde x_{0},u_{e}) = x_{e}}$$
![[Pasted image 20220608145624.png]]
- un punto di equilibrio per essere globalmente attrattivo deve essere l'unico del sistema


> [!note] Relazione tra le due stabilità
> Possono esserci dei casi in cui vale la stabilità alla Lyapunov ma non vale l'attrattività, o viceversa. Per questo i due concetto sono indipendenti l'uno con l'altro
> Ad esempio (Pallina sul piano):
> ![[Pasted image 20220608150113.png|200]]
> Abbiamo in questo caso stabilità alla Lyapunov (perché rimaniamo nell'intorno in caso di piccole perturbazioni) ma non attrattività (perché non torniamo al punto di equilibrio)
> Riportiamo adesso un caso in cui vale attrattività ma non la stabilità alla Lyapunov
> ![[Pasted image 20220608150337.png|500]]
> Prima di tornare nel punto di equilibrio mi allontano
> *Quindi un sistema è stabile se valgono entrambe queste condizioni*


## STABILITA' INTERNA DEI PUNTI DI EQUILIBRIO
![[Pasted image 20220608150614.png|500]]
![[Pasted image 20220608150913.png|600]]

### STUDIO DELLA STABILITA'
- Metodo di Lyapunov diretto --> ricerca di una funzione che associa il punto minimo di energia al punto di equilibrio (non lo studiamo)
- **Metodo indiretto di Lyapunov: linearizzazione**
	- Andiamo a linearizzare il sistema e studiamo quest'ultimo, con i metodi visti per i sistemi lineari

## METODO DI LYAPUNOV INDIRETTO - LINEARIZZAZIONE
Si approssima un sistema non lineare con un sistema lineare associato, ottenuto tramite il processo di linearizzazione del sistema di partenza

Sistema non lineare: $$ \begin{cases} \dot x = f(x,u)  \\ y = h(x,u) \end{cases} $$
- Lo si approssima *linearizzando le funzioni $f$ e $h$*

Si approssima la funzione (non lineare) nel punto di equilibrio $x_{e}$ con la relativa *retta tangente*
- Ovvero una *approssimazione di Taylor* del primo ordine
![[Pasted image 20220608151659.png|150]]
Ovvero:
$$
f(x) = \underbrace{f(x_{e}) \left.\frac{df}{dx} \right |_{x=x_{e}} x(x-x_{e})}_{\text{retta}} + \underbrace{R(x-x_{e})}_{\text{resto}}
$$
- Dove il resto tende a $0$ di ordine superiore rispetto alla retta
Quindi possiamo approssimare la nostra funzione non lineare con la **retta tangente** (lineare)
$$
\boxed{f(x) \approx f(x_{e}) \left.\frac{df}{dx} \right |_{x=x_{e}} x(x-x_{e})}
$$

In **generale**, l'approssimazione per funzione di più variabili si può effettuare con la **matrice Jacobiana delle derivate parziali** calcolata nel punto di equilibrio
$$
f(x,u) \approx f(x_{e},u_{e}) + \underbrace{\left.\frac{\partial f}{\partial x} \right |_{x=x_{e},u=u_{e}}}_{\large A_{e}} x(x-x_{e}) + \underbrace{\left.\frac{\partial f}{\partial u} \right |_{x=x_{e},u=u_{e}}}_{\large B_{e}}(u-u_{e})
$$
- perché $x$ è il vettore dello stato e $u$ il vettore degli ingressi
- $f = \begin{bmatrix} f_{1}  \\  \vdots  \\  f_{n} \end{bmatrix}$

- ![[Pasted image 20220608153100.png|400]]

Ovviamente si linearizza allo stesso modo anche $h(x,u)$:
![[Pasted image 20220608153302.png]]
--

Quindi partendo dal sistema non lineare abbiamo:
- trovato un punto di equilibrio $(x_{e},u_{e})$ t.c. $f(x_{e},u_{e}) = 0$, con $y_{e} = h(x_{e},u_{e})$
- e abbiamo poi approssimato le due funzioni $f$ e $h$ grazie alle matrici Jacobiane $A_{e},B_{e},C_{e},D_{e}$
![[Pasted image 20220608153648.png]]
- dove abbiamo osservato che $f(x_{e},u_{e}) = 0$ e $h(x_{e},u_{e}) = y_{e}$ per ipotesi del punto di equilibrio
*Possiamo riscrivere il sistema linearizzato nell'intorno dell'equilibrio* come:
![[Pasted image 20220608154019.png|600]]
- Rinominando gli argomenti all'interno delle parentesi (che sono oggetti che conosciamo almeno come idea)
![[Pasted image 20220608154032.png|500]]

Si osserva anche, dato che $x_{e}$ è costante:
![[Pasted image 20220608154159.png|600]]
Posso riscrivere la prima equazione:
![[Pasted image 20220608154227.png|500]]

Allo stesso modo, per l'uscita:
![[Pasted image 20220608154310.png]]
![[Pasted image 20220608154323.png]]

Possiamo quindi riassumere il tutto in *unico sistema linearizzato* relativo a uno specifico punto di equilibrio:
![[Pasted image 20220608154414.png]]
- ha come stato la deviazione rispetto all'equilibrio
- ha come ingresso la deviazione rispetto all'ingresso di equilibrio
- ha come uscita la deviazione rispetto all'uscita di equilibrio
*- Per questo è lineare (secondo un certo punto di equilibrio)*


**Si potrebbe dimostrare che lo studio della stabilità interna (robustezza rispetto a variazioni delle condizioni iniziali) dell'equilibrio si riduce all'esclusivo studio della matrice $A_{e}$**.

### TEOREMA DEL METODO INDIRETTO ALLA LYAPUNOV
Valgono le seguenti (casi indipendenti dalla molteplicità):
![[Pasted image 20220608155029.png]]
- nel caso critico dovrei considerare approssimazioni di Taylor a un ordine più grande

### ESERCIZIO 1)
- Trovo i punti di equilibrio (già fatto in esercizio precedente)
- Compongo la matrice Jacobiana $A_{e}$
	- Calcolo il risultato nei vari punti di equilibrio
		- Concludo sulla stabilità caso per caso
![[Pasted image 20220608160022.png|700]]
![[Pasted image 20220608160134.png|700]]

Quindi:
![[Pasted image 20220608160158.png|400]]
- tendo in generale a convergere in $-\sqrt{u_{e}}$
