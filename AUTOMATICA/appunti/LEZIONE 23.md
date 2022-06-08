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

