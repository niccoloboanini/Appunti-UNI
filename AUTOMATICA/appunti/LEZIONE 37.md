## ESERCIZIO: RETROAZIONE SULL'USCITA
![[Pasted image 20220616150623.png]]

### 0)
- Mi scrivo le matrici $A,B,C$
![[Pasted image 20220616150712.png]]
### A)
> $\varphi(s)$ e $G(s)$

- Calcolo il determinante secondo la prima riga (per esempio)
- Fattorizzo il polinomio
	- Essendo di grado $3$, faccio una prima fattorizzazione e poi eguaglio i coefficienti $a$,$b$ scelti
- Sempre utile fattorizzarlo infine secondo le proprie radici
	- Dagli autovalori capisco se è stabile oppure no (mi avvantaggio per dopo)

- Calcolo poi $G(s)$ (l'aggiogata ce l'ho di già)
	- Conviene fare il prodotto partendo dalle matrici con più zeri presenti
	- *Verifico anche se ci sono semplificazioni*

![[Pasted image 20220616151253.png]]
![[Pasted image 20220616151410.png|500]]

### B)
- Facile se abbiamo risposto in maniera completa ad A)  (con le semplificazioni)
	-  Infatti per $\alpha=-1$ avevamo semplificazioni, quindi vuol dire che è presente un autovalore nascosto (instabile in questo caso)
![[Pasted image 20220616151930.png]]
##### FINE STUDIO PARAMETRICO
### C)
- Cerchiamo $K$ stabilizzanti (asintotici a ciclo chiuso)
- Abbiamo retroazione sull'uscita quindi utilizzeremo la formula adeguata
	- $\varphi_{h}(s)=1$ perché come visto in B) non ci sono autovalori nascosti per $\alpha \neq -1$ 
![[Pasted image 20220616152212.png]]
Vediamo per quali $K$ abbiamo stabilità asintotica in ciclo chiuso
- Costruisco la tabella di Routh perché ho un polinomio di $3°$ grado
	- $\varphi^{*}(s)$ asintoticamente stabile $\iff$ tutti gli elementi della prima colonna ha lo stesso segno 
		- Risolviamo il sistema di disequazioni
			- Osservando che il denominatore della seconda disequazione deve essere positivo quindi si riduce allo studio del solo numeratore (che è semplice perché di secondo grado)
			- considero solo $K \in \mathbb{R}$
![[Pasted image 20220616152733.png]]

### D)
- Progetto per rispettare le specifiche: 
	- stabilità asintotica in ciclo chiuso (già fatto $\checkmark$)
	- inseguimento perfetto in riferimento costante
		- Scrivo la funzione di trasferimento in caso di retroazione algebrica sull'uscita (vedi formula)
		- Calcolo in zero
		- Trovo $H$ (in funzione di $K$)
![[Pasted image 20220616153112.png|600]]
- Scelgo un $K$ arbitrario per trovare un valore (numero) anche per $H$

### E) 
- Riferimento sinusoidale (applico teorema risposta in frequenza per segnali tipici)
	- Applico la formula del teorema della risposta in frequenza (ricordando che ho un sistema in ciclo chiuso: quindi l'ingresso è il riferimento e l'uscita è $y$ e ha funzione di trasferimento $G^{*}_{y^{\text{o}}y}$)
![[Pasted image 20220616153243.png]]
Prendendo gli stessi $H$ e $K$ dell'esercizio D), si ottiene:
- Calcolo alla fine la risposta in frequenza con $\omega_{0}=1$
	- Cerco $\text{Re}$ e $\text{Im}$
	- Li metto nella formula di $y_{f}^{Y^{o}}(t)$
![[Pasted image 20220616153710.png]]

---
