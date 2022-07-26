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

## D9
![[Pasted image 20220609153724.png|500]]
- dove per l'uscita si intende la risposta forzata $y_{f}(t)$
>> Studio della stabilità esterna (modo alternativo di dirlo)
>> 	Esistono ingressi limitati che fanno divergere solo se non è esternamente stabile

- Riscrivo in forma normale
- Individuo i coefficienti
- Applico la formula per la funzione di trasferimento $G(s)$
- Effettuo eventuali semplificazioni
	- Individuando eventuali poli nascosti
- Studio i poli di $G(s)$ semplificata: se sono tutti con $\text{Re}<0$ allora è esternamente stabile
![[Pasted image 20220609154106.png|600]]

## D10
![[Pasted image 20220609154132.png|600]]
- stesso procedimento dell'esercizio precedente
	- Solo che adesso abbiamo due poli (puramente immaginari) --> non tutti i poli con $\text{Re}< 0$ quindi esistono ingressi limitati che fanno divergere $(\star)$

$(\star)$ L'ingresso che fa violare la condizione di stabilità esterna è tale da andare in risonanza con i poli della $G(s)$
- Prendiamo quindi come ingresso limitato ad esempio $\sin(\omega_{0}t)\cdot 1(t)$, del tipo: $$ u(t) = \sin(\sqrt{10}\ t) \ 1(t) $$
>> Extra: verifichiamo che effettivamente diverge
>> Deve divergere: $Y_{f}(s) = G(s)U(s)$
>> 	Calcoliamo quindi la relativa trasformata $U(s)$
>> 	Mettiamo tutto insieme e verifichiamo (si va in risonanza, i poli puramente immaginari hanno molteplicità doppia --> compaiono quindi anche i modi con $t \cdot [\dots]$)

![[Pasted image 20220609154838.png|600]]

#### SISTEMI NON LINEARI
## D11
![[Pasted image 20220609154932.png|600]]
- Non lineare per il prodotto $ux$
- Studiare anche la stabilità (con il metodo della linearizzazione)

- Calcolo gli stati di equilibrio, ovvero individuo la relazione tra $x_{e}$ e $u_{e}$ (isolando uno delle due)
- Linearizzazione
	- Costruisco $Ae$ matrice Jacobiana (se lo stato ha dimensione $1$ come in questo caso allora è uno scalare invece di una matrice)
	- La calcoliamo nei punti $x$ e $u$ di equilibrio
- Individuo gli autovalori della matrice $Ae$ 
	- In questo caso avendo un solo valore studio il segno in base all'ingresso
		- Escludo i poli uguali a zero
![[Pasted image 20220609155701.png|600]]

## D12
![[Pasted image 20220609155719.png|600]]
- $y$ irrilevante per quello che devo trovare

- Individuo $f(x)$
	- Perché quando si annulla $f(x_{e})$ abbiamo equilibrio
- Trovo le soluzioni (in questo caso due)
	- Queste sono i punti di equilibrio del sistema non lineare

- Studio poi la stabilità, ancora con la matrice $Ae$ Jacobiana (in questo caso viene una matrice perché lo stato è composto da due elementi)
	- Calcolo la matrice nei punti $x_{e}$ di equilibrio
	- Calcolo infine $\varphi(s) = \det(sI-A_{e})$ per ogni punto di equilibrio
		- Concludo a seconda dei poli di $\varphi(s)$ sulla stabilità

![[Pasted image 20220609160831.png|600]]
![[Pasted image 20220609161139.png|600]]

## D13
![[Pasted image 20220609161200.png|600]]

- Calcolo la risposta libera $y_{\ell}(t)$
	- Attraverso l'antitrasformata di Laplace
- Ci costruiamo solo le matrici $A$ e $C$
	- $B$ e $D$ sono irrilevanti per quello che devo fare

>> Nota: non sempre bisogna calcolare l'intera risposta libera $y_{\ell}(t)$, perché ad esempio se il sistema fosse stabile internamente allora tutti i modi sarebbero limitati/convergenti e quindi la risposta libera sarebbe limitata.
>> Se ci fossero invece modi divergenti, allora sarebbe necessario calcolarla esplicitamente perché vuol dire che dipende fortemente dalle condizioni iniziali

- Cerco quindi i *modi* di evoluzione (ecco perché costruisco la matrice $A$)
	- Osservo i modi trovati: se come nell'esercizio ho modi sia divergenti che convergenti, allora $y_{\ell}(t)$ dipende dalle condizioni iniziali in qualche modo
![[Pasted image 20220609161955.png|600]]
![[Pasted image 20220609162358.png|600]]
![[Pasted image 20220609162430.png]]

