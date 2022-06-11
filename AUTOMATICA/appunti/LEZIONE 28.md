### ESEMPIO: CONTROLLO DI POSIZIONE
- L'uscita è rappresentata dalla posizione del carrello $y(t)$
- L'ingresso (da controllare) è la spinta da dietro $u$
- Esiste l'attrito (viscoso) $b$
- Il carrello ha massa $M$

Si vuole portare il carrello in una posizione desiderata $Y_{0}$ con il controllo $u$ a partire da una certa posizione di partenza $y(0)$
![[Pasted image 20220611125657.png|300]]
Dobbiamo quindi far accadere che: $$ \lim_{t \to \infty} y(t) \approx Y_{0} $$
Supponiamo di aver accesso allo stato per agire sulla legge del controllo
- Lo stato è come al solito: composto da due componenti $x(t)=\begin{bmatrix} x_{1}(t) \\ x_{2}(t) \end{bmatrix}=\begin{bmatrix} y(t)  \\ \dot y(t) \end{bmatrix}=\begin{bmatrix} \text{posizione}  \\ \text{velocita'} \end{bmatrix}$
	- Conoscere lo stato significa sapere a ogni istante $t$ la posizione e la velocità del carrello

Sappiamo già per questo sistema che:
(funzione di trasferimento in cui si vuole ricavare l'uscita, infatti $C=[1 \ \ 0]$)
![[Pasted image 20220611130253.png|500]]

Sappiamo per le specifiche di progetto che:
$$
u(t) = -F x(t) + Hy^{o}(t)
$$
- Il guadagno in feedback $F$ avrà la stessa dimensione del vettore di stato, quindi: $F=\begin{bmatrix} f_{1} & f_{2} \end{bmatrix}$
- $H$ invece è uno scalare (sistema SISO)
Totale: $3$ parametri da controllare $\to f_{1},f_{2},H$ 

#### PRIMO PASSO: polinomio caratteristico a ciclo chiuso
![[Pasted image 20220611131014.png|600]]
Come si nota, abbiamo un polinomio a ciclo chiuso in cui possiamo agire direttamente sui parametri moltiplicativi alla variabile di riferimento $s$. In questo modo posso arbitrariamente gestire la stabilità perché posso modificare gli zeri (ovvero i poli della funzione di trasferimento a ciclo chiuso in questo caso)
- Se avessimo usato il polinomio ad anello aperto, avrei ottenuto $$ \varphi(s) = s^{2}+s $$ su cui non avrei potuto far niente se non concludere che veniva un sistema marginalmente stabile (osservando gli zeri)
- Adesso invece con quelli che ho rinominato $a_{1}^{*}$ e $a_{2}^{*}$ posso regolarmi, perché dipendono da $f_{i}$ ovvero gli elementi della matrice $F$ di controllo/guadagno in feedback

Basta applicare Cartesio