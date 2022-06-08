# SISTEMI NON LINEARI - STUDIO DELLA STABILITA' INTERNA

## STABILITA'
- Nei sistemi non lineari la stabilità è intrinsecamente stabile solo *localmente*
	- Configurazione più complessa del sistema (stabilità diverse a seconda della zona)
![[Pasted image 20220608114947.png|500]]
- La stabilità è legata alla singola *traiettoria* e dipende da quanto perturbiamo (se perturbiamo tanto giungiamo a una situazione di stabilità diversa del sistema)

## PUNTI DI EQUILIBRIO
Abbiamo detto che la stabilità dipende dalle traiettorie.
Ci concentriamo solo sulle *traiettorie **costanti***, ovvero i punti di equilibrio
- Lo studio e l'individuazione di essi corrisponde a trovare le condizioni di quiete

Matematicamente è una coppia stato ingresso per cui:
- Partendo da quello stato e applicando costantemente quell'ingresso allora lo stato non cambia
$$
\boxed{
\text{Coppia di partenza: } (x_{e},u_{e}) \Rightarrow
\begin{align*}
&x(0) = x_{e}\\
&u(t) = u_{e}
\end{align*} \implies x(t) = x_{e}  \quad , \forall t \geq 0}
$$
I punti di equilibrio sono quelli rappresentati in verde, rosso e blu nella figura precedente (sono lì fermi, non si muovono, supponendo che siano effettivamente fermi in partenza)

*Sono i punti in cui la derivata vale zero*
$\dot x(t) = \frac{d}{dt}x(t) = 0$
$\dot x(t) = f(x(t),u(t))$
$x(t) = x_{e}  \quad , \quad u(t)=u_{e}$
$\Rightarrow \dot x(t) = 0$
![[Pasted image 20220608120228.png|500]]
- trovare i punti di equilibrio quindi corrisponde a trovare tutte le coppie $(x_{e},u_{e})$ tali per cui la $f(x_{e},u_{e}) = 0$
### USCITA DI EQUILIBRIO
È una funzione associata a ciascun punto di equilibrio, in particolare:
$$
y_{e} = h(x_{e},u_{e})
$$

## ESEMPI
### ESERCIZIO
- Sistema non autonomo
- Ci interessano solo le *soluzioni reali in $\mathbb{R}$*
![[Pasted image 20220608120954.png|600]]

### PENDOLO (braccio robotico)
![[Pasted image 20220608121546.png|500]]
- unico grado di libertà: angolo $\theta$

Riscriviamo l'equazione differenziali in termini di equazione di stato
 - Poi cerco i punti di equilibrio una volta trovata la funzione di transizione di stato $f(x)$
![[Pasted image 20220608122049.png|500]]
- prima componente stato $x_e$ : angolo
- seconda componente stato $x_e$ : velocità
![[Pasted image 20220608122756.png|600]]
- Infiniti punti di equilibrio (angolo pari a $k\pi$ e velocità angolare nulla)
	- Per $k$ pari i punti di equilibrio sono quelli in cui il pendolo è in verticale in basso
		- Equilibrio *stabile*. Se applico piccole sollecitazioni il pendolo torna nella medesima posizione
	- Per $k$ dispari i punti di equilibrio sono quelli in cui il pendolo è in verticale in alto
		- Equilibrio *instabile* (con il controllo lo potremo rendere stabile). Per ora però con piccole sollecitazioni il pendolo perde l'equilibrio 

## MAPPA TRANSIZIONE GLOBALE
Supponendo che sia possibile trovare la soluzione di un sistema non lineare, allora questa è identificata dalla *mappa di transizione di stato*:
$$
x(t) = \Phi (t,x_{0},u)
$$
Ovvero a partire da una condizione iniziale $x_{0}$ e un segnale d'ingresso $u$ possiamo determinare lo stato del sistema per ogni istante $t$

Se abbiamo un punto di equilibrio $(x_{e}, u_{e})$ allora la mappa si riduce a
$$
\Phi (t,x_{e},u_{e}) = x_{e}
$$
- ovvero se applichiamo un determinato stato e un ingresso rimaniamo nella posizione di equilibrio
*Proviamo ora a perturbare*
- osservo cioè la traiettoria a partire da un punto "leggermente" spostato rispetto a $x_{e}$, ovvero $x_{e}+\tilde x_{0}$
![[Pasted image 20220608124957.png|500]]
## EFFETTO PERTURBAZIONE
Al solito, si fa la differenza tra la situazione perturbata e quella nominale:
![[Pasted image 20220608125019.png|600]]

## STABILITA' ALLA LYAPUNOV

>Perturbazioni sufficientemente piccole della condizione iniziale danno luogo a perturbazioni arbitrariamente piccole della traiettoria

"Più piccola è la perturbazione più piccolo è l'effetto"
- Se perturbiamo poco la condizione iniziale rispetto alla condizione di equilibrio, allora anche la traiettoria corrispondente si allontana poco dalla condizione di equilibrio stessa

Matematicamente:
Abbiamo stabilità se (partendo da un punto $x(0)$ di equilibrio):
- Fissato un $\delta$ esterno al punto di equilibrio tale per cui la condizione iniziale perturbata si trova in questo intorno, allora anche la relativa traiettoria si trova a distanza inferiore a $\large \varepsilon$
- Dal punto di equilibrio riesco sempre a trovare un intorno $\delta$ che mi garantisce questo tipo di stabilità
![[Pasted image 20220608131001.png|300]]

Quindi: 
- $\delta$ è la perturbazione massima che agiamo sulla condizione iniziale
- $\large \varepsilon$ è la traiettoria massima che "possiamo permetterci" una volta fissato $\delta$
Ovvero la differenza tra la traiettoria perturbata e quella nominale deve essere inferiore a un certo $\large \varepsilon$ fissato
![[Pasted image 20220608130844.png]]

