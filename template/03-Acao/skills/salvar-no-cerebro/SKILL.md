---
name: salvar-no-cerebro
description: Guarda uma informação no lugar certo do Segundo Cérebro. Use quando o usuário disser guarde, anote, salve, registre ou lembre disso, ou colar um texto de reunião, e-mail, WhatsApp ou conversa com IA para guardar.
---

# Salvar no cérebro

## Quando usar

O usuário quer guardar algo: uma decisão, um aprendizado, uma conversa, um fato sobre cliente ou um material bruto.

## Antes de começar

Leia `AGENTS.md`, `PADRAO-DE-ARQUIVOS.md` e o `_index.md` da pasta de destino provável.

## Passos

1. Classifique o que foi pedido: decisão, aprendizado, cliente, projeto, diário ou material bruto. Se faltar o conteúdo principal (por exemplo, quem decidiu), pergunte uma vez antes de gravar.
2. Se veio de fonte externa colada (reunião, e-mail, WhatsApp, conversa com IA) ou se a classificação não é clara, grave em `02-Memoria/_inbox/` copiando `_template-item.md`. Nome do arquivo: `AAAA-MM-DD-origem-assunto.md`.
3. Se é claramente uma decisão, aprendizado ou projeto e o usuário pediu para guardar, copie o `_template-*` da pasta certa em `02-Memoria/` e preencha todas as seções.
4. Se a informação é sobre um cliente, identifique a ficha pela regra 8 de "Como escrever" do `AGENTS.md` e preencha o campo `cliente` com o nome do arquivo da ficha. Preencha o que souber. O que faltar fica como `[A PREENCHER]` com a pergunta. Escreva um `resumo` real de até 200 caracteres e converta datas relativas em AAAA-MM-DD.
5. Adicione a linha do arquivo novo no `_index.md` da pasta.
6. Responda em até duas linhas: o que foi salvo, em qual arquivo, e uma pergunta só se faltar algo importante.

## Saída esperada

Um arquivo novo com frontmatter completo, índice atualizado e confirmação curta ao usuário.

## Regras

Nível 1. Não invente fatos. Não grave senha, dado bancário ou documento pessoal. Se o conteúdo for sensível, pergunte antes e use `_restrito/` apenas com o nome do assunto.
