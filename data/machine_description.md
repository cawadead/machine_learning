# Machine dataset
Краткое описание
## Ссылка на источник 
https://archive.ics.uci.edu/ml/datasets/Computer+Hardware
## Описание
Создатели: Филипп Эйн-Дор и Якоб Фельдмессер
Связанные публикации:
1. Ein-Dor and Feldmesser (CACM 4/87, стр 308-317)
2. Kibler,D. & Aha,D. (1988).  Instance-Based Prediction of
Real-Valued Attributes. In Proceedings of the CSCSI (Canadian AI) Conference.
## Суть задачи и целевой признак
Вычислить расчетные значения относительной производительности с использованием
метода линейной регрессии.
ERP
## Признаки объектов
vendor name: adviser, amdahl,apollo, basf, bti, burroughs, c.r.d, cambex, cdc,
dec, dg, formation, four-phase, gould, honeywell, hp, ibm, ipl, magnuson,
microdata, nas, ncr, nixdorf, perkin-elmer, prime, siemens, sperry, sratus, wang)
Model Name: many unique symbols
MYCT: machine cycle time in nanoseconds (integer)
MMIN: minimum main memory in kilobytes (integer)
MMAX: maximum main memory in kilobytes (integer)
CACH: cache memory in kilobytes (integer)
CHMIN: minimum channels in units (integer)
CHMAX: maximum channels in units (integer)
PRP: published relative performance (integer)
ERP: estimated relative performance from the original article (integer)