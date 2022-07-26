# **1) MODELLISTICA E SIMULAZIONE**

## MODELLO
Descrive matematicamente un sistema

### TEMPO DISCRETO (TD)
Descritti da $\text{equazioni alle differenze}$
- Più facili da implementare (utili per approssimare modelli tempo continuo complessi)
### TEMPO CONTINUO (TD)
Descritti da $\text{equazioni differenziali}$

## SISTEMA CAUSALE
Sistema dinamico, rappresentabile in maniera intuitiva con l'asse dei tempi:
- si distingue cioè tra: passato, presente $t$ e futuro.
	- Ognuno di essi è in interazione secondo il principio *causa-effetto*: il valore a un certo tempo $t_{0}$ dipende solo da istanti precedenti $t_{0}-1,t_{0}-2,\dots$

#### STATO DEL SISTEMA
Rappresenta la *configurazione* del sistema a un certo istante di tempo $t_{0}$. 
- È in altre parole una fotografia del sistema
- Conoscendo gli ingressi, esso contiene tutte le informazioni necessarie per prevedere come si evolverà il sistema stesso

Matematicamente è un insieme di variabili (vettore) necessarie da conoscere per descrivere un sistema a un certo istante $t_0$.
- Si rappresenta con $x(t_{0})$
![[Pasted image 20220527094901.png|250]]

#### EQUAZIONI DI STATO TD
Dette anche *rappresentazioni ingresso-uscita*, permettono appunto di rappresentare un sistema
$$
\begin{align*}
&\text{eq. transizione stato} & x(t+1) &= f(t,x(t),u(t))  \\
&\text{eq. uscita} & y(t)&= h(t,x(t),u(t))
\end{align*}
$$
- La prima permette di passare da un certo istante $t$ a un istante $t+1$, sulla base della configurazione attuale $x(t)$ e gli ingressi $u(t)$
	- $f$ è la funzione di transizione di stato
- La seconda permette di calcolare il valore di uscita (che in generale è un vettore) di un sistema sulla base della configurazione attuale $x(t)$ e gli ingressi $u(t)$
	- $h$ è la funzione di uscita
			- Se come uscita ci interessa l'intero stato, allora $y(t) = x(t)$

#### EQUAZIONI DI STATO TC
L'istante successivo dell'equazione (che nel TD è $t_{0}+1$), è un istante infinitesimale successivo. Ovvero in è la derivata rispetto al tempo $\bigg( \displaystyle \dot x(t)=\frac{dx(t)}{t}\bigg)$
$$
\begin{align*}
&\text{eq. transizione stato} & \dot x(t) &= f(t,x(t),u(t))  \\
&\text{eq. uscita} & y(t)&= h(t,x(t),u(t))
\end{align*}
$$
- Viene specificato quindi lo stato dopo una variazione di tempo infinitesimale
- Indica in particolare *il tasso di variazione*: 
$$
\dot x \to \lim_{\Delta t \to 0^+} \frac{x(t+\Delta t)-x(t)}{\Delta t} = f(t,x(t),u(t))
$$
![[Pasted image 20220527101445.png]]

## SISTEMI NON AUTONOMI
Un sistema si dice *non autonomo* se *è presente un ingresso* che influenza l'evoluzione del sistema. Pertanto, c'è una interazione con l'esterno così rappresentabile:
$$
\big[ \dot x || x(t+1) \big] =f(t,x(t),u(t))  \quad , \quad y(t)=h(t,x(t),u(t))
$$

Viceversa, un sistema autonomo non ha ingressi dall'esterno che influenzano l'evoluzione del sistema. Quindi:
$$
\big[ \dot x || x(t+1) \big] =f(t,x(t))  \quad , \quad y(t)=h(t,x(t))
$$
- mi basta conoscere la configurazione al tempo $t$ per capire l'evoluzione futura (risolvendo l'equazione differenziale / alle differenze)

