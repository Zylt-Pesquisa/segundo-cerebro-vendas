---
name: revisar-carteira
description: Revisa a carteira e o pipeline lendo as fichas do Segundo Cérebro e mostra o que precisa de atenção: contatos atrasados e da semana, oportunidades sem próximo passo, negócios parados em continuação, propostas sem necessidade explícita ou sem decisor, etapas fora do critério, decisões para revisar e o funil por etapa, com o avanço a pedir em cada caso. Use quando o usuário perguntar quem precisa contatar, o que está atrasado ou travado, como está a carteira, o funil ou o pipeline, pedir a revisão da semana ou preparar a reunião de pipeline, ou quando uma tarefa agendada pedir a revisão da carteira.
---

# Revisar carteira

## Quando usar

O vendedor ou o gestor quer saber o que fazer primeiro com os clientes: quem contatar, o que está atrasado, o que está travado e como está o funil. Serve para a revisão da semana, para a reunião de pipeline e para uma tarefa agendada, por exemplo toda segunda de manhã.

## Antes de começar

Leia `02-Memoria/clientes/_index.md`, `01-Contexto/07-processo-comercial.md` (etapas, critérios de passagem e cadência), `01-Contexto/08-metodo-spin.md`, `02-Memoria/prioridades/atual.md` e `02-Memoria/decisoes/_index.md`. Depois abra cada ficha de cliente, menos o modelo e as fichas com `status: substituido` ou `arquivado`. Em cada uma, leia o frontmatter e as seções Decisores e contatos, Necessidades explícitas, Oportunidades e as três entradas mais recentes do Histórico. Clientes já em pós-venda com plano em `02-Memoria/sucesso/` ficam para a skill radar-de-contas, se ela existir.

## Passos

1. Use a data de hoje. Se o usuário pediu a carteira de um vendedor, uma etapa ou só as maiores oportunidades, aplique o filtro (`responsavel`, `etapa_funil` ou valor).
2. Considere só oportunidades abertas. Cliente com todas as oportunidades ganhas ou perdidas fica de fora, a menos que tenha `proximo_contato` marcado.
3. Atrasados: `proximo_contato` antes de hoje, do mais atrasado para o menos, com os dias de atraso.
4. Esta semana: `proximo_contato` de hoje até daqui a 7 dias, em ordem de data.
5. Sem próximo passo: oportunidade aberta sem data em `proximo_contato` (vazio, AAAA-MM-DD ou A PREENCHER).
6. Parados: `ultimo_resultado` igual a continuação, com destaque para duas ou mais continuações seguidas no Histórico. Se a cadência estiver preenchida no `07-processo-comercial.md`, inclua quem está sem contato há mais tempo que ela.
7. Em risco pelo SPIN: oportunidades em etapa de proposta ou depois sem nenhuma necessidade explícita registrada, ou sem nenhum decisor em Decisores e contatos.
8. Etapa a revisar: oportunidades cuja etapa não bate com os critérios de passagem do `07-processo-comercial.md`, quando eles estiverem preenchidos.
9. Decisões para revisar: decisões vigentes com `revisar_em` antes de hoje ou nos próximos 7 dias.
10. Funil: quantas oportunidades abertas existem em cada etapa e, se houver valor registrado, a soma por etapa.
11. Para cada cliente dos passos 3 a 8, sugira em uma linha o avanço concreto a pedir no próximo contato e, quando o problema for continuação ou falta de necessidade explícita, uma pergunta de Implicação ou de Necessidade de solução para destravar. Ordene os casos em risco pelas prioridades atuais.
12. Termine oferecendo preparar a reunião ou escrever o follow-up do primeiro cliente da lista, salvar a revisão na nota de diário do dia e atualizar o `proximo_contato` das fichas que o usuário confirmar.

## Saída esperada

Uma lista curta, em blocos, nesta ordem: Atrasados, Esta semana, Sem próximo passo, Parados, Em risco pelo SPIN, Etapa a revisar, Decisões para revisar e Funil por etapa. Cada cliente em uma linha, com nome, etapa, data, avanço a pedir e, quando couber, a pergunta para destravar, citando a ficha. Bloco sem itens não aparece. Com mais de 30 clientes, mostre até 10 por bloco e diga quantos ficaram de fora. Fichas com data inválida ou campos que impedem a revisão aparecem no fim, em Fichas para corrigir. Feche com um resumo de três linhas: quantas oportunidades estão saudáveis, quantas em risco e quantas pedem revisão de etapa.

## Regras

Nível 0 para a análise. Salvar no diário e atualizar `proximo_contato` são nível 1 e só acontecem com a confirmação do usuário. Não mude etapa do funil sem confirmação. Não altere o CRM. Não invente datas nem etapas: o que não está na ficha vai para Sem próximo passo ou Fichas para corrigir. Quando rodar por tarefa agendada, sem ninguém para responder, não faça perguntas nem grave nada: use a carteira inteira, ou o vendedor indicado na tarefa, e entregue a lista.
