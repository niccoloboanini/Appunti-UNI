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
	- (indipendentemente dalla stabilità anche se sarà utile il calcolo in caso di stabilità. In particolare il regime permanente ci fornisce informazioni utili quando il sistema che stiamo studiando è stabile. Vedi dopo)

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
Considerazioni importanti che mettono in collegamento quanto visto adesso con la stabilità.
![[Pasted image 20220608175438.png]]

![[Pasted image 20220608175603.png|600]]
Basta osservare il $\lim_{t \to 0} y_{\tiny f}(t)$:
- Nel caso di **stabilità esterna abbiamo**: $y_{f}(t) = \cancelto{0}{y_{f}^{G}(t)}+y_{f}^{U}(t)$ >> la *risposta forzata* tende al regime permanente (dato che ci rimane: $y_{(t)}=y_{\ell}(t)+y_{f}^{U}(t)$)
- Nel caso di **stabilità asintotica** invece: $y_{(t)} = \cancelto{0}{y_{\ell}(t)} + \cancelto{0}{y_{f}^{G}(t)}+{y_{f}^{U}(t)}$ >> la *risposta complessiva* tende al regime permanente
	- Perché se è stabile asintoticamente è anche stabile esternamente
	- In più la risposta libera $\cancelto{0}{y_{\ell}(t)}$ 

>> Il regime permanente dà informazioni circa l'andamento asintotico di un sistema stabile.


## REGIME PERMANENTE PER SEGNALI D'INGRESSO TIPICI

### GRADINO
#### RISPOSTA IN CONTINUA
- DEFINIZIONE: Regime permanente in risposta a un ingresso costante a gradino

Si suppone che $G(s)$ non abbia poli in $0$ così da avere poli distinti e rientrare nelle ipotesi e fare la scomposizione in fratti semplici
- In particolare, la scomposizione di $Y_{f}^{G}(s)$ non mi interessa per il momento; invece la scomposizione di $Y_{f}^{U}(s)$ è $\tilde K / s$ perché abbiamo un unico polo dell'ingresso (in $0$)
	- Mi focalizzo soltanto su com'è fatto il regime permanente (che è quello che mi interessa)
- $\tilde K$ è al solito calcolabile con la formula dei residui
![[Pasted image 20220609114847.png|600]]

Mandando in ingresso al sistema un gradino, abbiamo in uscita come regime permanente ancora un gradino di ampiezza originale $U_{0}$ moltiplicata per $G(0)$  (infatti antitrasformando $\tilde K /s$ è $G(0)U_{0} \ 1(t)$)
- Questo nelle ipotesi che l'ingresso non abbia poli in zero
- In altre parole come detto, la risposta forza tenderà a un regime permanente che è ancora un gradino nelle ipotesi fatte
- Ci sarà all'inizio anche un po' di transitoria ma poi svanisce a zero e rimane solo la permanente

$G(0)$ viene detto *guadagno in continua*
![[Pasted image 20220609115010.png|500]]
Quindi per calcolare il guadagno per sistemi SISO (quelli degli esercizi), una volta ottenuta $G(s)$ 
basta calcolarla per $s=0$, ovvero: $\boxed{\left . G(s) \right |_{s=0} = G(s)}$ 
##### ESEMPIO DI CALCOLO DEL GUADAGNO IN CONTINUA
- Controllo che $G(s)$ non abbia poli in zero
- Eseguo eventuali semplificazioni
- Se sono arrivato fin qui, allora conosco già la forma del regime permanente: $y_{f}^{U}(t) = G(0)U_{0}1(t)$
- Calcolo $\left . G(s)\right |_{s=0}$
	- Se viene $>0$ abbiamo un guadagno, altrimenti una attenuazione
- Controllo se il sistema è esternamente stabile
	- Ad esempio con i metodi algebrici oppure calcolando i poli di $G(s)$
- Posso scrivere eventualmente l'evoluzione asintotica della risposta forzata $\lim_{t \to \infty} y_{f}(t)$
![[Pasted image 20220609115928.png|600]]
