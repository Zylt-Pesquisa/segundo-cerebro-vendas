---
name: registrar-atendimento
description: Registra um contato com cliente na ficha dele e no diário, separando o que foi dito pelo método SPIN: situação, problemas, implicações, necessidades explícitas e o resultado do contato (avanço ou continuação). Use quando o usuário disser que falou, atendeu, ligou, reuniu ou trocou mensagens com um cliente ou lead, ou colar o resumo ou a transcrição de uma reunião, e quiser registrar.
---

# Registrar atendimento

## Quando usar

O usuário acabou de falar com um cliente e conta o que aconteceu, ou cola o resumo ou a transcrição da reunião.

## Antes de começar

Leia `01-Contexto/08-metodo-spin.md` para aplicar as marcas e as definições do SPIN, `02-Memoria/clientes/_index.md` para achar a ficha do cliente, `01-Contexto/07-processo-comercial.md` para usar os nomes certos das etapas e `02-Memoria/decisoes/_index.md` para saber se alguma decisão vigente se aplica ao que o cliente pediu.

## Passos

1. Identifique o cliente pela regra 8 de "Como escrever" do `AGENTS.md`: procure no índice e nos campos `nome`, `apelidos` e `id_crm`, e pergunte se achar um nome parecido. Se o cliente for novo, crie a ficha copiando `_template-cliente.md` com o nome da empresa em minúsculas e hífen, e adicione ao índice com a etapa e os apelidos. Se a ficha for do modelo antigo, acrescente as seções e os campos que faltarem (Problemas, Implicações, Necessidades explícitas, Oportunidades, `apelidos`, `id_crm`), sem apagar nada.
2. Descubra de qual oportunidade o contato trata. Se for uma venda nova para o mesmo cliente, acrescente uma linha em Oportunidades em vez de criar outra ficha.
3. Se o usuário colou uma transcrição ou um texto longo, guarde o texto bruto em `02-Memoria/_inbox/` como manda a skill salvar-no-cerebro, com o campo `cliente` preenchido, e ligue o item à ficha em `relacionados`.
4. Separe o que foi dito e grave em cada seção da ficha, com a data do contato. Fatos novos sobre o cliente vão em Situação. Dificuldades vão em Problemas, com [fato] se o cliente disse e [hipótese] se foi o vendedor que deduziu. Consequências vão em Implicações, com o número e quem o disse; número sem confirmação do cliente leva [estimativa]. Desejos declarados vão em Necessidades explícitas, entre aspas, com as palavras do cliente.
5. Se o cliente confirmou uma hipótese antiga, troque a marca para [fato] e anote a data. Não apague a linha.
6. Classifique o resultado do contato como avanço, continuação, pedido ou sem venda, pelas definições do `08-metodo-spin.md`. Se não ficar claro, pergunte qual compromisso concreto o cliente assumiu.
7. Acrescente no topo da seção Histórico uma entrada com data, canal, oportunidade, o que foi dito, objeções, o que ficou combinado e o resultado.
8. Atualize a linha da oportunidade em Oportunidades e, no frontmatter, `etapa_funil`, `proximo_contato`, `ultimo_resultado` e `atualizado_em`. Reescreva o `resumo` se a situação mudou. Em Próximo passo, escreva o avanço a buscar no próximo contato. Se o Histórico passar de 10 entradas, aplique a regra 10 de "Como escrever" do `AGENTS.md`.
9. Se apareceu uma objeção nova ou uma lição concreta, proponha criar uma nota em `aprendizados/`, com o campo `cliente` preenchido, já com "O que aprendemos" e "Como aplicar da próxima vez" preenchidos. Se uma pergunta funcionou bem, proponha acrescentá-la ao Banco de perguntas do `08-metodo-spin.md`. Se houve uma decisão, proponha uma nota em `decisoes/`. Só crie depois de o usuário confirmar.
10. Acrescente uma linha na nota de diário do dia e inclua o cliente no campo `clientes`. Se a nota não existir, crie copiando `_template-diario.md` com o nome AAAA-MM-DD.md.
11. Pergunte, no máximo, a etapa do funil, a data do próximo contato e o resultado, se o usuário não disse. Responda em até quatro linhas com o que foi atualizado e um alerta SPIN quando couber, como "ainda não há necessidade explícita registrada" ou "segunda continuação seguida".

## Saída esperada

Ficha do cliente atualizada nas seções SPIN, Histórico com o resultado do contato, diário do dia atualizado e, se couber, uma proposta de aprendizado, decisão ou pergunta nova.

## Regras

Nível 1. Registre só o que o usuário contou. Não preencha motivos ou intenções do cliente por suposição. Nunca marque como [fato] o que o cliente não disse, e nunca transforme queixa vaga em necessidade explícita. Nunca grave na ficha de um cliente sem ter certeza de que é ele.
