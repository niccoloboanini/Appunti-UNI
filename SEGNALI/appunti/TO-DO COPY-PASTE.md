### ESERCIZIO: PASSAGGIO H(Z) --> EQ. ALLE DIFFERENZE FINITE
Sceglieremo sempre $H(Z)$ formata da *un solo polo*.

Esempio (polo in $z=a$):
$$
H(Z) = \frac{1}{1-a\ z^{-1}} = \frac{z}{z-a}$$
Calcoliamo l'equazione alle differenze finite, ricordando che:
$$
H(Z) = \frac{Y(Z)}{X(Z)} = \frac{1}{1-a\ z^{-1}}
$$
Manipolando la frazione si può ottenere facilmente:
$$
Y(Z) \cdot (1-a \ z^{-1}) = X(Z)
$$
Moltiplicando:
$$
Y(Z) - a \ Y(Z) \ z^{-1} = X(Z) 
$$
Da cui si applica la *trasformata Z inversa* (ricordando ad esempio che $z^{-1}$ produce un ritardo)
$$
y[n] - a \ y[n-1] = x[n] 
$$
Isolando $y[n]$ si ottiene l'equazione alle differenze finite:
$$
\boxed{y[n] = a \ y[n-1] + x[n] }
$$
Che è la soluzione richiesta.

#### STABILITà
L'equazione appena ottenuta *non garantisce sempre la stabilità*, infatti:

Ricavando $h[n]$:
$$
h[n] = T(\delta[n])
$$
- ovvero come operatore $T$ applicato all'ingresso dato dall'impulso discreto unitario (ovvero la definizione di risposta impulsiva: come reagisce il sistema a un impulso unitario $\delta[n]$)
- Quindi come ingresso abbiamo $x[n] = \delta[n]$, ovvero
![[Pasted image 20220520115514.png|250]]

**Ci chiediamo quanto vale l'uscita, ovvero $y[n]$**

(nota: si riesce a calcolare l'uscita se si conosce l'ingresso a tale istante $n$ e l'uscita precedente... dato che non conosciamo in generale l'uscita precedente, si suppone la seguente:)
>> Ipotizziamo di avere un sistema in **quiete**: $y[n] = 0  \quad se \quad x[n]=0$

Ovvero nel nostro caso equivale ad avere:
$$
y[n] = 0  \quad , \quad n\leq 1
$$
Quindi per ora:
![[Pasted image 20220520120800.png|300]]

Procediamo quindi a calcolare $y[0]$, utilizzando l'equazione alle differenze finite ricavata:
$$
y[0] = a \ y[-1]+x[0] = 0+1 = 1
$$
Andando avanti:
$$
y[1] = a \ y[0] + x[1] = a \cdot 1 + 0 = a
$$
Ancora:
$$
y[2] = a \ y[1]+x[2] = a \cdot a + 0 = a^{2}
$$
Il pattern quindi è il seguente:
$$
y[n] = a^{n}  \quad , \quad a \geq 0
$$

Per cui mettendo insieme anche i valori negativi:
$$
\boxed{y[n] = a^{n} \ u[n]}
$$

Il risultato ottenuto è coerente infatti valgono le seguenti relazioni:
![[Pasted image 20220520121733.png|500]]
- dove le frecce indicano i legami di trasformata/antitrasformata
- dove $h[n]$ corrisponde all'uscita $y$ che ci siamo appena calcolati
- vale in particolare $H(Z)$ scegliendo una $ROC = \{z:|z|>a\}$, caratteristica di una sequenza monolatera destra (infatti $h$ è monolatera destra ($\triangle$))

> [!important] NOTA BENE ($\triangle$)
>se l'equazione alle differenze è una *equazione ricorsiva "in avanti"* come nel caso appena visto (in avanti: calcolo dell'uscita in base a quelle precedenti andando quindi in avanti come progressione degli indici) *implica risposta impulsiva monolatera destra* e inoltre *implica regione di convergenza di $H(Z)$ esterno del cerchio* 


#### STABILITà
1) controllo che $h[n] = a^{n}u[n]$ è assolutamente sommabile?
	>> Questo vale solo per alcuni valori di $a$, in particolare: $|a|<1$
2) ricordando che $\displaystyle H(Z)=\frac{z}{z-a}$ ha un polo in $a$ ha quindi $ROC = \{z:|z|>|a|\}$, ovvero esterni alla circonferenza su $a$. Dato che la $ROC$ deve includere la circonferenza unitaria, si deve scegliere $a<1$. Ecco graficamente:
![[Pasted image 20220520123010.png|500]]



