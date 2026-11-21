# rtex-vigia

[![rtex-vigia](guia/assets/banner-en.jpg)](https://inematds.github.io/rtex-vigia/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

rtex-vigia, or rtexv, is a short vertical video format for telling a news story or sharing a discovery in about 2 minutes. It’s for content creators who want to explain something important without losing people along the way. Here you’ll find the rules, a script template, and examples that have already been published. It doesn’t make the video for you: you copy a prompt into your AI, get the script, then record and edit it. To record, use your phone or an avatar, a digital version of someone speaking.

## 📖 User guide

Full guide: **https://inematds.github.io/rtex-vigia/guia/en/**

## Start by asking your AI

Paste this prompt into Claude, ChatGPT, or another AI that can read web pages:

```text
I want a reel script in the rtex-vigia format.

Format rules:
- About 2 minutes at my speaking pace, in 7 to 10 short blocks.
- Sequence: hook with the strongest fact, speaking directly to "you"; proof right near the beginning; the story, including how it started and what was stuck; the turning point, explained with a simple comparison; the limits of the story, if any; and the close, with a takeaway, an invitation to visit my website or profile, and a genuine question.
- Visuals: a short headline, captions with 2 or 3 words at a time, realistic images, and large numbers. Never use AI to generate images of another real person’s face.

If you can open them, take a look at these examples. If you can’t, let me know and follow only the rules above:
https://github.com/inematds/rtex-vigia/blob/main/exemplos/cirurgia-raio-x/roteiro.md
https://github.com/inematds/rtex-vigia/blob/main/exemplos/so-tres-ferramentas/roteiro.md
https://github.com/inematds/rtex-vigia/blob/main/exemplos/ia-sem-internet/roteiro.md

Before writing, ask me these questions and wait for my answers:
1. What’s the topic?
2. What facts have I already researched, and where did they come from?
3. Who is the video for?
4. Which website or profile do I want to direct people to?
5. Will I speak at a normal or fast pace?
6. Do I have a text of my own or an audio transcript you can use to match the way I speak?

Then write the script in your own words and in my voice, as continuous text, block by block, and give me the estimated reading time.
For each block, list the screens: the headline, the featured number, if any, and an image I can legally use, including where to find it.
Check numbers and dates against reliable sources and show me the links. If you can’t search the internet, let me know and don’t make up sources or links. If something I researched isn’t online, keep it and mark it as "my own research" for me to confirm. If a source contradicts something, let me know before changing it.
Don’t publish anything or change any files without my go-ahead.
```

## The three parts of the format

| Part | What it defines |
|---|---|
| **Technical** | Vertical 1080 x 1920 video, about 2 minutes, fast-paced speech, and something changing on screen every 2 or 3 seconds |
| **Visual** | Opens with a headline and a person in half the frame, then full-screen images with a face in the corner, short captions, and large numbers |
| **Script** | Hook, early proof, story, turning point, a grounded perspective, and a closing question |

Details and measurements: [format/FORMATO.md](formato/FORMATO.md) (in Portuguese).

## Published examples

| Video | Script |
|---|---|
| [Surgeon with X-ray vision](https://www.youtube.com/shorts/kqNiaEvGtTQ) | [script](exemplos/cirurgia-raio-x/roteiro.md) |
| [Just 3 AI tools](https://www.youtube.com/shorts/r5FoW7NjTqE) | [script](exemplos/so-tres-ferramentas/roteiro.md) |
| [AI without internet](https://www.youtube.com/shorts/KHcn1nvT_g0) | [script](exemplos/ia-sem-internet/roteiro.md) |

---

## The process, from start to finish

🧠 = session with a person and AI · ⚙️ = script · 🤖 = AI working on its own

| # | Step | Command or action | Who |
|---|---|---|---|
| 1 | Choose the fact and audience | Define the pain point or desire of the people watching | 🧠 |
| 2 | Create the script | `bin/rtexv novo roteiros/meu-tema.json` | ⚙️ |
| 3 | Write the blocks | Fill in the file following `formato/FORMATO.md` | 🧠 |
| 4 | Verify the facts | Check each number and date against a reliable source | 🧠 |
| 5 | Check the format | `bin/rtexv checar roteiros/meu-tema.json` | ⚙️ |
| 6 | Record | Camera or avatar. At INEMA, [explicavideos](https://github.com/inematds/explicavideos) handles the avatar | 🧠 |
| 7 | Assemble | At INEMA, explicavideos in viral profile, in 9:16 | 🤖 |
| 8 | Publish | At INEMA, the [yt-pub-x3](https://github.com/inematds/yt-pub-x3) queue | ⚙️ |

## Technical installation

Requires Python 3.9 or newer, with no other dependencies.

```bash
git clone https://github.com/inematds/rtex-vigia.git
cd rtex-vigia
bin/rtexv novo roteiros/meu-tema.json
bin/rtexv checar roteiros/meu-tema.json
bin/rtexv checar roteiros/meu-tema.json --destino meusite.com
```

`checar` exits with `0` when approved, `1` when rejected, and `2` when it can’t read the file. It checks for 7 to 10 blocks, 1,800 to 2,700 spoken characters, estimated duration, a hook at the beginning, a turning point in the middle, and a website mentioned in the close.

| Path | Contents |
|---|---|
| `formato/FORMATO.md` | Complete rules and measurements |
| `formato/regras.json` | Limits used by `rtexv` |
| `modelo/roteiro.json` | Template to copy, with a text version in `roteiro.md` |
| `exemplos/` | Scripts for published videos, in JSON and text |
| `bin/rtexv` | Script checker |
| `tests/` | Tests |
| `guia/` | Guide in Portuguese, English, and Spanish |

Tests: `python3 -m unittest discover -s tests`

## License

[MIT](LICENSE)