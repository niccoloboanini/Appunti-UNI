### ESERCIZIO 2) (PENDOLO)
Applichiamo il criterio della linearizzazione al problema del pendolo già visto, che aveva due punti di equilibrio (a seconda della parità di $k \pi$).
Partiamo dunque dalle equazioni di stato e dai punti di equilibrio
![[Pasted image 20220608163432.png|400]]

Dove $f(x)$ si può esplicitare facilmente:
![[Pasted image 20220608163507.png|500]]
Costruiamo la matrice Jacobiana:
![[Pasted image 20220608163705.png|600]]

Troviamo ora la matrice della dinamica linearizzata, che cambia come già visto a seconda del punto di equilibrio di riferimento
- Primo equilibrio: $k \text{ pari}$ (verticale in basso)
- Secondo equilibrio: $k \text{ dispari}$ (verticale in alto)

#### primo equilibrio
![[Pasted image 20220608163929.png|600]]
Da cui posso calcolare tutti gli oggetti necessari per calcolare la stabilità (ovvero $\varphi_{e}(s)$):
![[Pasted image 20220608164253.png|600]]

#### SECONDO EQUILIBRIO
Analogamente al caso precedente (cambia solo il segno del coseno)
![[Pasted image 20220608164644.png|600]]

---

## RISPOSTA IN CONTINUA E IN FREQUENZA
Utile per capire *in modo immediato* *l'uscita* ovvero la risposta dei sistemi LTI con in ingresso dei *segnali tipici (gradino [risposta in continua] e sinusoide [risposta in frequenza])*

Partiamo dalle seguenti (classiche) considerazioni:
![[Pasted image 20220608173308.png|500]]

Facciamo anche le seguenti ipotesi, così da poter scomporre in fratti semplici:
![[Pasted image 20220608173502.png|600]]
- dove il primo addendo riguarda i termini relativi ai poli della funzione di trasferimento (in particolare $a(s)$)
- dove il secondo addendo riguarda i termini relativi ai poli dell'ingresso (in particolare $b(s)$)
*Abbiamo così scomposto la risposta forzata*

Rinominiamoli così:
![[Pasted image 20220608173837.png|500]]
- nelle *ipotesi di poli distinti tra funzione di trasferimento e ingresso*
	- (indipendentemente dalla stabilità anche se sarà utile il calcolo in caso di stabilità)

Per linearità, posso calcolare i due contributi nel tempo tramite l'antitrasformata
- Si ottiene così:
	- una parte di *regime transitorio* (parte di risposta forzata che dipende dalla funzione di trasferimento)
	- una parte di *regime permanente* (parte di risposta forzata che dipende dall'ingresso)
Quindi:
![[Pasted image 20220608174126.png|600]]
- transitorio perché se il sistema è esternamente stabile allora la $G(s)$ avrà poli $<0$ e quindi antitrasformando vengono modi convergenti (e quindi tende a $0$)
### ESEMPIO:
- notando che il polo in $-1$ viene dalla funzione di trasferimento $G(s)$ e il polo in $0$ viene dall'ingresso $U(s)$
![[Pasted image 20220608174635.png|600]]
![[Pasted image 20220608175241.png|200]]

#### STABILITà E REGIME PERMANENTE
![[Pasted image 20220608175438.png]]
![[Pasted image 20220608175603.png|600]]
 