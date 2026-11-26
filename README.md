ï»¿# rtex-vigia

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![rtex-vigia](guia/assets/banner.jpg)](https://inematds.github.io/rtex-vigia/guia/)

**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

## O que êÂ©

O rtex-vigia, ou rtexv, êÂ© um formato de vêÂ­deo curto e vertical para contar uma notêÂ­cia ou descoberta em cerca de 2 minutos. Ele serve para quem cria conteêÂºdo e quer explicar algo importante sem perder a pessoa no meio. Aqui vocêÂª encontra as regras, um modelo de roteiro e exemplos jêÂ¡ publicados. Ele nêÂ£o produz o vêÂ­deo sozinho: vocêÂª copia um pedido para a sua IA, recebe o roteiro e depois grava e edita. Para gravar, use o celular ou um avatar, a versêÂ£o digital de uma pessoa falando.

## ê°Å¸ââ Guia de uso

Guia completo: **https://inematds.github.io/rtex-vigia/guia/**

## Comece pedindo êÂ  sua IA

Cole este pedido no Claude, no ChatGPT ou em outra IA que consiga ler pêÂ¡ginas da internet:

```text
Quero um roteiro de reel no formato rtex-vigia.

Regras do formato:
- Cerca de 2 minutos no meu ritmo de fala, em 7 a 10 blocos curtos.
- SequêÂªncia: gancho com o fato mais forte, falando com "vocêÂª"; uma prova logo no inêÂ­cio; a histêÂ³ria, com como comeêÂ§ou e o que estava travado; a virada, explicada com uma comparaêÂ§êÂ£o simples; o limite do assunto, quando houver; e o fecho, com uma moral, o convite para o meu site ou perfil e uma pergunta de verdade.
- Visual: manchete curta, legenda de 2 ou 3 palavras por vez, imagens realistas e nêÂºmeros grandes. Nas imagens, nunca gere com IA o rosto de outra pessoa real.

Se conseguir abrir, veja estes exemplos. Se nêÂ£o conseguir, me avise e siga sêÂ³ as regras acima:
https://github.com/inematds/rtex-vigia/blob/main/exemplos/cirurgia-raio-x/roteiro.md
https://github.com/inematds/rtex-vigia/blob/main/exemplos/so-tres-ferramentas/roteiro.md
https://github.com/inematds/rtex-vigia/blob/main/exemplos/ia-sem-internet/roteiro.md

Antes de escrever, me pergunte e espere as respostas:
1. Qual êÂ© o assunto?
2. Quais fatos eu jêÂ¡ apurei e de onde vieram?
3. Para quem êÂ© o vêÂ­deo?
4. Para qual site ou perfil quero levar as pessoas?
5. Vou falar em ritmo normal ou acelerado?
6. Tenho um texto meu ou a transcriêÂ§êÂ£o de um êÂ¡udio para vocêÂª copiar meu jeito de falar?

Depois escreva o roteiro com palavras prêÂ³prias e na minha voz, em texto corrido, bloco por bloco, e diga o tempo estimado de leitura.
Em cada bloco, liste as telas: a manchete, o nêÂºmero em destaque, se houver, e uma imagem que eu possa usar legalmente, dizendo onde buscar.
Confira nêÂºmeros e datas em fontes confiêÂ¡veis e me mostre os links. Se nêÂ£o conseguir pesquisar na internet, avise e nêÂ£o invente fontes nem links. O que eu apurei e nêÂ£o estiver na internet, mantenha e marque como "apuraêÂ§êÂ£o prêÂ³pria" para eu confirmar. Se algo for contrariado por uma fonte, me avise antes de mudar.
NêÂ£o publique nada e nêÂ£o altere nenhum arquivo sem o meu sim.
```

## O formato em trêÂªs partes

| Parte | O que define |
|---|---|
| **TêÂ©cnico** | VêÂ­deo vertical 1080 x 1920, cerca de 2 minutos, fala rêÂ¡pida e algo mudando na tela a cada 2 ou 3 segundos |
| **Visual** | Abertura com manchete e pessoa em meia tela, depois imagem cheia com rosto no canto, legenda curta e nêÂºmeros grandes |
| **Roteiro** | Gancho, prova cedo, histêÂ³ria, virada, pêÂ© no chêÂ£o e fecho com pergunta |

Detalhes e medidas: [formato/FORMATO.md](formato/FORMATO.md).

## Exemplos publicados

| VêÂ­deo | Roteiro |
|---|---|
| [CirurgiêÂ£o com visêÂ£o de raio-x](https://www.youtube.com/shorts/kqNiaEvGtTQ) | [roteiro](exemplos/cirurgia-raio-x/roteiro.md) |
| [SêÂ³ 3 ferramentas de IA](https://www.youtube.com/shorts/r5FoW7NjTqE) | [roteiro](exemplos/so-tres-ferramentas/roteiro.md) |
| [IA mesmo sem internet](https://www.youtube.com/shorts/KHcn1nvT_g0) | [roteiro](exemplos/ia-sem-internet/roteiro.md) |

---

## O processo, do inêÂ­cio ao fim

ê°Å¸Â§Â  = sessêÂ£o com pessoa e IA êÂ· ê¢Å¡â¢ê¯Â¸Â = script êÂ· ê°Å¸Â¤â = IA executando sozinha

| # | Passo | Comando ou aêÂ§êÂ£o | Quem |
|---|---|---|---|
| 1 | Escolher o fato e o pêÂºblico | Definir a dor ou o desejo de quem vai assistir | ê°Å¸Â§Â  |
| 2 | Criar o roteiro | `bin/rtexv novo roteiros/meu-tema.json` | ê¢Å¡â¢ê¯Â¸Â |
| 3 | Escrever os blocos | Preencher o arquivo seguindo `formato/FORMATO.md` | ê°Å¸Â§Â  |
| 4 | Conferir os fatos | Checar cada nêÂºmero e data em fonte confiêÂ¡vel | ê°Å¸Â§Â  |
| 5 | Conferir o formato | `bin/rtexv checar roteiros/meu-tema.json` | ê¢Å¡â¢ê¯Â¸Â |
| 6 | Gravar | CêÂ¢mera ou avatar. Na INEMA, o [explicavideos](https://github.com/inematds/explicavideos) cuida do avatar | ê°Å¸Â§Â  |
| 7 | Montar | Na INEMA, o explicavideos no perfil viral, em 9:16 | ê°Å¸Â¤â |
| 8 | Publicar | Na INEMA, a fila do [yt-pub-x3](https://github.com/inematds/yt-pub-x3) | ê¢Å¡â¢ê¯Â¸Â |

## InstalaêÂ§êÂ£o têÂ©cnica

Precisa de Python 3.9 ou mais novo, sem outras dependêÂªncias.

```bash
git clone https://github.com/inematds/rtex-vigia.git
cd rtex-vigia
bin/rtexv novo roteiros/meu-tema.json
bin/rtexv checar roteiros/meu-tema.json
bin/rtexv checar roteiros/meu-tema.json --destino meusite.com
```

`checar` sai com `0` quando aprova, `1` quando reprova e `2` quando nêÂ£o consegue ler o arquivo. Ele confere de 7 a 10 blocos, 1.800 a 2.700 caracteres de fala, duraêÂ§êÂ£o estimada, gancho no inêÂ­cio, virada no meio e site citado no fecho.

| Caminho | ConteêÂºdo |
|---|---|
| `formato/FORMATO.md` | Regras completas e medidas |
| `formato/regras.json` | Limites usados pelo `rtexv` |
| `modelo/roteiro.json` | Modelo para copiar, com versêÂ£o em texto em `roteiro.md` |
| `exemplos/` | Roteiros de vêÂ­deos publicados, em JSON e em texto |
| `bin/rtexv` | Conferidor de roteiros |
| `tests/` | Testes |
| `guia/` | Guia em portuguêÂªs, inglêÂªs e espanhol |

Testes: `python3 -m unittest discover -s tests`

## LicenêÂ§a

[MIT](LICENSE)

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>