# Game1 -Untilted Game

[Enlace al reto](https://kashictf.iitbhucybersec.in/challenges#Game%201%20-%20Untitled%20Game-20)

![imagen](https://github.com/user-attachments/assets/3d21ca30-dd2e-4e69-8e6a-d71c0c40a889)

En este reto nos dan un ejecutable que resulta ser un juego.

![imagen](https://github.com/user-attachments/assets/1d2cd074-9a00-4610-9e50-e8e352551d18)

Mi primera impresión fue pensar que estaba hecho en Unity, pero buscando en el archivo, descubrí que el juego estaba hecho en godot engine

![imagen](https://github.com/user-attachments/assets/0f364b75-c239-46e0-a4f6-53dec5e9dde1)

Para descompilar el juego utilicé la herramienta [Godot RE Tools](https://github.com/GDRETools/gdsdecomp/tree/master)

![imagen](https://github.com/user-attachments/assets/6113f864-7280-4ef7-aa06-f72570eaae7b)

Buscando en los archivos del juego, tenemos dos scripts, un script “Global.gd”  sin mucha utilidad que, imagino funciona parecido a un GameManager de Unity, controlando variables globales.
Y un archivo player.gd

![imagen](https://github.com/user-attachments/assets/be3e3b94-aaaa-4683-8de7-3b34b026aa3e)

Podemos ver también que esta flag se muestra en el método “ready()”. Esto significa que otra forma de ver la flag sería ejecutar el juego desde comandos

![imagen](https://github.com/user-attachments/assets/9a539e19-db67-4a8c-900d-72ec8244841e)

<details>
  <summary>Mostrar la flag</summary>
KashiCTF{N07_1N_7H3_G4M3}
</details>

**Autor:** [Fernando Lorenzo](https://github.com/Fernandolv123)
