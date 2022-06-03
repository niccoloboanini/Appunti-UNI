#### Nota sulla regione di convergenza
Viene indicata con $\sigma$ che viene detta **ascissa di convergenza**
![[Pasted image 20220603125224.png|300]]
## PROPRIETA' DELLA TRASFORMATA

### 1) LINEARITA'
(già di per sé l'integrale è un operatore lineare)
![[Pasted image 20220603125306.png|500]]

### 2) TRASLAZIONE IN FREQUENZA
(compare un esponenziale nel tempo)
![[Pasted image 20220603125858.png|600]]
- moltiplicare per un esponenziale nel tempo causa una traslazione in frequenza

### 3) DERIVATA IN FREQUENZA
Prendendo $t$ come costante quando facciamo la derivata rispetto a $s$ e poi portando fuori dall'integrale:
![[Pasted image 20220603131454.png|600]]
- moltiplicare per $t$ nel tempo equivale a derivare nel dominio di Laplace

### 4) DERIVATA NEL TEMPO
- Proprietà duale (equivale a moltiplicare per $s$ in frequenza, tenendo conto della condizione iniziale $f(0)$)
- Sfruttiamo alcune proprietà come la derivata del prodotto

La dimostrazione si esegue calcolando $\displaystyle \int_{0}^{\infty} (f(t) e^{-st}) \,dt$ in due modi, e poi uguagliandoli 
- il primo modo si fa sfruttando la derivata del prodotto
- il secondo modo si fa l'integrale della derivata
![[Pasted image 20220603132923.png|600]]
Infatti:
![[Pasted image 20220603133235.png|500]]
- Nota: $s$ funge da *operatore di derivazione*
**- Ci permette questa proprietà di passare dalle equazioni differenziali a equazioni algebriche nel dominio di Laplace**

### 5) INTEGRAZIONE NEL TEMPO
Dalla $4$, si può interpretare $s$ come operatore di derivazione. Quindi per l'integrazione *prendiamo $1/s$* come operatore.
![[Pasted image 20220603133540.png|600]]

### 6) CONVOLUZIONE
- vedi definizione di convoluzione in proprietà 5
![[Pasted image 20220603133723.png|600]]
- convoluzione nel tempo $\longleftrightarrow$ prodotto in Laplace
**- utile per la risposta forzata**

## [...] TRASFORMATE FONDAMENTALI

### ESPONENZIALE CAUSALE
![[Pasted image 20220603130349.png|600]]

### SENO
Sfruttando le formule di Eulero e le proprietà appena descritte:
![[Pasted image 20220603131011.png|600]]
Riscrivendo:
![[Pasted image 20220603131117.png|600]]

#### POLINOMI
### RAMPA UNITARIA
Rampa unitaria: $f(t) = t \cdot 1(t)$
- moltiplicazione per $t \longrightarrow$ proprietà $3$ 
![[Pasted image 20220603131734.png|600]]

### RAMPA PARABOLICA
Rampa parabolica: $f(t) = t^{2} \cdot 1 (t)$
- Posso riscrivere evidenziando la moltiplicazione per $t$
![[Pasted image 20220603131900.png]]
Da cui:
![[Pasted image 20220603132039.png]]

### RAMPA DEL K-ESIMO ORDINE
Vale, per induzione:
$$
t^{k} \cdot 1(t) \longleftrightarrow \frac{k!}{s^{k+1}}
$$
- partendo da $t^{k+1} = t \cdot \underbrace{{t^{k}\cdot 1(t)}}_{g(t)}$


### IMPULSO DI DIRAC
- Area rettangolo unitaria avente base infinitesima (astrazione)
- Matematicamente: $\int_{-\infty}^{\infty} \delta(t) f(t) \,dt = f(0)$     (tutta l'energia concentrata in $0$)
	- Eseguendo la trasformata: $$ \mathcal{L}\{\delta(t)\} = \int_{0}^{\infty} \delta(t) e^{-st} \,dt = e^{-st}|_{t=0} = 1 $$
![[Pasted image 20220603134307.png|200]]

- in maniera sempre astratta [funzioni generalizzate], può essere interpretato come la derivata dei gradini $1(t)$ (incremento infinito)

Abbiamo quindi $3$ modi di vedere l'impulso di Dirac


## TABELLA TRASFORMATE
![[Pasted image 20220603134512.png|500]]

Tutte le funzioni elementari hanno come trasformate delle **funzioni razionali**