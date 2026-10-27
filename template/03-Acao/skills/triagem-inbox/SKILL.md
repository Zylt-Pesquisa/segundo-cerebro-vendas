---
name: triagem-inbox
description: Organiza a caixa de entrada do Segundo Cérebro. Use quando o usuário pedir para organizar, triar, limpar ou processar o que está esperando na caixa de entrada.
---

# Triagem da caixa de entrada

## Quando usar

Há itens em `02-Memoria/_inbox/` com `processado: nao` e o usuário quer organizá-los.

## Antes de começar

Leia `02-Memoria/_inbox/_index.md` e abra cada item com `processado: nao`.

## Passos

1. Para cada item, preencha a seção "O que parece importante" com até 5 linhas e sugira um destino: decisão, aprendizado, cliente, projeto, diário ou descarte.
2. Mostre ao usuário uma lista curta: item, resumo em uma linha, destino sugerido.
3. Espere a confirmação do usuário. Ele pode aprovar tudo, ajustar item a item ou pular.
4. Para cada destino confirmado, crie a nota copiando o `_template-*` certo, preencha, atualize o índice da pasta e ligue a nota ao item em `relacionados`.
5. Marque o item como `processado: sim` e `status: arquivado`. Não apague.
6. Termine dizendo quantos itens foram organizados e quantos ficaram.

## Saída esperada

Notas criadas nos destinos confirmados, itens da caixa marcados como processados e um resumo de duas linhas.

## Regras

Nível 1. Nada vira nota curada sem confirmação. Descarte significa arquivar, nunca apagar.