## SISTEMI TEMPO INVARIANTI
Un sistema è *tempo invariante* se la configurazione di evoluzione futura del sistema non dipende dall'istante in cui ci troviamo $t$.
- Si comporta cioè allo stesso modo indipendentemente dal tempo in cui osserviamo (ora, tra un anno, tra dieci anni...)
- il sistema cioè risponde allo stesso modo indipendentemente dal tempo in cui si applica l'ingresso
	- esempio: corpo umano --> la risposta dipende dal tempo
$$
\big[ \dot x || x(t+1) \big]=f(x(t),u(t))  \quad , \quad y(t)=h(x(t),u(t))  \quad , \quad  \text{non compare } t
$$

Viceversa, l'evoluzione di un sistema *tempo variante* dipende dal tempo $t$ in cui si applica
$$
\big[ \dot x || x(t+1) \big]=f(t,x(t),(t))\quad , \quad y(t)=h(t,x(t),u(t))  \quad , \quad \textbf{compare } \mathbf{t}
$$
- esempio: equazioni della fisica

## RIASSUNTO
![[Pasted image 20220527103606.png|500]]

## ESEMPI
### MODELLO SISTEMA SCOLASTICO
$$
x(t+1) = x(t) - \alpha x(t) - \beta x(t)+ u(t)
$$
- $\alpha$ e $\beta$ in percentuale ($\in(0,1)$), rappresentano persone che lasciano gli studi o che vengono promossi
- l'indice di riferimento $t$ è discreto
- è una equazione alle differenze
Analogamente:
$$
x(t+1) = f\big(x(t),u(t)\big)
$$
- si calcola quindi un valore della variabile d'interesse (studenti iscritti) a un certo $t+1$ in funzione del valore al tempo $t$ e dell'ingresso $u(t)$.
- l'equazione alle differenze quindi permette di passare dal tempo $t$ al tempo $t+1$
- Vale se il sistema è **causale**
	- Lo stato del sistema è il numero di studenti iscritti
	- Si sottintende che $y(t) = x(t)$
- è classificato come modello di trasferimento di risorse

### MODELLO ROBOT
![[Pasted image 20220527101921.png|600]]


# MODELLO DI TRASFERIMENTO DI RISORSE
Sono rappresentati da una **equazione di bilancio**:
$$
x(t+1) = x(t) + f^{\text{in}}(t) + f^{\text{out}}(t)
$$
Dove abbiamo *risorse che entrano e che escono*
- Negli esempi più complessi le risorse si possono trovare **in più stadi**
### ESEMPIO: CONTO IN BANCA
$f^{in}$ sarà rappresentato dagli ingressi in termini di soldi nel mio conto (guadagni), ad esempio dati dagli interessi che fruttano nel conto attuale e dai guadagni mensili regolari, quindi:
$$
f^{in}(t)= \gamma x(t) + g(t)
$$
$f^{out}$ sarà rappresentato dai flussi di uscita (spese), quindi:
$$
f^{out}(t) = s(t)
$$
L'equazione di stato sarà:
$$
x(t+1) = x(t)+\gamma x(t) + g(t) - s(t)
$$

## MODELLI COMPARTIMENTALI
Usati quando le risorse nei modelli di trasferimento appena descritti hanno *più di uno stadio*, in generale $n$ stadi
- Un esempio generale può essere quello degli anni accademici della triennale: abbiamo tre compartimenti ciascuno che descrive un anno accademico.
	- Due stadi sono collegabili tra loro grazie alle transizioni
![[Pasted image 20220527104813.png|300]]
- In questo caso dopo l'ultimo compartimento, si esce dal sistema (non sempre questo accade, può essere ciclico)

Sono detti anche *modelli di flusso* o *modelli di decisione* a seconda se il tempo è rispettivamente continuo (TC) o discreto (TD)

A ogni compartimento si può associare una variabile di configurazione dello stato stesso
![[Pasted image 20220527105121.png]]
- In questo caso $x_{i}$ rappresenta ad esempio il numero di studenti iscritti

In generale:
![[Pasted image 20220527105222.png|300]]

#### Esempio corso magistrale:
![[Pasted image 20220527105414.png|300]]
![[Pasted image 20220527105522.png|400]]
- è modello TD non autonomo TI (tempo invariante perché si suppone $\alpha$ e $\beta$ costanti)
