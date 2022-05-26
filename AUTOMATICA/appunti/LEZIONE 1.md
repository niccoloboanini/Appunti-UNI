# INTRODUZIONE AL CORSO

## SISTEMA DINAMICO
#### SISTEMA
Complesso di elementi connessi tra loro che si comporta come un unico oggetto che interagisce con il mondo esterno
#### SISTEMA DINAMICO
Sistema che evolve nel tempo. Di questi si occupa l'automatica

## ARGOMENTI
1) MODELLISTICA: descrizione matematica del sistema
2) ANALISI: studio dell'evoluzione/interazione con l'esterno nel tempo dei sistemi dinamici
3) CONTROLLO: progetto di sistemi che si comportano autonomamente

## ESEMPI di MODELLI
- Scolastico
- Page Rank
- Epidemiologico

## INTERAZIONI CON L'ESTERNO
Un sistema interagisce con l'esterno grazie a:
- Ingressi 
	- Manipolabili (cioè previsti): $u \to$  (macchina: freno, acceleratore...)
	- Non manipolabili (imprevedibili/di disturbo): $d \to$ (macchina: condizioni meteorologice, problemi...)
- Uscite $y$

![[Pasted image 20220526120357.png|300]]


## CONTROLLO
- Alla base c'è il concetto di *feedback* (o sistema di retroazione)
- Si occupa di gestire gli ingressi manipolabili
- Esempio: cruise control che regola la velocità, in generale

Il sistema di controllo cerca di adattare il più possibile il valore di $y$ al valore desiderato $y^O$, tenendo conto dei disturbi $d$ e cercando quindi di manipolare al meglio gli ingressi $u$.
![[Pasted image 20220526122040.png|300]]

Il sistema da controllare è indicato con ${P}$

Sistema ad **anello chiuso**
![[Pasted image 20220526123626.png|400]]
- Il comportamento di uscita diventa l'ingresso per l'istante successivo per il controllo


Altro esempio: *robot mobile* (evitare gli ostacoli durante lo spostamento) 