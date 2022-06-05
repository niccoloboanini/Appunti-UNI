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
- ovvero capire la corrispondenza $polo \longleftrightarrow esponenziale$ per capire il comportamento
