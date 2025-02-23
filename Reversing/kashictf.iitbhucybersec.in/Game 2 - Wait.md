# Game 2 - Wait

[Enlace del reto](https://kashictf.iitbhucybersec.in/challenges#Game%202%20-%20Wait-21)

![imagen](https://github.com/user-attachments/assets/d325c176-e869-46e6-b2b1-b64dca495d68)

En este reto, tenemos un ejecutable de un juego. Si intentamos abrir este juego, tendremos una cuenta gigantesca para obtener la flag.

![imagen](https://github.com/user-attachments/assets/20837c7c-7e9a-40b1-b275-65cb955bc4f8)

Por supuesto, no podemos esperar tanto tiempo (incluso si llegase a funcionar) pues los retos no estarán activos tanto tiempo.
Utilizando [Godot RE Tools](https://github.com/GDRETools/gdsdecomp/tree/master) Podemos decompilar el juego para ver el código

![imagen](https://github.com/user-attachments/assets/e1a19927-79ea-438b-97d6-b369642777a9)

En el archivo main.gd, podemos encontrar la variable time_left, seteada a un gran valor. Podemos eliminar este código y volver a compilar el juego

![imagen](https://github.com/user-attachments/assets/bba9c053-d41d-4244-8610-f878fec6a1f1)

Ahora, si volvemos a compilar el juego y ejecutamos el ejecutable (me he descargado godot exclusivamente para este paso)

![imagen](https://github.com/user-attachments/assets/8e7fc80f-1cc4-4f96-9ec2-e6ff84d85743)

<details>
  <summary>Mostrar la flag</summary>
KashiCTF{Ch4kr4_Vyuh}
</details>

**Autor:** [Fernando Lorenzo](https://github.com/Fernandolv123)
