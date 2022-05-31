### ESERCIZI: PASSAGGIO ALLE EQ. DI STATO (SLIDE 94)
#### 3) 
 ![[Pasted image 20220531122458.png|500]]

#### 4)
- Riscrivo innanzitutto in forma normale
- singolo ingresso $\to \text{B}$ matrice colonna 
![[Pasted image 20220531122819.png|500]]

#### TEMPO CONTINUO (autonomo oppure ingresso non derivato)
#### 7)
- $y(t)$ come prima variabile di stato
![[Pasted image 20220531123111.png|500]]

#### 8)
- caso TV
- ingresso compare ma non derivato $m=0$
![[Pasted image 20220531124004.png|500]]


# SIMULAZIONE DEI SISTEMI DINAMICI
Conoscendo:
- il modello matematico
- la condizione iniziale $x(t_{0}) = x_{0}$
- come l'ambiente esterno influisce sul sistema (ingresso nell'intervallo d'interesse, ovvero: $u(t)$ in $[t_{0},t_{f}]$)

Ci si chiede come calcolare (numericamente) l'**andamento dello stato $x(t)$ e dell'uscita $y(t)$** nell'intervallo di tempo d'interesse
- Esempio: meteo ---> conosco com'è il tempo oggi e il modello matematico (eq. diff). Studio come si evolverà lo stato del sistema (temperatura, umidità, etc...)

In caso TD:
![[Pasted image 20220531124620.png|300]]

Caso TC:
- equazioni differenziali: più complesso (problema di Cauchy) :/
- Si cerca una *soluzione approssimata*
	- Affetto da errore di quantizzazione
- Si utilizzano metodi numerici, come il **metodo di Eulero**
	- si esegue in generale una discretizzazione (il tempo continuo diventa discreto t.c. Sia una approssimazione valida --> è un campionamento)
		- Da qui si scrivono le equazioni alle differenze

