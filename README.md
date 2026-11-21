# rtex-vigia

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![rtex-vigia](guia/assets/banner.jpg)](https://inematds.github.io/rtex-vigia/guia/)

**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

## O que Ã©

O rtex-vigia, ou rtexv, Ã© um formato de vÃ­deo curto e vertical para contar uma notÃ­cia ou descoberta em cerca de 2 minutos. Ele serve para quem cria conteÃºdo e quer explicar algo importante sem perder a pessoa no meio. Aqui vocÃª encontra as regras, um modelo de roteiro e exemplos jÃ¡ publicados. Ele nÃ£o produz o vÃ­deo sozinho: vocÃª copia um pedido para a sua IA, recebe o roteiro e depois grava e edita. Para gravar, use o celular ou um avatar, a versÃ£o digital de uma pessoa falando.

## ðŸ“– Guia de uso

Guia completo: **https://inematds.github.io/rtex-vigia/guia/**

## Comece pedindo Ã  sua IA

Cole este pedido no Claude, no ChatGPT ou em outra IA que consiga ler pÃ¡ginas da internet:

```text
Quero um roteiro de reel no formato rtex-vigia.

Regras do formato:
- Cerca de 2 minutos no meu ritmo de fala, em 7 a 10 blocos curtos.
- SequÃªncia: gancho com o fato mais forte, falando com "vocÃª"; uma prova logo no inÃ­cio; a histÃ³ria, com como comeÃ§ou e o que estava travado; a virada, explicada com uma comparaÃ§Ã£o simples; o limite do assunto, quando houver; e o fecho, com uma moral, o convite para o meu site ou perfil e uma pergunta de verdade.
- Visual: manchete curta, legenda de 2 ou 3 palavras por vez, imagens realistas e nÃºmeros grandes. Nas imagens, nunca gere com IA o rosto de outra pessoa real.

Se conseguir abrir, veja estes exemplos. Se nÃ£o conseguir, me avise e siga sÃ³ as regras acima:
https://github.com/inematds/rtex-vigia/blob/main/exemplos/cirurgia-raio-x/roteiro.md
https://github.com/inematds/rtex-vigia/blob/main/exemplos/so-tres-ferramentas/roteiro.md
https://github.com/inematds/rtex-vigia/blob/main/exemplos/ia-sem-internet/roteiro.md

Antes de escrever, me pergunte e espere as respostas:
1. Qual Ã© o assunto?
2. Quais fatos eu jÃ¡ apurei e de onde vieram?
3. Para quem Ã© o vÃ­deo?
4. Para qual site ou perfil quero levar as pessoas?
5. Vou falar em ritmo normal ou acelerado?
6. Tenho um texto meu ou a transcriÃ§Ã£o de um Ã¡udio para vocÃª copiar meu jeito de falar?

Depois escreva o roteiro com palavras prÃ³prias e na minha voz, em texto corrido, bloco por bloco, e diga o tempo estimado de leitura.
Em cada bloco, liste as telas: a manchete, o nÃºmero em destaque, se houver, e uma imagem que eu possa usar legalmente, dizendo onde buscar.
Confira nÃºmeros e datas em fontes confiÃ¡veis e me mostre os links. Se nÃ£o conseguir pesquisar na internet, avise e nÃ£o invente fontes nem links. O que eu apurei e nÃ£o estiver na internet, mantenha e marque como "apuraÃ§Ã£o prÃ³pria" para eu confirmar. Se algo for contrariado por uma fonte, me avise antes de mudar.
NÃ£o publique nada e nÃ£o altere nenhum arquivo sem o meu sim.
```

## O formato em trÃªs partes

| Parte | O que define |
|---|---|
| **TÃ©cnico** | VÃ­deo vertical 1080 x 1920, cerca de 2 minutos, fala rÃ¡pida e algo mudando na tela a cada 2 ou 3 segundos |
| **Visual** | Abertura com manchete e pessoa em meia tela, depois imagem cheia com rosto no canto, legenda curta e nÃºmeros grandes |
| **Roteiro** | Gancho, prova cedo, histÃ³ria, virada, pÃ© no chÃ£o e fecho com pergunta |

Detalhes e medidas: [formato/FORMATO.md](formato/FORMATO.md).

## Exemplos publicados

| VÃ­deo | Roteiro |
|---|---|
| [CirurgiÃ£o com visÃ£o de raio-x](https://www.youtube.com/shorts/kqNiaEvGtTQ) | [roteiro](exemplos/cirurgia-raio-x/roteiro.md) |
| [SÃ³ 3 ferramentas de IA](https://www.youtube.com/shorts/r5FoW7NjTqE) | [roteiro](exemplos/so-tres-ferramentas/roteiro.md) |
| [IA mesmo sem internet](https://www.youtube.com/shorts/KHcn1nvT_g0) | [roteiro](exemplos/ia-sem-internet/roteiro.md) |

---

## O processo, do inÃ­cio ao fim

ðŸ§  = sessÃ£o com pessoa e IA Â· âš™ï¸ = script Â· ðŸ¤– = IA executando sozinha

| # | Passo | Comando ou aÃ§Ã£o | Quem |
|---|---|---|---|
| 1 | Escolher o fato e o pÃºblico | Definir a dor ou o desejo de quem vai assistir | ðŸ§  |
| 2 | Criar o roteiro | `bin/rtexv novo roteiros/meu-tema.json` | âš™ï¸ |
| 3 | Escrever os blocos | Preencher o arquivo seguindo `formato/FORMATO.md` | ðŸ§  |
| 4 | Conferir os fatos | Checar cada nÃºmero e data em fonte confiÃ¡vel | ðŸ§  |
| 5 | Conferir o formato | `bin/rtexv checar roteiros/meu-tema.json` | âš™ï¸ |
| 6 | Gravar | CÃ¢mera ou avatar. Na INEMA, o [explicavideos](https://github.com/inematds/explicavideos) cuida do avatar | ðŸ§  |
| 7 | Montar | Na INEMA, o explicavideos no perfil viral, em 9:16 | ðŸ¤– |
| 8 | Publicar | Na INEMA, a fila do [yt-pub-x3](https://github.com/inematds/yt-pub-x3) | âš™ï¸ |

## InstalaÃ§Ã£o tÃ©cnica

Precisa de Python 3.9 ou mais novo, sem outras dependÃªncias.

```bash
git clone https://github.com/inematds/rtex-vigia.git
cd rtex-vigia
bin/rtexv novo roteiros/meu-tema.json
bin/rtexv checar roteiros/meu-tema.json
bin/rtexv checar roteiros/meu-tema.json --destino meusite.com
```

`checar` sai com `0` quando aprova, `1` quando reprova e `2` quando nÃ£o consegue ler o arquivo. Ele confere de 7 a 10 blocos, 1.800 a 2.700 caracteres de fala, duraÃ§Ã£o estimada, gancho no inÃ­cio, virada no meio e site citado no fecho.

| Caminho | ConteÃºdo |
|---|---|
| `formato/FORMATO.md` | Regras completas e medidas |
| `formato/regras.json` | Limites usados pelo `rtexv` |
| `modelo/roteiro.json` | Modelo para copiar, com versÃ£o em texto em `roteiro.md` |
| `exemplos/` | Roteiros de vÃ­deos publicados, em JSON e em texto |
| `bin/rtexv` | Conferidor de roteiros |
| `tests/` | Testes |
| `guia/` | Guia em portuguÃªs, inglÃªs e espanhol |

Testes: `python3 -m unittest discover -s tests`

## LicenÃ§a

[MIT](LICENSE)

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>