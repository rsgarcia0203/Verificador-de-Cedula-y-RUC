# Verificador-de-Cedula-y-RUC
La cédula de identidad ecuatoriana tienen un algoritmo especial muy sencillo que es conveniente dominar para su implementación efectiva en proyectos informáticos. Su verificación es muy útil para garantizar la calidad de los datos de una manera sencilla. Por ejemplo, cuando se digitan números de cédula de identidad muchas veces se comenten errores de tipeo, los cuales se los podría detectar inmediatamente automatizando su verificación.

Un ejemplo donde conviene realizar esta validación es en las facturas electrónicas, donde antes de remitir la factura al SRI se puede comprobar que esté correcta la cédula o RUC del receptor de la factura.


## ESTRUCTURA DEL NÚMERO DE CÉDULA DE IDENTIDAD
El estado ecuatoriano, mediante el Registro Civil, asigna el número de cédula de identidad para identificar de manera única a los ciudadanos; el mismo que consiste en 10 dígitos con la siguiente estructura:

- Los dos primeros números corresponden al número de la provincia donde fue generada o expedida la cédula de identidad con el certificado de nacido.  Sin embargo, hay un caso que excluye a la 24 provincias del país y este es cuando un ciudadano se registra como ecuatoriano pero en el exterior, para los cuales el número es 30.  Los valores posibles a la fecha son:
```python
01	Azuay
02	Bolivar
03	Canar
04	Carchi
05	Cotopaxi
06	Chimborazo
07	El_Oro
08	Esmeraldas
09	Guayas
10	Imbabura
11	Loja
12	Los_Rios
13	Manabi
14	Morona_Santiago
15	Napo
16	Pastaza
17	Pichincha
18	Tungurahua
19	Zamora_Chinchipe
20	Galapagos
21	Sucumbios
22	Orellana
23	Santo_Domingo_de_los_Tsachilas
24	Santa_Elena
30	Numero_reservado_para_ecuatorianos_registrados_en_el_exterior.
```
- Del tercer al noveno dígito es un número secuencial que el Registro Civil obtiene de manera automática al momento de la generación de una nueva cédula de identidad.
- El décimo y último dígito es el dígito verificador, el cual se lo obtiene mediante un cálculo especial utilizando el módulo 10.

Nota: Según testimonios de varios funcionarios del Registro Civil, el tercer dígito no es utilizado para la validación de la cédula o como otro dígito verificador, esto se indica debido a que en internet existen muchas páginas que mencionan que el tercer dígito debe ser menor o igual a 5, pero si se ha encontrado cédulas que el tercer dígito sea un 6, por lo tanto, el **único** mecanismo de validación formalmente aceptado es el dígito verificador


## ALGORITMO DE VERIFICACIÓN
El décimo dígito es el resultado de un cálculo realizado con los anteriores nueve, de la siguiente manera:

- Se agrupan los nueve primeros dígitos en dos conjuntos: los que están en posiciones impares y los que están en pares. Por ejemplo, para la cédula de identidad 1713175071, las posiciones impares serían 1, 1, 1, 5 y 7, mientras que las posiciones pares serían 7, 3, 7 y 0.
- A las posiciones impares se multiplican por dos (2). Si el resultado de esta multiplicación es mayor a nueve, se le resta nueve. Por ejemplo, si los números en posiciones impares son 1, 1, 1, 5 y 7, la multiplicación por dos de cada número sería 2, 2, 2, 10 y 14. Ya que algunos resultados son mayores a nueve, se procede a restar nueve a esos valores, quedando así: 2, 2, 2, 1 y 5.
- Se suman los dígitos en posiciones pares, más los resultados de las operaciones en las posiciones impares. Por ejemplo, si los dígitos pares son 7, 3, 7 y 0, la suma de dígitos en posiciones pares sería 17. Por otro lado, si el resultado de las operaciones en las posiciones impares es 2, 2, 2, 1 y 5, su suma sería 12. El total de la suma sería 17 + 12 = 29
- Se obtiene el módulo 10 de la suma total anterior, es decir, se toma el dígito más a la derecha del resultado de la suma. Por ejemplo, si suma 29, el módulo 10 sería 9.
- Si el resultado anterior es cero entonces el dígito verificador es cero, caso contrario al número 10 se le resta el resultado obtenido en el anterior paso. Por ejemplo, si el resultado del paso anterior es 9, la resta sería 10 – 9 = 1, siendo 1 el dígito verificador calculado.
Como se puede verificar, el resultado en el ejemplo del quinto paso (1) es igual al último dígito de la cédula de identidad de ejemplo que consta en el primer paso (1713175071).
