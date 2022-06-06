# ANALISI MODALE
Ricordiamo che per un sistema LTI TC abbiamo trovato che esiste la seguente corrispondenza tra dominio del tempo e Laplace:
$$
e^{at} \longleftrightarrow \frac{1}{s-a}
$$
$$
\updownarrow
$$
$$
e^{At} \longleftrightarrow (sI-A)^{-1}
$$
Questo ci ha portato a trovare l'evoluzione libera:
$$
x_{\ell} = e^{At}x_{0} = \mathcal{L}^{-1} \{ (sI-A)^{-1} \}
$$
- da cui si può capire i modi di evoluzione del sistema
- dove abbiamo notato che $(sI-A)^{-1} = \frac{1}{\varphi(s)}Adj(sI-A)$
	- Ovvero l'inversa è un rapporto di polinomi tale che grado numeratore minore del grado del denominatore (strettamente propria)

#### POLINOMIO CARATTERISTICO
Il polinomio caratteristico $\varphi(s)$ può essere riscritto individuando i suoi zeri, che sono gli **autovalori $\lambda_{1}, \dots, \lambda_{k}$ con molteplicità $\mu_{1},\dots,\mu_{2}$**, e fattorizzando:
$$
 \varphi(s) = \prod_{i=1}^{k}(s-\lambda_{i})^{\mu_{i}}
$$
- Pertanto, *gli autovalori del polinomio caratteristico sono i poli della matrice inversa*, infatti: $(sI-A)^{-1} = \frac{Adj(sI-A)}{ \varphi(s)}$
- Quindi gli autovalori determinano l'evoluzione nel tempo dell'esponenziale di matrice $e^{At}$

>> Primo esempio: *Calcolo esponenziale di matrice*
>> ![[Pasted image 20220606115752.png|600]]
>> i modi di evoluzione sono associati agli autovalori

#### ESEMPIO 2
- calcolo $\varphi(s)$
- trovo gli zeri (autovalori)
- calcolo l'inversa $(sI-A)^{-1}$
- antitrasformo per trovare l'esponenziale di matrice $e^{At}$
- interpreto i modi di evoluzione e li classifico se serve (divervente, convergente etc...)
	- la molteplicità determina il modo di evoluzione
![[Pasted image 20220606120305.png|500]]

#### ESEMPIO 3: STESSO POLINOMIO CARATTERISTICO MA DIVERSA MATRICE
- $\varphi(s)$ viene come nell'esempio precedente
- cambia però l'evoluzione nel tempo (basta calcolare $(sI-A)^{-1}$)
- in origine avevo una molteplicità $2$ ma facendo l'inversa la **molteplicità si abbassa** e diventa $1$.
![[Pasted image 20220606120622.png|500]]
- Un solo modo di evoluzione in questo caso: il gradino

### POLINOMIO MINIMO
- Polinomio che rimane dopo le semplificazioni, per trovarlo si calcola:
![[Pasted image 20220606120802.png]]

#### esempio (precedente)
![[Pasted image 20220606121014.png|500]]
- ci aiuta a capire la molteplicità di ciascun autovalore e pertanto, *essendo gli autovalori dei poli del polinomio caratteristico possiamo applicare quanto visto in precedenza per capire i modi di evoluzione*
- Nell'esempio: la prima matrice ha **due modi di evoluzione**: $1$ e $t$
	- La seconda matrice ha **un solo modo**: 1

In generale quindi, **il polinomio minimo è un sottoinsieme del polinomio caratteristico**, ovvero:
$$
\varphi(s) = (s-\lambda_{1})^{\mu_{1}}(s-\lambda_{2})^{\mu_{2}} \dots (s-\lambda_{k})^{\mu_{k}}  \quad , \quad m(s) = (s-\lambda_{1})^{m_{1}}(s-\lambda_{2})^{m_{2}} \dots (s-\lambda_{k})^{m_{k}}
$$
$$
\text{Con } \boxed{m_{i} \leq \mu_{i}}  \quad , \quad m_{1} \geq 1
$$
- ciascun autovalore non può sparire come polo, ma la sua molteplicità può abbassarsi fino a scomparire (e al massimo se non si semplifica è pari alla molteplicità algebrica $\mu_{i}$)
> [!summary] DIMOSTRAZIONE DEL PERCHE' CIASCUN AUTOVALORE NON PUO' SPARIRE
> ![[Pasted image 20220606122550.png|500]]
Rimane alla fine un $\lambda_{i}$ (polo con molteplicità almeno $1$)

## MODI NATURALI
![[Pasted image 20220606122920.png|600]]

- Analogamente a quanto visto in precedenza solo che adesso teniamo conto del polinomio minimo $m(s)$
- gli elementi della matrice esponenziale sono una combinazione lineare dei modi di evoluzione del sistema

