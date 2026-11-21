# Formato rtex-vigia (rtexv)

Reel vertical de cerca de 2 minutos que conta uma notícia ou descoberta como história. Os números abaixo foram medidos em 16 reels produzidos neste formato, em novembro de 2026.

## Técnico

| Item | Regra | Medido nos 16 reels |
|---|---|---|
| Tela | Vertical 9:16, 1080 x 1920 | 1080 x 1920 em todos |
| Quadros por segundo | 25 | 25 em todos |
| Duração | Cerca de 2 minutos, no máximo 170 s | 105 a 138 s, mediana 121 s |
| Fala | 1.800 a 2.700 caracteres | 1.990 a 2.526 caracteres |
| Velocidade | Fala rápida e clara | Mediana de 205 palavras por minuto |
| Blocos | 7 a 10 | 8 a 10 |
| Ritmo da tela | Algo muda a cada 2 a 3 s | Mediana de 2,7 s |

## Visual

- **Abertura:** manchete em cima e a pessoa em meia tela embaixo.
- **Depois da abertura:** a imagem ocupa a tela e o rosto vai para um canto.
- **Manchete:** curta, em letras grandes, branco com destaque âmbar.
- **Legenda:** 2 ou 3 palavras por vez, com uma palavra destacada.
- **Imagens:** cenas, lugares e objetos realistas. Nunca gerar com IA o rosto de outra pessoa real.
- **Números:** aparecem grandes, sozinhos na tela.
- **Selo:** marca e tema no topo, do início ao fim.
- **Fecho:** o site na tela e uma pergunta para quem assistiu.

## Roteiro

1. **Gancho:** o fato mais forte na primeira frase, falando com "você".
2. **Prova cedo:** um número ou uma autoridade nos primeiros segundos.
3. **História em ordem:** origem, problema e crescimento.
4. **Virada:** o detalhe contraintuitivo que explica por que isso importa, com uma comparação simples.
5. **Pé no chão:** o limite do assunto ou o que ainda não foi provado, quando houver.
6. **Moral e fecho:** uma frase de efeito, o convite ao site e uma pergunta de verdade.

Os blocos podem ter nomes próprios em cada vídeo, como "O ciclo" ou "A regra". O que se mantém é esta sequência.

## Regras de conteúdo

- Todo número e toda data são conferidos antes de entrar no roteiro. O que não se confirma sai.
- O texto usa palavras próprias, na voz de quem apresenta.
- Promessa só com o que é verdade.

## Arquivo do roteiro

`roteiro.json` tem `titulo` e `blocos`. Cada bloco tem `capitulo`, `titulo` e `fala`. O primeiro capítulo é `Gancho`, um dos capítulos do meio contém `Virada` e o último cita o site de destino. Veja `modelo/roteiro.json` e a pasta `exemplos/`.
