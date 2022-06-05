## FUNZIONE RAZIONALI
Consideriamo una funzione razionale:
$$
F(s) = \frac{b(s)}{a(s)}
$$
I calcoli delle antitrasformate si distinguano a seconda del rapporto che c'è tra il grado del numeratore e il grado del denominatore.
In particolare:
$$
\boxed{\text{grado } b(s)  < \text{grado } a(s) \quad \Rightarrow F(s) \text{ è strettamente propria}}
$$
$$
\boxed{\text{grado } b(s)  = \text{grado } a(s) \quad \Rightarrow F(s) \text{ è semplicemente propria}}
$$
- Si suppone inoltre che non si possano fare semplificazioni tra numeratore e denominatore (ovvero $b(s)$ e $a(s)$ sono *coprimi* tra loro)
- Le radici del numeratore $a(s)$ vengono dette *zeri* della funzione
- Le radici del denominatore $a(s)$ vengono dette *poli* della funzione


Inoltre, *il termine di grado massimo del denominatore nella forma standard che consideriamo lo prendiamo uguale a $1$*. Se $F(s)$ non avesse questa caratteristica in partenza, ci si può sempre ricondurre a quel caso, ad esempio:
![[Pasted image 20220605150855.png|500]]
- ovvero $a(s)$ è un polinomio *monico*

## TEOREMA DEI RESIDUI
### CASO POLI DISTINTI
$F(s)$, nelle ipotesi di strettamente propria con poli distinti, può essere sempre riscritta in fratti semplici come:
$$
F(s) = \sum_{i=1}^{n} \frac{K_{i}}{s-p_{i}}
$$
Il generico $K_{i}$ vengono detti *residui*, e ognuno è associato al relativo polo $p_{i}$. Si può calcolare secondo il teorema in questo modo:
$$
\large K_{i} = \lim_{s \to p_{i}} (s-p_{i})\cdot F(s)
$$

Infatti:
![[Pasted image 20220605151850.png]]

#### ESEMPIO:
![[Pasted image 20220605152147.png|500]]
- utile perché non devo impostare un sistema che potenzialmente potrebbe avere molte equazioni

### il teorema e l'ANTITRASFORMATA
Partendo dai fratti semplici: $F(s) = \sum_{i=1}^{n} \frac{K_{i}}{s-p_{i}}$, possiamo antitrasformare ciascun termine, così da ottenere $f(t)$:
$$
f(t) = \mathcal{L}^{-1} \bigg\{\sum_{i=1}^{n} \frac{K_{i}}{s-p_{i}}\bigg\} = \sum_{i=1}^{n} K_{i} \mathcal{L}^{-1} \bigg\{ \frac{1}{s-p_{i}} \bigg\} = \Large \sum_{i=1}^{n} K_{i}e^{p_{i}} \ 1(t)
$$
dove:
- $e^{p_{1}t} 1(t), \dots , e^{p_{n}t} 1(t)$ sono i **modi di evoluzione** della funzione $F(s)$
	- e $K_{i}$ sono i residui relativi

Quindi, data una funzione razionale in Laplace dotata di poli sono associati dei segnali del tempo che caratterizzano i modi di evoluzione esponenziali. Essi sono in corrispondenza biunivoca con i relativi poli.
- Quindi dato un poli in Laplace si deduce com'è fatto il corrispondente segnale nel tempo
	- (anche senza calcolare i rispettivi residui posso capire in generale com'è l'andamento: convergente, divergente etc..)

L'obiettivo quindi è capire come *prevedere* l'evoluzione nel tempo dell'esponenziale, ovvero capire come influisce la posizione del polo sul piano complesso per l'evoluzione del segnale nel tempo
- ovvero capire la corrispondenza $polo \longleftrightarrow esponenziale$ per capire il comportamento, ovvero: $$ p_{i} \longleftrightarrow e^{p_{i}t}\ 1(t) $$
## CORRISPONDENZE POLO - ESPONENZIALE
### POLO REALE NEGATIVO
Consideriamo $p_{i} < 0$. Avremo in generale:
$$
p_{i} \longleftrightarrow e^{p_{i}t} \ 1(t)
$$
- ovvero un esponenziale **convergente a zero**
![[Pasted image 20220605161645.png|400]]
- più il polo si avvicina a $0$ più la convergenza diventa lenta
### POLO REALE ZERO
Consideriamo $p_{i} = 0$. Avremo in generale:
$$
p_{i} \longleftrightarrow e^{p_{i}t} \ 1(t) = e^{0t} \ 1(t) = 1(t)
$$
- ovvero un esponenziale **convergente costante a uno (gradino)**
![[Pasted image 20220605161841.png|400]]
- segnale limitato ma non convergente a zero

### POLO REALE POSITIVO
Consideriamo $p_{i} > 0$. Avremo in generale:
$$
p_{i} \longleftrightarrow e^{p_{i}t} \ 1(t)
$$
- ovvero un esponenziale **convergente divergente a $\infty$**
![[Pasted image 20220605161948.png|400]]
- sempre più divergente se $p_{i}$ è grande

