## SNR: SIGNAL TO NOISE RATIO
Sigla per indicare il *rapporto **segnale-rumore***, ovvero si cerca di valutare le "prestazioni" del segnale sulla base del confronto tra la potenza del segnale che arriva e la potenza del segnale sul ricevitore.
Nel caso di rumore di quantizzazione (ciò che affrontiamo noi), si definisce: 
$$
\boxed{SNR = \frac{S}{P_{e}}} \quad , \quad \text{supponendo: } P_{e}=\frac{\Delta^2}{12}
$$
Dove:
- $S$ è potenza del segnale da quantizzare;
- $P_{e}$ è la potenza dell'errore di quantizzazione.

Sappiamo che $\displaystyle \Delta = \frac{D}{2^{B}}$, dove $D$ è la dinamica sia del segnale che del quantizzatore, supponendo infatti di rientrare in questa ipotesi come già detto precedentemente.
- Sostituendo questa osservazione alla formula dell' $SNR$ precedentemente scritta si ottiene alternativamente:
$$
SNR = \frac{S}{\frac{\Delta^2}{12}} = \frac{S}{\left( \frac{D}{2^{B}} \right)^2 \cdot \frac{1}{12}}
$$
Quindi:
$$
\boxed{\boxed{SNR = \frac{12 \cdot S \cdot 2^{2B}}{D^{2}}}}
$$
- Che è la formula *generale* con la possibilità di "scegliere" la dinamica del segnale e il tipo di segnale a seconda del caso
	- Nella pratica quindi si sostituiscono le informazioni del segnale che conosciamo all'interno della formula

>> Spesso il $SNR$ viene espresso in $d_{B}$ , da cui si ottiene: $$SNR = 10 \log_{10} (SNR) = 10 \log_{10} 2^{2B} + 10 \log_{10} \frac{12 S}{D^{2}}= 2B \cdot \log_{10}2 + 10 \log_{10} \frac{12 S}{D^{2}}$$
>> Da cui finalmente: $$ 6.02B + 10 \log_{10}\frac{12S}{D^{2}} $$
