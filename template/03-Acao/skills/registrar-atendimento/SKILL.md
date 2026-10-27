---
name: registrar-atendimento
description: Registra um contato com cliente na ficha dele e no diário. Use quando o usuário disser que falou, atendeu, ligou, reuniu ou trocou mensagens com um cliente ou lead, e quiser registrar.
---

# Registrar atendimento

## Quando usar

O usuário acabou de falar com um cliente e conta o que aconteceu.

## Antes de começar

Leia `02-Memoria/clientes/_index.md` para achar a ficha do cliente, `01-Contexto/07-processo-comercial.md` para usar os nomes certos das etapas e `02-Memoria/decisoes/_index.md` para saber se alguma decisão vigente se aplica ao que o cliente pediu.

## Passos

1. Procure a ficha do cliente em `02-Memoria/clientes/`. Se não existir, crie copiando `_template-cliente.md` com o nome do cliente em minúsculas e hífen, e adicione ao índice.
2. Acrescente no topo da seção Histórico uma entrada com data, canal, o que foi dito, objeções e o que ficou combinado.
3. Atualize no frontmatter `etapa_funil`, `proximo_contato` e `atualizado_em`. Reescreva o `resumo` se a situação mudou.
4. Se apareceu uma objeção nova ou uma lição concreta, proponha criar uma nota em `aprendizados/` já com "O que aprendemos" e "Como aplicar da próxima vez" preenchidos. Se não houver lição concreta, não proponha. Se houve uma decisão, proponha uma nota em `decisoes/`. Só crie depois de o usuário confirmar.
5. Acrescente uma linha na nota de diário do dia. Se ela não existir, crie copiando `_template-diario.md` com o nome AAAA-MM-DD.md.
6. Pergunte, no máximo, a etapa do funil e a data do próximo contato, se o usuário não disse. Responda em até três linhas com o que foi atualizado.

## Saída esperada

Ficha do cliente atualizada, diário do dia atualizado e, se couber, uma proposta de aprendizado ou decisão.

## Regras

Nível 1. Registre só o que o usuário contou. Não preencha motivos ou intenções do cliente por suposição.
