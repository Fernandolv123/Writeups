# Memories Bring Back You

[Enlace del reto](https://kashictf.iitbhucybersec.in/challenges#Memories%20Bring%20Back%20You-13)

![imagen](https://github.com/user-attachments/assets/5e348558-38d9-41c8-a611-be06be8f91a9)

Para este reto, tenemos que descargar un archivo de 1GB. Como era de esperar en un archivo tan extenso, el análisis con binwalk detecta una gran cantidad de archivos ocultos. Entre ellos, encontre algunas bases de datos

![imagen](https://github.com/user-attachments/assets/ab1324a3-bde0-4f4c-bdce-2270974c5cc9)

Decidí exportar estas bases de datos para ver su contenido

![imagen](https://github.com/user-attachments/assets/9435fb8c-5f34-42f9-b7eb-2817b9bd2d2e)

Desgraciadamente, este proceso no exporta ningún archivo y, en general, los archivos exportados desde binwalk no resultan de utilidad. Debido a esto, me decidí a probar suerte con strings para buscar información dentro del archivo con palabras clave como flags o ctf

![imagen](https://github.com/user-attachments/assets/7c5d0792-8a8d-4e79-8063-0aa27d233aff)

<details>
  <summary>Mostrar la flag</summary>
KashiCTF{DF1R_g03555_Brrrr}
</details>

**Autor:** [Fernando Lorenzo](https://github.com/Fernandolv123)
