### ESERCIZIO PARTENDO DALLE DIFFERENZE FINITE
Sia:
$$
y[n] = 0.5 \ y[n-1] - 0.04 \ y[n-2 ] + 2 \ x[n]
$$
**Ci si chiede se il sistema è stabile**

- Abbiamo una equazione *ricorsiva in avanti*, quindi $h[n]$ è *monolatera destra*.
	- Questo implica che $H(Z)$ ha $ROC$ che è l'*esterno del cerchio*.
	- ![[Pasted image 20220521151406.png|200]]
		- Il raggio (minimo) del cerchio  è determinato dai *poli* della funzione di trasferimento
			- Per la stabilità, tali poli dovranno essere *interni al cerchio unitario*
				- In questo modo l'esterno del cerchio avente raggio il modulo massimo dei poli include la circonferenza unitaria
				- ![[Pasted image 20220521151650.png|550]]
				- (Dovrebbe venir fuori una regione anulare?)

> [!missing] Un esempio di non stabilità
> ![[Pasted image 20220521151909.png|250]] 
> Un polo (rappresentato dalla X), è esterno alla circonferenza unitaria

Troviamo la funzione di trasferimento applicando la trasformata Z
$$
Y(Z) = 0.5 \ z^{-1} Y(Z) - 0.04 \ z^{-2} Y(Z) + 2 X(Z)
$$
Da cui:
$$
Y(Z) = \left[ 1-0.5 \ z^{-1} + 0.04 \ z^{-2} \right] = 2 X(Z)
$$
Infine:
$$
\frac{Y(Z)}{X(Z)} = H(Z) = \frac{2}{1-0.5 z^{-1}+0.04z^{-2}}
$$
Che si può riscrivere esprimendo in $z$ (moltiplicando per $z^{2}$) invece di $z^{-1}$, come:
$$
H(Z) = \frac{2z^{2}}{(z-0.1)(z-0.4)}
$$
Ha poli (radici):
	- $z=0.1$
	- $z=0.4$
Sono *interne al cerchio unitario* $\Rightarrow$ il sistema è **stabile**

**Ci si chiede quale sia l'uscita dato un certo ingresso: $x[n] = 3 \delta[n] \longrightarrow y[n]?$
- Essendo l'ingresso un multiplo dell'impulso discreto unitario, l'uscita sarà anch'essa multipla della stessa quantità della risposta impulsiva
	- Ovvero: $x[n] = 3 \delta[n] \longrightarrow y[n] = 3h[n]$
Dobbiamo quindi calcolare $h[n]$ come trasformata Z inversa di $H(Z)$ e poi moltiplicare per $3$ il risultato. Già sappiamo che:

$$H(Z) = \frac{2z^{2}}{(z-0.1)(z-0.4)}  \quad , \quad ROC=\{z:|z|>0.4\}$$
Essendo una funzione razionale, so calcolare l'antitrasformata (conosco anche la $ROC$ di riferimento quindi apposto):
- fratti semplici:
![[Pasted image 20220521153912.png|500]]
- Isolando $H(Z)$:
![[Pasted image 20220521153947.png|500]]

- Da cui, eseguendo l'antitrasformata di tipo *monolatero destro*, si giunge a:
![[Pasted image 20220521154059.png|500]]

- Nota: abbiamo la somma di monolatere destre che è compatibile con la $ROC$ che era l'esterno di un cerchio
- Bisogna moltiplicare per $3$ per ottenere l'uscita desiderata (questa era la risposta impulsiva)


**Ci si chiede quale sia l'uscita dato un certo ingresso: $\displaystyle x[n] = 2 \cos \frac{\pi n}{3} \longrightarrow y[n]?$**
Facciamo comparire la frequenza del coseno, riscrivendo:
$$ 
x[n] = 2 \cos 2\pi \frac{1}{6}  \quad , \quad \text{quindi: } F_{0}=\frac{1}{6}
$$
Ricaviamo quindi $H(F)$ ricordando che:
$$
H(F) = \left. |H(Z) \right|_{\large z=e^{j2\pi F}}
$$
Dove $H(Z)$ l'avevamo già calcolata:
$$
\frac{Y(Z)}{X(Z)} = H(Z) = \frac{2}{1-0.5 z^{-1}+0.04z^{-2}}
$$
Pertanto sostituendo $z$ con $e^{j2\pi F}$:
$$
H(F) = \frac{2}{1-0.5 e^{-j2\pi F}+0.04 e^{-j2\pi F \cdot 2}}
$$
- funzione della variabile $F$
	- a noi basta il suo valore calcolato in $F_{0}=\frac{1}{6}$. Sostituendo questo valore al posto di $F$ ed esprimendo quindi il numero complesso come modulo e fase e quindi applicando eventualmente la simmetria hermitiana si ottiene: $$ H(F_{0})=2.40 e^{-j0.50}  $$
Da qui si ricava l'uscita come:
$$
y[n] = 2 \cdot (2.40) \ \cos (2\pi \frac{1}{6}n-0.50)
$$
- abbiamo usato la rappresentazione risposta in frequenza

**Ci si chiede quale sia l'uscita dato un certo ingresso: $\displaystyle x[n] = 5 \ u[n] \longrightarrow y[n]?$**
Vediamo qual è la rappresentazione più utile per calcolare l'uscita e ottenerla in forma chiusa (come nei casi precedenti)
Tra le $4$ possibili opzioni, scegliamo di calcolare l'uscita passando da $H(Z)$
![[Pasted image 20220521161320.png]]
	- negli altri casi c'è il rischio di ottenere una uscita non in forma chiusa (ovvero con infiniti termini da calcolare)

Andiamo perciò a trovare $Y(Z)$ per poi antitrasformare:
![[Pasted image 20220521161611.png|400]]


