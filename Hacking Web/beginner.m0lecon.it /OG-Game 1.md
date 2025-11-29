<img width="791" height="229" alt="imagen" src="https://github.com/user-attachments/assets/6d8d1186-5a60-4fe2-9164-ae5330ed4d00" />

En este reto nos proporcionan una web donde necesitamos un score superior a 1000 ountos en el clásico juego Snake

<img width="593" height="524" alt="imagen" src="https://github.com/user-attachments/assets/d693b627-3bcd-4cb3-9a53-b5abfb926308" />

Cada "manzana" nos da un total de 10 puntos, por lo que, salvo que nos resulte muy entretenido, vamos a tener que saltarnos el juego.

<img width="362" height="535" alt="imagen" src="https://github.com/user-attachments/assets/e41a3d4c-46c2-4854-82ad-10f6706288bb" />

Para realizar este bypass tenemos varias formas.

Podemos capturar el tráfico y mandarlo cambiado

<img width="969" height="766" alt="imagen" src="https://github.com/user-attachments/assets/0a78a1c8-8e80-4ca2-9461-1fcdd4492ffc" />

Y simplemente con esto, obtendremos la flag

<img width="439" height="544" alt="imagen" src="https://github.com/user-attachments/assets/9cb84eaa-5b23-40d1-8fd5-a13b6b7ea82f" />

Esta sería la manera más fácil. Curiosamente, este menú de submit, solo aparece al chocar con tu propio cuerpo, si perdemos por salir de los limites de la pantalla, no podremos submitear ninguna puntuación, al no saber esto, mi solución final fué ligeramente más rebuscada (y luego descubri como mandar puntuaciones)

Mi solución personal consiste en buscar dentro del código javascript de la web. dentro de este podemos encontrar el método 
"submitHighScore()" que se conecta con la página "/api/submit-score", dando como parámetros una puntuación (score) y un nombre de usuario

<img width="474" height="509" alt="imagen" src="https://github.com/user-attachments/assets/106da392-e232-4ef2-8f23-a1f86f09301f" />

Podemos verificar la existencia de esta página desde el navegador
https://snake1.challs.m0lecon.it/game
Obviamente, no vamos a obtener ningun resultado visible ya que solo responde a metodos POST, pero de esta forma podemos verificar la existencia de esta url

Ahora que sabemos los datos que necesitamos y a donde los tenemos que mandar, podemos crear un pequeño código que envie un score mayor a 1000 a esta url y capturar la salida

<img width="644" height="209" alt="imagen" src="https://github.com/user-attachments/assets/71072775-5bca-4c8f-ab47-1ba89b99c3dc" />

Y obtendremos nuestra flag

<img width="644" height="209" alt="imagen" src="https://github.com/user-attachments/assets/95131d77-9b6e-4bb9-b9b7-2f3867bfb877" />


<details>
  <summary>Mostrar la flag</summary>
ptm{sn4k3_1s_th3_g04t!}
</details>

**Autor:** [Fernando Lorenzo](https://github.com/Fernandolv123)
