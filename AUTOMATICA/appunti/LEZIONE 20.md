### ESERCIZI: STUDIO STABILITA' ESTERNA
#### 0)
- Controllo se la condizione necessaria è soddisfatta
- Se non lo è, costruisco la tabella (essendo grado $3$)
- Applico il criterio di stabilità
	- Se gli elementi della prima colonna sono tutti di segno concorde (e diversi da zero), allora hanno tutti parte reale minore di zero e quindi è *esternamente stabile*
![[Pasted image 20220607173531.png|600]]

#### 1)
- Verifico se ci sono semplificazioni (guardando se ci sono zeri in comune)
- Verifico se è verificata la condizione necessaria
- Se è verificata, costruisco la tabella di Routh
![[Pasted image 20220607174241.png|600]]
#### 2)
- Qui ci sono semplificazioni
![[Pasted image 20220607174355.png|500]]
- Abbiamo un polinomio di secondo grado con tutte radici con parte reale minore di zero
#### 3)
- Non ci sono semplificazioni
- Non è verificata la condizione necessaria $\Rightarrow$ mancano dei termini (coefficienti)
	- Non ha tutte radici con parte reale $<0 \Rightarrow$ sistema *esternamente instabile*
![[Pasted image 20220607174637.png|500]]
#### 4)
- Parametro $\alpha$ reale
- Non cerco di capire il segno andando a calcolare esplicitamente le radici, ma piuttosto:
	- *Applico la regola di Cartesio*, perché ho un polinomio di secondo grado
		- Radici con parte reale minore di zero $\iff$ tutti i coefficienti di segno concorde e diversi da zero
		- Faccio un sistema per imporre le condizioni
![[Pasted image 20220607174932.png|500]]

#### 5)
- Semplificazioni: non banale perché il denominatore dipende da un parametro
	- Dovrei studiare tanti caso
	- Allora non lo faccio e osservo che il polinomio al numeratore è stabile, avendo una radice in $-3$
		- Da cui allora osservo il denominatore e guardo quando questo ha radici con parte reali maggiore di $0$, senza fare semplificazioni
	- In altre parole, *eventuali radici instabili (parte reale maggiore o uguale a 0), non possono essere semplificate*
> [!abstract] Nota
> Se avessimo avuto: $$ G(s) = \frac{s-1}{s^{3}+2^{2}+s+\alpha} $$ avremmo avuto lo zero del numeratore con parte reale maggiore di $0$, quindi potevano esserci semplificazioni instabili. Quindi era *necessario considerare separatamente i casi per la stabilità*
- Nel nostro caso: $G(s)$ ha tutti i poli con $Re<0 \iff$ denominatore ha tutte le radici con $Re < 0$
- Costruiamo quindi la tabella per sicurezza (anche se tipo $\alpha>0$ potrei già dirlo per rispettare la condizione necessaria)
![[Pasted image 20220607175802.png|600]]

---

# ANALISI SISTEMI LTI IN RAPPRESENTAZIONE INGRESSO/USCITA
- Studiamo il caso dei sistemi SISO

Abbiamo la derivata dell'ordine massimo del sistema è data dalla somma delle uscite precedenti (derivate di ordine più basso) e dalla somma degli ingressi e delle sue derivate
![[Pasted image 20220607180258.png|600]]

**(prima) Idea: passare alle equazioni di stato e poi applicare tutti i metodi già visti**
- cioè passare da una equazione differenziale a una equazione di stato

#### INGRESSO NON DERIVATO
Sappiamo già come muoverci (già visto), infatti in quel caso
$$
x(t) = \begin{bmatrix} y(t)  \\ \dot y(t)  \\  \vdots  \\  y^{n-1}(t) \end{bmatrix}
$$
#### IN GENERALE
Si utilizza la forma canonica di osservazione

## FORMA CANONICA DI OSSERVAZIONE
Si costruiscono le matrici generiche che sappiamo, ovvero:
$$
\begin{cases} \dot x = Ax +Bu  \\ y = Cx + Du \end{cases}
$$
In questo modo:
![[Pasted image 20220607180702.png|600]]

Dove i coefficienti $\alpha$ e $\beta$ si trovano nel generico sistema LTI TC (vedi forma generale scritta poco fa)

#### ESEMPIO
- Basta prestare attenzione ai coefficienti
- Poi posso subito passare alle matrici $A,B,C,D$
![[Pasted image 20220607181234.png|600]]
- uso questo metodo solo se mi servono esplicitamente le equazioni di stato, altrimenti cfr. Metodo successivo
---
## DOMINIO DI LAPLACE
L'alternativa per lavorare con sistemi LTI in rappresentazione ingresso uscita e trovare quindi la loro soluzione/analisi è passare al dominio di Laplace attraverso la trasformata
Infatti, facendo la derivata delle varie uscite $y(t)$ si ottiene:
![[Pasted image 20220607185500.png|500]]
In generale quindi **la generica derivata dell'uscita è data da**:
$$
\large \boxed{\mathcal{L}\{y^{(i)}\} = s^{i}Y(s) - s^{i-1}y(0)-\dots-s y^{(i-2)}(0)-y^{(i-1)}(0)}
$$
- Questo metodo è utile anche per risolvere equazioni differenziali, ad esempio il seguente è un sistema integratore:
![[Pasted image 20220607185943.png|400]]

#### FUNZIONE DI TRASFERIMENTO
Con il metodo visto si può facilmente trovare la funzione di trasferimento (o la risposta forzata):
- Ponendo le condizioni iniziali a $0$
![[Pasted image 20220607190454.png|500]]
- scrivo nel dominio di Laplace la risposta forzata a partire dall'ingresso
- se necessario faccio semplificazioni
	- utile ad esempio se devo studiare la stabilità esterna, perché ho una formula per $Y_{f}(t)$ 
		- E potrò derivare facilmente anche $\varphi(s)$ e $m(s)$ perché coincidono entrambi con il denominatore

