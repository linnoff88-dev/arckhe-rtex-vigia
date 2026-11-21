# rtex-vigia

[![rtex-vigia](guia/assets/banner-es.jpg)](https://inematds.github.io/rtex-vigia/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

rtex-vigia, o rtexv, es un formato de video corto y vertical para contar una noticia o un descubrimiento en unos 2 minutos. Está pensado para quienes crean contenido y quieren explicar algo importante sin perder la atención de la gente por el camino. Aquí encontrarás las reglas, un modelo de guion y ejemplos ya publicados. El formato no produce el video por sí solo: copias una solicitud para tu IA, recibes el guion y luego lo grabas y editas. Para grabar, puedes usar el celular o un avatar, la versión digital de una persona hablando.

## 📖 Guía de uso

Guía completa: **https://inematds.github.io/rtex-vigia/guia/es/**

## Empieza pidiéndoselo a tu IA

Pega esta solicitud en Claude, ChatGPT o en otra IA que pueda leer páginas de internet:

```text
Quiero un guion para un reel en formato rtex-vigia.

Reglas del formato:
- Unos 2 minutos a mi ritmo de habla, en 7 a 10 bloques cortos.
- Secuencia: gancho con el dato más contundente, hablándole a "tú"; una prueba al principio; la historia, con cómo empezó y qué estaba trabado; el giro, explicado con una comparación sencilla; el límite del tema, si lo hay; y el cierre, con una reflexión, una invitación a mi sitio o perfil y una pregunta de verdad.
- Visual: titular corto, subtítulos de 2 o 3 palabras por vez, imágenes realistas y números grandes. Nunca generes con IA el rostro de otra persona real para las imágenes.

Si puedes abrirlos, mira estos ejemplos. Si no puedes, avísame y sigue solo las reglas de arriba:
https://github.com/inematds/rtex-vigia/blob/main/exemplos/cirurgia-raio-x/roteiro.md
https://github.com/inematds/rtex-vigia/blob/main/exemplos/so-tres-ferramentas/roteiro.md
https://github.com/inematds/rtex-vigia/blob/main/exemplos/ia-sem-internet/roteiro.md

Antes de escribir, pregúntame y espera mis respuestas:
1. ¿Cuál es el tema?
2. ¿Qué datos ya investigué y de dónde salieron?
3. ¿A quién va dirigido el video?
4. ¿A qué sitio o perfil quiero llevar a la gente?
5. ¿Hablaré a un ritmo normal o acelerado?
6. ¿Tengo un texto mío o la transcripción de un audio para que copies mi forma de hablar?

Después, escribe el guion con tus propias palabras y con mi voz, en texto corrido, bloque por bloque, e indica el tiempo estimado de lectura.
En cada bloque, enumera las pantallas: el titular, el número destacado, si lo hay, y una imagen que pueda usar legalmente, indicando dónde buscarla.
Comprueba los números y las fechas en fuentes confiables y muéstrame los enlaces. Si no puedes investigar en internet, avísame y no inventes fuentes ni enlaces. Si algún dato que investigué no está en internet, consérvalo y márcalo como "investigación propia" para que yo lo confirme. Si alguna fuente contradice algo, avísame antes de cambiarlo.
No publiques nada ni modifiques ningún archivo sin mi autorización.
```

## El formato en tres partes

| Parte | Qué define |
|---|---|
| **Técnica** | Video vertical 1080 x 1920, unos 2 minutos, habla rápida y algo que cambia en pantalla cada 2 o 3 segundos |
| **Visual** | Apertura con titular y una persona en media pantalla; después, imagen a pantalla completa con un rostro en la esquina, subtítulos cortos y números grandes |
| **Guion** | Gancho, prueba temprana, historia, giro, sentido de la realidad y cierre con una pregunta |

Detalles y medidas: [formato/FORMATO.md](formato/FORMATO.md) (en portugués).

## Ejemplos publicados

| Video | Guion |
|---|---|
| [Cirujano con visión de rayos X](https://www.youtube.com/shorts/kqNiaEvGtTQ) | [guion](exemplos/cirurgia-raio-x/roteiro.md) |
| [Solo 3 herramientas de IA](https://www.youtube.com/shorts/r5FoW7NjTqE) | [guion](exemplos/so-tres-ferramentas/roteiro.md) |
| [IA incluso sin internet](https://www.youtube.com/shorts/KHcn1nvT_g0) | [guion](exemplos/ia-sem-internet/roteiro.md) |

---

## El proceso, de principio a fin

🧠 = sesión con una persona y una IA · ⚙️ = script · 🤖 = IA trabajando sola

| # | Paso | Comando o acción | Quién |
|---|---|---|---|
| 1 | Elegir el dato y el público | Definir el problema o deseo de quien verá el video | 🧠 |
| 2 | Crear el guion | `bin/rtexv novo roteiros/meu-tema.json` | ⚙️ |
| 3 | Escribir los bloques | Completar el archivo siguiendo `formato/FORMATO.md` | 🧠 |
| 4 | Comprobar los datos | Verificar cada número y fecha en una fuente confiable | 🧠 |
| 5 | Comprobar el formato | `bin/rtexv checar roteiros/meu-tema.json` | ⚙️ |
| 6 | Grabar | Cámara o avatar. En INEMA, [explicavideos](https://github.com/inematds/explicavideos) se encarga del avatar | 🧠 |
| 7 | Montar | En INEMA, explicavideos con el perfil viral, en 9:16 | 🤖 |
| 8 | Publicar | En INEMA, la cola de [yt-pub-x3](https://github.com/inematds/yt-pub-x3) | ⚙️ |

## Instalación técnica

Necesitas Python 3.9 o una versión posterior, sin otras dependencias.

```bash
git clone https://github.com/inematds/rtex-vigia.git
cd rtex-vigia
bin/rtexv novo roteiros/meu-tema.json
bin/rtexv checar roteiros/meu-tema.json
bin/rtexv checar roteiros/meu-tema.json --destino meusite.com
```

`checar` termina con `0` cuando aprueba, `1` cuando no aprueba y `2` cuando no puede leer el archivo. Comprueba que haya de 7 a 10 bloques, de 1.800 a 2.700 caracteres de voz, una duración estimada, un gancho al principio, un giro a mitad del guion y un sitio mencionado en el cierre.

| Ruta | Contenido |
|---|---|
| `formato/FORMATO.md` | Reglas completas y medidas |
| `formato/regras.json` | Límites que usa `rtexv` |
| `modelo/roteiro.json` | Modelo para copiar, con versión en texto en `roteiro.md` |
| `exemplos/` | Guiones de videos publicados, en JSON y en texto |
| `bin/rtexv` | Validador de guiones |
| `tests/` | Pruebas |
| `guia/` | Guía en portugués, inglés y español |

Pruebas: `python3 -m unittest discover -s tests`

## Licencia

[MIT](LICENSE)