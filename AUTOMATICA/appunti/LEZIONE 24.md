# ESERCITAZIONE
## D3
Trovare (se esiste) valore asintotico della risposta impulsiva di un sistema LTI
> Bisognerà capire i modi di evoluzione

- Verifico se ci sono semplificazioni
- Calcolo i poli di $a(s)$ (denominatore)
- Classifico i poli in base alla loro posizione sul piano complesso
- Determino i modi di evoluzione
	- Concludo sull'esistenza o meno di $\lim_{t \to \infty} g(t)$
		- Ad esempio applicando il teorema del valore finale
![[Pasted image 20220609123251.png|500]]

## D4
![[Pasted image 20220609123323.png]]
> Trovare in pratica il comportamento asintotico della risposta forzata (limitata, divergente etc..)

- Calcolo la risposta forzata in Laplace: $Y_{f}(s) = G(s)U(s)$
	- Dove $U(s)$ lo troviamo con la trasformata di $u(t)$
- Adesso posso esplicitare $Y_{f}(s)$
	- *Non sommare*
	- Tenere separate le due parti (proprietà distributiva) $\checkmark$ 
		- Così da capire ogni termine come si comporta per ogni ingresso (risposta forzata)
- Studio ciascun termine (addendo)
	- Guardo dove sono i poli (e la relativa molteplicità)
	- Trovo i corrispondenti modi di evoluzione
- Individuo eventuali modi divergenti
	- Se ci sono, posso capire se la risposta forzata di un polo diverge e quindi il comportamento asintotico in generale diverge
![[Pasted image 20220609124225.png|700]]
#### MODO ALTERNATIVO
Dalle considerazioni fatte sulla stabilità esterna, sappiamo che $G(s)$ ha un polo in zero quindi non è esternamente stabile (perché per stabilità esterna tutti i poli devono avere $\text{Re}<0$)
- Un sistema con polo in zero non è asintoticamente stabile perché con in ingresso un gradino entra in risonanza e diverge (componente e rampa)

## D5
![[Pasted image 20220609124712.png|600]]
##### PRIMO MODO
- Polinomio minimo
	- Autovalori e relativa molteplicità
	- $[\dots]$
#### MODO ALTERNATIVO
- È già in forma standard $\checkmark$
- Essendo in rappresentazione ingresso uscita, sappiamo che $m(s) = \varphi(s) = s^ {2}-\alpha_{1}s-\alpha_{0}$
	- Trovo facilmente $\alpha_{1}$ e $\alpha_{0}$ osservando l'equazione di partenza
	- Individuo esplicitamente $m(s)$ e trovo le radici (autovalori)
	- Trovo i relativi modi di evoluzione
![[Pasted image 20220609125308.png|600]]

## D6
![[Pasted image 20220609125331.png|600]]
- Scrivo il sistema in forma normale
- Seguo procedimento esercizio precedente
	- Qui abbiamo molteplicità $2$ quindi cambia solo in questo
![[Pasted image 20220609125745.png|500]]

## D7
![[Pasted image 20220609125808.png|500]]
- Scrivo esplicitamente le matrici che rappresentano il sistema $A,B,C,D$
- Calcolo $\varphi(s)$ e se serve $m(s)$
	- In questo caso posso già concludere perché abbiamo un autovalore con $\text{Re}>0$ quindi è internamente instabile
- Stabilità esterna (se verifico che è asintoticamente stabile so che implica stabilità esterna; in questo caso però non lo so a priori, perché ho un autovalore stabile e l'altro no --> devo calcolare la funzione di trasferimento)
	- Calcolo quindi la funzione di trasferimento
	- Guardo i poli e concludo sulla stabilità

![[Pasted image 20220609130514.png|600]]
Si nota che c'è una semplificazione
- il polo in $1$ si semplifica --> autovalore nascosto
![[Pasted image 20220609130714.png|600]]