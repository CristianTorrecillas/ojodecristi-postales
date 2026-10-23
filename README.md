# Postales ojodecristi

Herramienta para armar los carruseles de Instagram (postales, grillas y receta Fujifilm).

Página: https://cristiantorrecillas.github.io/ojodecristi-postales/

- `src/postales.template.html` es el código fuente.
- `python3 src/build.py` embebe fuentes, texturas y fotos de ejemplo y genera `index.html`.
- `sw.js` + `manifest.webmanifest`: se puede instalar en el celu ("Agregar a pantalla de inicio") y abre sin señal.

## Cómo está armado el espacio de trabajo

- **Columna de fotos**: número inicial, lugar, títulos de grilla y la lista corta (miniatura, N.°, título, lugar, colores). Se ordena arrastrando el ⠿ o con las flechas.
- **Vista grande** en el centro y la tira del carrusel abajo. Lista, vista grande y tira siguen a la misma foto.
- **Panel de la derecha** con dos pestañas: «Esta foto» (título, lugar, fecha, N.°, colores, encuadre y lo que tiene distinto de las demás, con «Volver a como todas») y «Todas las fotos» (el diseño general).
- En el celu, tocar una foto abre su editor con la postal fija arriba; «‹ Fotos» o el botón atrás vuelven a la lista.
- **Deshacer / rehacer** (Ctrl+Z, Ctrl+Shift+Z o Ctrl+Y) para todo: textos, orden, fotos quitadas, encuadres y diseño. Dentro de un campo de texto, Ctrl+Z deshace lo que se escribe.
- **Guardados**: carruseles con nombre (fotos, textos y diseño). El que está abierto se guarda solo. Van en IndexedDB `postales-ojodecristi-extra` (aparte de la sesión, que sigue en `postales-ojodecristi`).
- **De la web**: trae fotos de `../pagina-web/` por número (título, lugar, año, cámara y colores). Vienen a 1600 px; «Reemplazar imagen» cambia la imagen por la original sin perder los datos.
- **Exportar** abre la revisión: ancho (1080 / 2160), avisos (sin título, sin lugar, colores casi iguales, números repetidos, poca resolución), el texto del posteo con los hashtags guardados, y .zip, una por una, Drive o compartir (celu). Las imágenes se van armando mientras revisás.
- **Vista previa → En tu perfil**: la portada nueva en la grilla de 3 con los posteos anteriores (se guardan al exportar; también se suman capturas).
- **Receta**: «Completar con la foto» lee la simulación y los ajustes que guarda la cámara Fujifilm en sus JPG (MakerNote).
- **⚙**: colores de la herramienta y conexión con Drive.
