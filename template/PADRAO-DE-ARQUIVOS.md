---
tipo: guia
titulo: Padrão de arquivos
resumo: Regras de formato dos arquivos .md do cérebro para que a IA os encontre, entenda e atualize com segurança.
status: vigente
atualizado_em: {{DATA}}
fonte: estrutura inicial
relacionados: [AGENTS.md]
---

# Padrão de arquivos

## Por que existe

A IA lê muito texto e erra quando os arquivos são longos, vagos ou diferentes entre si. Este padrão deixa todo arquivo previsível: ela sabe onde está cada informação, o que vale e o que está pendente.

## Anatomia de todo arquivo

1. Frontmatter entre linhas `---` no topo, com os campos abaixo.
2. Um título H1 igual ao campo `titulo`.
3. Seções H2 fixas, na ordem do modelo do tipo. Não renomeie seções.
4. Conteúdo curto, afirmativo e específico.

## Campos do frontmatter

- `tipo` — um de: contexto, decisao, aprendizado, cliente, projeto, diario, prioridade, inbox, indice, guia, conector.
- `titulo` — nome curto do arquivo.
- `resumo` — uma frase de até 200 caracteres dizendo o que o arquivo contém. A IA usa o resumo para decidir se abre o arquivo. Reescreva o resumo sempre que o conteúdo mudar.
- `status` — rascunho (ainda não revisado pela pessoa), vigente (revisado e confirmado; lacunas que sobrarem continuam marcadas com [A PREENCHER]), substituido (não vale mais), arquivado (histórico), modelo (template), reservado (ainda não usar).
- `atualizado_em` — data AAAA-MM-DD da última alteração.
- `fonte` — de onde veio a informação (entrevista inicial, site da empresa, reunião de AAAA-MM-DD, e-mail, conversa com a IA, documento).
- `relacionados` — lista de caminhos relativos de arquivos ligados a este.

Campos extras por tipo ficam abaixo dos comuns. Cliente: nome, apelidos, id_crm, responsavel, etapa_funil, produto, proximo_contato, ultimo_resultado. Decisão: data, decisor, cliente, projeto, revisar_em, substituido_por. Aprendizado: data, origem, cliente, categoria. Projeto: responsavel, prazo, andamento. Diário: data, clientes. Inbox: origem, data, cliente, processado. Plano de sucesso (tipo cliente, em 02-Memoria/sucesso): nome, cliente, responsavel, inicio, saude, proxima_revisao, proximo_contato. Histórico antigo de cliente (tipo cliente, em 02-Memoria/clientes/historico): cliente. O campo `cliente` sempre leva o nome do arquivo da ficha do cliente, sem `.md` (por exemplo, casa-clara-esquadrias), ou a palavra vazio quando a nota não é sobre um cliente.

## Regras de escrita

- Uma ideia principal por arquivo. Passou de 400 palavras, divida em dois arquivos e ligue-os em `relacionados`.
- Frases afirmativas e específicas. Troque "vendemos para vários segmentos" por "vendemos para clínicas odontológicas de 2 a 10 cadeiras".
- Datas no formato AAAA-MM-DD. Valores com moeda e período (R$ 1.200 por mês).
- Nome completo de pessoas e empresas na primeira menção em cada arquivo.
- Listas curtas com hífen. Evite tabelas largas, imagens como fonte de informação e blocos de código.
- Links em Markdown com caminho relativo: o nome entre colchetes, seguido do caminho entre parênteses, como ../01-Contexto/02-icp.md. Nunca use caminho completo do computador.
- Dúvida ou dado ausente vira `[A PREENCHER]` seguido da pergunta. Nunca preencha com suposição. Dado parcial é escrito na mesma linha: o que se sabe, depois [A PREENCHER] e a pergunta que falta.
- Informação que mudou não é apagada. Crie a nota nova e marque a antiga com `status: substituido` e `substituido_por`.

## Nomes de arquivos

- Notas datadas: `AAAA-MM-DD-assunto-curto.md` (decisões, aprendizados, diário, inbox).
- Clientes e produtos: nome em minúsculas, sem acento, com hífen (`casa-clara-esquadrias.md`). A ficha de cliente leva o nome da empresa, não o do contato. Pessoas sem sobrenome são escritas como foram ditas.
- Modelos começam com `_template-` (a pasta do modelo de skill se chama `template-skill`, porque o nome da skill não aceita sublinhado). Nunca edite um modelo. Copie e preencha a cópia.
- Cada pasta de 01-Contexto e de 02-Memoria, e a pasta 03-Acao, tem um `_index.md` que lista seu conteúdo, uma linha por arquivo.

## Ao copiar um modelo

Todo arquivo novo nasce de uma cópia do modelo. Na cópia, troque `titulo` e o título H1 pelo nome real, escreva um `resumo` verdadeiro, ponha `status: rascunho` (ou `vigente` se estiver completo), atualize `atualizado_em`, preencha os campos extras com um valor só (apague as opções separadas por barra; campos de data levam AAAA-MM-DD, ou a palavra sem se não se aplicam) e apague o que não se aplica. Os modelos têm status modelo e são a única exceção à regra de que o H1 é igual ao `titulo`.

## Índices

O `_index.md` é o mapa da pasta. Tem frontmatter (tipo: indice), uma seção "O que há aqui" com um item por arquivo (link com o nome, um travessão e uma linha de descrição) e uma seção "Quando usar". Ao criar um arquivo, adicione a linha no índice. Ao marcar como substituído, mantenha a linha e escreva "(substituído)".

## Skills

Os roteiros em `03-Acao/skills/` seguem o padrão aberto Agent Skills. Cada um é uma pasta com um `SKILL.md`. O frontmatter tem só `name` (igual ao nome da pasta, minúsculas com hífen) e `description` (diz o que faz e quando usar, até 1024 caracteres). O corpo tem as seções Quando usar, Antes de começar, Passos, Saída esperada e Regras.