---
### POLI COMPLESSI
Per capire l'evoluzione nel tempo, conviene prendere a *coppie* i poli *complessi coniugati*.
Se prendiamo un polo complesso del tipo: $p_{i} = \sigma_{i} + j\omega_{i}$ allora a esso sono associati: il coniugato, il residuo e il coniugato del residuo, ovvero:
$$
\begin{cases}
p_{i} = \sigma_{i} + j \omega_{i} \longleftrightarrow K_{i} = \alpha_{i}+j \beta_{i} \\
\overline{p_{i}} = \sigma_{i} - j \omega_{i} \longleftrightarrow \overline{K_{i}} = \alpha_{i} - j \beta_{i}
\end{cases}
$$
I **modi di evoluzione** associati sono i seguenti:
$$
P_{i} \longleftrightarrow e^{p_{i}t} 1(t) = e^{(\sigma_{i}+j\omega_{i})t}1(t) = e^{\sigma_{i}t} e ^{j \omega_{i}t}1(t) = e^{\sigma_{i}t} \cdot [\cos(\omega_{i}t)+ j \sin (\omega_{i}t)]1(t)
$$
$$
\overline{P_{i}} \longleftrightarrow e^{\overline{p_{i}}t} 1(t) = e^{(\sigma_{i}-j\omega_{i})t}1(t) = e^{\sigma_{i}t} e ^{-j \omega_{i}t}1(t) = e^{\sigma_{i}t} \cdot [\cos(\omega_{i}t)- j \sin (\omega_{i}t)]1(t)
$$
Considerando anche i residui, possiamo mettere tutto insieme:
$$
K_{i}e^{p_{i}t}1(t) + \overline{K_{i}}e^{\overline{p_{i}}t}1(t)
$$
Ovvero:
$$
K_{i} \ e^{\sigma_{i}t} \cdot [\cos(\omega_{i}t)+ j \sin (\omega_{i}t)]1(t) + \overline{K_{i}} \ e^{\sigma_{i}t} \cdot [\cos(\omega_{i}t)- j \sin (\omega_{i}t)]1(t)
$$
- dove i residui $k_{i}$sono numeri complessi della forma: $\alpha_{i} \pm j \beta_{i}$ 

Combinandoli algebricamente in maniera corretta, ci si rende conto che *la parte immaginaria scompare*, infatti rimane soltanto la parte reale:
![[Pasted image 20220605164038.png]]

- quindi una volta calcolato il polo e il residuo, con questa formula *possiamo capire il modo di evoluzione* quando abbiamo appunto poli complessi

Quindi, a una coppia di poli complessi coniugati sono associati due modi di evoluzione, ovvero:
![[Pasted image 20220605164441.png]]

Ricordando che $p_{i} = \sigma_{i}+j \omega_{i}$:
- la parte reale contribuisce con un esponenziale
- la parte immaginaria contribuisce con una oscillazione (seno/coseno)

>> Basta calcolare i poli per capire i modi di evoluzione. La differenza col caso reale è che compare anche un termine oscillatorio, introdotto dalla parte immaginaria

### POLI COMPLESSI CON PARTE REALE NEGATIVA
Consideriamo due poli complessi coniugati del tipo con $\sigma_{i} < 0$
- L'esponenziale per quanto già visto, *converge a zero*
- Mettendo insieme si giunge a un **esponenziale oscillante convergente a zero**, del tipo:
$$
\sin(\omega_{i}t)e^{\sigma_{i}t}1(t) \quad , \quad \cos(\omega_{i}t)e^{\sigma_{i}t}1(t)
$$
![[Pasted image 20220605165114.png|500]]
- dove in figura è mostrato l'andamento del coseno
		- Da notare che il grafico "va sotto zero" come ci può aspettare (anche se non è disegnata l'asse $x$)

### POLI COMPLESSI CONIUGATI PURAMENTE IMMAGINARI
- Poli con parte reale uguale a zero, cioè: $\sigma_{i} = 0$
- I poli sono della forma: $p_{i} = j \omega_{i} \quad , \quad \overline{p_{i}} = -j \omega_{i}$
Si ottengono **modi completamente oscillanti e limitati**, della forma:
$$
\sin(\omega_{i}t) \quad , \quad \cos(\omega_{i}t)1(t)
$$
![[Pasted image 20220605165720.png|500]]

### POLI COMPLESSI CONIUGATI CON PARTE REALE POSITIVA
- Ragionando come nei casi precedenti si arriva a: $$ \sin(\omega_{i}t)e^{\sigma_{i}t}1(t) \quad , \quad \cos(\omega_{i}t)e^{\sigma_{i}t}1(t) $$
Con $\sigma_{i}>0$.
- **Oscillanti (perché c'è la parte immaginaria) e divergenti (esponenziale positivo)**
![[Pasted image 20220605170037.png|500]]

---
#### RIASSUMENDO
![[Pasted image 20220605170120.png|600]]

![[Pasted image 20220605170254.png|600]]