---
name: revisar-carteira
description: Revisa a carteira de clientes lendo as fichas do Segundo Cérebro e mostra o que precisa de atenção: contatos atrasados e da semana, oportunidades sem próximo passo, negócios parados em continuação, propostas sem necessidade explícita e o funil por etapa. Use quando o usuário perguntar quem precisa contatar, o que está atrasado, como está a carteira ou o funil, pedir a revisão da semana, ou quando uma tarefa agendada pedir a revisão da carteira.
---

# Revisar carteira

## Quando usar

O usuário quer saber o que fazer primeiro com os clientes: quem contatar, o que está atrasado, o que está parado e como está o funil. Serve também para uma tarefa agendada, por exemplo toda segunda de manhã.

## Antes de começar

Leia `02-Memoria/clientes/_index.md`, `01-Contexto/07-processo-comercial.md` (etapas e cadência de contato), `01-Contexto/08-metodo-spin.md` e `02-Memoria/prioridades/atual.md`. Depois abra cada ficha de cliente, menos o modelo. Em cada uma, leia o frontmatter e as seções Oportunidades, Necessidades explícitas e as três entradas mais recentes do Histórico.

## Passos

1. Use a data de hoje. Se o usuário pediu a carteira de um vendedor, considere só as fichas com aquele `responsavel`.
2. Considere só oportunidades abertas. Cliente com todas as oportunidades ganhas ou perdidas fica de fora, a menos que tenha `proximo_contato` marcado.
3. Atrasados: `proximo_contato` antes de hoje, do mais atrasado para o menos, com os dias de atraso.
4. Esta semana: `proximo_contato` de hoje até daqui a 7 dias, em ordem de data.
5. Sem próximo passo: oportunidade aberta sem data em `proximo_contato` (vazio, AAAA-MM-DD ou A PREENCHER).
6. Parados: `ultimo_resultado` igual a continuação, com destaque para quem teve duas ou mais continuações seguidas no Histórico. Se a cadência de contato estiver preenchida no `07-processo-comercial.md`, inclua quem está sem contato há mais tempo que ela.
7. Sem necessidade explícita: oportunidades em etapa de proposta ou depois (pelos nomes das etapas do `07-processo-comercial.md`) sem nada registrado em Necessidades explícitas. Pelo SPIN, é proposta com risco alto.
8. Funil: quantas oportunidades abertas existem em cada etapa e, se houver valor registrado, a soma por etapa.
9. Para cada cliente dos passos 3 a 7, sugira a próxima ação em uma linha, levando em conta as prioridades atuais. Exemplos: preparar a reunião, escrever follow-up, pedir um compromisso concreto, explorar uma implicação.
10. Termine oferecendo preparar a reunião ou escrever o follow-up do primeiro cliente da lista, e salvar a revisão na nota de diário do dia.

## Saída esperada

Uma lista curta, em blocos, nesta ordem: Atrasados, Esta semana, Sem próximo passo, Parados, Sem necessidade explícita e Funil por etapa. Cada cliente em uma linha, com nome, etapa, data e ação sugerida, citando a ficha. Bloco sem itens não aparece. Com mais de 30 clientes, mostre até 10 por bloco e diga quantos ficaram de fora. Fichas com data inválida ou campos que impedem a revisão aparecem no fim, em Fichas para corrigir.

## Regras

Nível 0: só leitura. Não altere fichas. Salvar no diário é nível 1 e só acontece se o usuário pedir. Não invente datas nem etapas: o que não está na ficha vai para Sem próximo passo ou Fichas para corrigir. Quando rodar por tarefa agendada, sem ninguém para responder, não faça perguntas: use a carteira inteira, ou o vendedor indicado na tarefa, e entregue a lista.
