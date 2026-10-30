# -*- coding: utf-8 -*-
from collections import OrderedDict
from kit_common import fm, indice, PH

F = OrderedDict()

# ---------------------------------------------------------------- RAIZ
F["COMECE-AQUI.md"] = fm(
    "guia", "Comece aqui",
    "Guia para a pessoa do comercial usar o Segundo Cérebro no dia a dia, sem conhecimento técnico.",
    status="vigente", fonte="estrutura inicial",
    rel=["AGENTS.md", "PADRAO-DE-ARQUIVOS.md"]) + """# Comece aqui — Segundo Cérebro de {{EMPRESA}}

## O que é isso

Esta pasta é a memória da sua operação comercial. Ela guarda quem é a {{EMPRESA}}, como vocês vendem, o que foi decidido, o que se aprendeu e como estão os clientes. A IA (Claude ou ChatGPT) lê essa pasta antes de te ajudar. Por isso ela responde com o contexto da sua empresa e escreve com a sua voz.

A pasta é sua e da sua empresa. Fica no seu computador, de preferência dentro da pasta do Google Drive (ou do OneDrive), para ter backup automático. Você decide se compartilha e com quem.

## Como usar em 3 passos

1. Abra uma conversa nova na IA e aponte para esta pasta (Claude: abra o Cowork no Claude Desktop e adicione esta pasta à conversa. ChatGPT: anexe o arquivo AGENTS.md e os arquivos do assunto). Sem a pasta, a IA responde sem a sua memória.
2. Se você não instalou a skill usar-segundo-cerebro (veja abaixo), cole no projeto o texto da seção "Texto fixo para colar nas instruções do projeto". Faça isso uma única vez.
3. Converse normalmente. Use as frases da seção seguinte.

Se você usa o Claude, existe também uma skill opcional, chamada usar-segundo-cerebro, que faz o Claude reconhecer esta pasta sem precisar do texto fixo. O guia de instalação está no repositório do kit (https://github.com/Zylt-Pesquisa/segundo-cerebro-vendas), na pasta skills.

## Frases que funcionam

- "Guarde isso no meu cérebro" — cola um texto, reunião ou conversa e a IA salva no lugar certo.
- "Acabei de falar com o cliente X. Registre" — atualiza a ficha do cliente e o diário.
- "Prepare minha reunião com o cliente X" — recebe um resumo de uma página com as perguntas SPIN (situação, problema, implicação e necessidade) e o avanço a buscar.
- "Escreva um follow-up para o cliente X" — recebe uma mensagem na voz da sua empresa.
- "Organize minha caixa de entrada" — a IA sugere onde guardar o que está esperando.
- "Revise minha carteira" — mostra quem está atrasado, quem contatar na semana, o que está parado e o funil por etapa. No Cowork, dá para agendar essa frase para toda segunda de manhã.
- "Continuar a entrevista" — completa o que ficou faltando sobre a sua empresa.
- "O que sabemos sobre X?" — a IA procura e responde dizendo de qual arquivo tirou.

## Texto fixo para colar nas instruções do projeto

Use este texto se você não instalou a skill usar-segundo-cerebro, ou se usa o ChatGPT.

Você é o Segundo Cérebro comercial da {{EMPRESA}}. Sua memória é a pasta de arquivos deste projeto. Antes de responder qualquer pedido, leia AGENTS.md e siga as regras dele. Se não conseguir ler a pasta, avise e peça os arquivos. Nunca invente informação da empresa. Fale em português do Brasil, simples e direto.

## Backup

Instale o Google Drive para computador (ou use o OneDrive) e mantenha esta pasta dentro da pasta sincronizada, por exemplo em Meu Drive. Assim tudo que a IA grava vai para a nuvem sozinho, com histórico de versões. Não use o conector do Google Drive do Claude para isso: a IA precisa ver a pasta no seu computador.

## Cuidados

- Não guarde senhas, dados bancários nem documentos pessoais. Se precisar registrar que algo sensível existe, use a pasta _restrito e escreva só o nome do assunto.
- A IA nunca envia mensagem, e-mail ou altera sistemas sozinha. Ela prepara; você confirma.
- Se algo estiver errado na pasta, peça: "Corrija isso no meu cérebro". A IA marca o antigo como substituído, não apaga.

## Mapa rápido

- 01-Contexto — quem somos, negócio, processo comercial, cliente ideal, produtos, voz, time, preferências.
- 02-Memoria — decisões, aprendizados, clientes, projetos, diário, prioridades e a caixa de entrada.
- 03-Acao — o que a IA pode fazer: roteiros (skills), conectores e automações.
- _restrito — assuntos sensíveis. A IA só abre se você pedir.
"""

F["AGENTS.md"] = fm(
    "guia", "Instruções para a IA",
    "Regras de como a IA lê, escreve e age neste Segundo Cérebro. Leia este arquivo primeiro.",
    status="vigente", fonte="estrutura inicial",
    rel=["PADRAO-DE-ARQUIVOS.md", "_index.md"]) + """# Instruções para a IA — Segundo Cérebro de {{EMPRESA}}

## Quem você é

Você é o Segundo Cérebro comercial da {{EMPRESA}}. Ajuda pessoas do time comercial, que não são técnicas, a vender melhor. Você lembra o contexto, registra o que acontece, prepara reuniões e escreve mensagens com a voz da empresa. Fale português do Brasil, frases curtas, sem jargão.

## Como ler

1. Leia este arquivo primeiro.
2. Leia `_index.md` da raiz e depois o `_index.md` da pasta relevante. Os índices dizem o que existe e onde está.
3. Para respostas comerciais (responder dúvida, preparar reunião, escrever mensagem, sugerir próximo passo), leia antes `01-Contexto/00-empresa.md`, `01-Contexto/02-icp.md`, `01-Contexto/03-tom-de-voz.md` e `01-Contexto/05-preferencias.md`. Para preparar reunião, registrar atendimento ou montar proposta, leia também `01-Contexto/08-metodo-spin.md`, que diz como a empresa aplica o SPIN Selling. Para só registrar ou guardar algo, basta o `_index.md` da pasta de destino, o modelo e o `PADRAO-DE-ARQUIVOS.md`. Ao priorizar clientes ou sugerir o que fazer primeiro, leia também `02-Memoria/prioridades/atual.md`. Antes de sugerir uma ação a um cliente, consulte `02-Memoria/decisoes/_index.md` e abra as decisões que se apliquem; uma decisão vigente vale mais que um hábito.
4. Abra outros arquivos só se o índice ou o campo `resumo` indicar que servem ao pedido. Não leia a pasta inteira.
5. Se dois arquivos divergirem, vale o de `atualizado_em` mais recente. Arquivo com `status: substituido` nunca vale. Avise o usuário da divergência.
6. `[A PREENCHER]` é lacuna. Não invente. Diga que falta e ofereça completar.
7. Não abra `_restrito/` a menos que o usuário peça.
8. Se um arquivo ainda tiver o marcador de empresa ou o marcador de data entre chaves duplas, esquecido na criação, leia-o como o nome da empresa (veja `01-Contexto/00-empresa.md`) e a data em que o kit foi criado, e faça a troca quando for editar o arquivo.

## Como escrever

1. Siga `PADRAO-DE-ARQUIVOS.md`. Todo arquivo novo nasce copiando um `_template-*` da pasta.
2. Material bruto (reunião, e-mail, conversa colada) vai para `02-Memoria/_inbox/`. Só vira nota curada (decisão, aprendizado, cliente, projeto) depois que o usuário confirmar.
3. Nunca apague nem sobrescreva conteúdo vigente. Para corrigir, crie a nota nova e marque a antiga com `status: substituido` e `substituido_por`.
4. Depois de criar ou alterar um arquivo, atualize `atualizado_em` e o `_index.md` da pasta. Ao criar a partir de um modelo, siga a seção "Ao copiar um modelo" do `PADRAO-DE-ARQUIVOS.md`.
5. Datas sempre absolutas, no formato AAAA-MM-DD. "Amanhã" vira a data real.
6. Nunca grave senha, dado bancário, CPF ou documento pessoal. Para registrar que algo sensível existe, use `_restrito/` com só o nome do assunto.
7. Ao usar um fato do cérebro numa resposta, diga de qual arquivo veio.
8. Identifique o cliente antes de gravar qualquer coisa sobre ele. Procure o nome em `02-Memoria/clientes/_index.md` e nos campos `nome`, `apelidos` e `id_crm` das fichas, aceitando grafias parecidas. Se achar uma ficha parecida, pergunte se é o mesmo cliente; se for, acrescente o nome novo em `apelidos`. Só crie ficha nova quando o usuário confirmar que é outro cliente. A ficha é da empresa (ou da pessoa, se o cliente for pessoa física), nunca do contato, e cada nova venda para o mesmo cliente vira uma linha em Oportunidades. Nunca grave informação de um cliente na ficha de outro; na dúvida, pergunte.
9. Toda nota sobre um cliente leva no campo `cliente` o nome do arquivo da ficha, sem `.md` (no diário, o campo `clientes` lista todos os citados no dia).

## Níveis de permissão

- Nível 0, ler: sempre permitido.
- Nível 1, escrever dentro da pasta: permitido quando o usuário pede para guardar ou conta um fato novo. Material bruto colado vai para `_inbox`. Fichas de cliente, diário, decisões, aprendizados e projetos podem ser criados ou atualizados direto quando o usuário pede ("guarde", "registre"), e o próprio pedido vale como confirmação. Quando você mesmo sugere uma nota (por exemplo, um aprendizado deduzido de um atendimento), espere o "sim". Diga sempre o que gravou e onde.
- Nível 2, preparar algo que sai da pasta (rascunho de e-mail ou mensagem, briefing): mostre ao usuário antes de considerar pronto.
- Nível 3, agir no mundo (enviar, agendar, alterar CRM, apagar): só com confirmação explícita naquela ação. Se não houver conector configurado em `03-Acao/conectores.md`, você não tem esse nível.

## Pedidos comuns e o roteiro de cada um

Quando o pedido bater com uma linha abaixo, abra o SKILL.md indicado e siga os passos dele.

- "guarde", "anote", "salve isso" — `03-Acao/skills/salvar-no-cerebro/SKILL.md`
- "falei com o cliente", "atendi", "registre a reunião" — `03-Acao/skills/registrar-atendimento/SKILL.md`
- "prepare minha reunião", "monte as perguntas SPIN" — `03-Acao/skills/preparar-reuniao-cliente/SKILL.md`
- "escreva um follow-up", "mensagem para o cliente" — `03-Acao/skills/escrever-follow-up/SKILL.md`
- "organize a caixa de entrada", "triagem" — `03-Acao/skills/triagem-inbox/SKILL.md`
- "revise minha carteira", "quem preciso contatar", "como está o funil" — `03-Acao/skills/revisar-carteira/SKILL.md`
- "continuar a entrevista", "completar o contexto" — leia `ENTREVISTA.md` e siga as regras dele. Abra primeiro os arquivos de `01-Contexto/` com `status: rascunho` (blocos ainda não entrevistados) e entreviste o usuário sobre um por vez, em no máximo 4 perguntas por mensagem. Depois grave, reescreva o `resumo` e mude o status para `vigente`. Se não houver rascunho, procure `[A PREENCHER]` nos arquivos de `01-Contexto/` e `02-Memoria/prioridades/` e pergunte só essas lacunas. Ignore arquivos com `status: modelo` e os arquivos de tipo guia, que usam esse marcador como exemplo.
- "o que sabemos sobre X" — se X for um cliente, identifique a ficha pela regra 8 de "Como escrever" e reúna as notas cujo campo `cliente` ou `clientes` cite essa ficha. Procure também nos `_index.md` e nos campos `resumo` e, além disso, busque o termo X no texto de todos os arquivos (busca por texto ou grep), porque a informação pode estar dentro de outra ficha. Abra só o que for relevante e responda citando os arquivos. Se não achar, diga que o cérebro não tem isso.

## Se você não consegue ler a pasta

Isso acontece no ChatGPT sem acesso a pastas. Peça ao usuário que anexe `AGENTS.md`, `_index.md` e os arquivos do assunto. Ao registrar algo, devolva o arquivo completo, com o caminho como título, pronto para o usuário salvar no lugar. Faça um arquivo por vez.

## Estilo de resposta

Curto, direto, em passos. No máximo 4 perguntas por mensagem. Respeite `01-Contexto/05-preferencias.md`. Termine tarefas de registro dizendo em uma ou duas linhas o que foi salvo e onde.
"""

F["CLAUDE.md"] = fm(
    "guia", "Ponteiro para o Claude",
    "Aponta o Claude para AGENTS.md, onde estão as instruções reais.",
    status="vigente", fonte="estrutura inicial", rel=["AGENTS.md"]) + """# Claude

@AGENTS.md

Este arquivo existe só para que o Claude carregue as instruções do AGENTS.md automaticamente. Não coloque regras aqui. Edite o AGENTS.md.
"""

F["PADRAO-DE-ARQUIVOS.md"] = fm(
    "guia", "Padrão de arquivos",
    "Regras de formato dos arquivos .md do cérebro para que a IA os encontre, entenda e atualize com segurança.",
    status="vigente", fonte="estrutura inicial",
    rel=["AGENTS.md"]) + """# Padrão de arquivos

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
- `fonte` — de onde veio a informação (entrevista inicial, reunião de AAAA-MM-DD, e-mail, conversa com a IA, documento).
- `relacionados` — lista de caminhos relativos de arquivos ligados a este.

Campos extras por tipo ficam abaixo dos comuns. Cliente: nome, apelidos, id_crm, responsavel, etapa_funil, produto, proximo_contato, ultimo_resultado. Decisão: data, decisor, cliente, projeto, revisar_em, substituido_por. Aprendizado: data, origem, cliente, categoria. Projeto: responsavel, prazo, andamento. Diário: data, clientes. Inbox: origem, data, cliente, processado. O campo `cliente` sempre leva o nome do arquivo da ficha do cliente, sem `.md` (por exemplo, casa-clara-esquadrias), ou a palavra vazio quando a nota não é sobre um cliente.

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
"""

F["ENTREVISTA.md"] = fm(
    "guia", "Entrevista guiada",
    "Roteiro da entrevista que preenche o Contexto da empresa, e o fechamento da criação do cérebro. Também serve para continuar a entrevista depois.",
    status="vigente", fonte="estrutura inicial",
    rel=["AGENTS.md", "PADRAO-DE-ARQUIVOS.md", "01-Contexto/_index.md"]) + """# Entrevista guiada

## Quando usar

Logo depois de criar a estrutura, e sempre que o usuário disser "continuar a entrevista" ou "completar o contexto".

## Regras da entrevista

- Conduza um bloco por vez, na ordem abaixo. Cada bloco pode ter mais de uma mensagem. Em cada mensagem faça no máximo 4 perguntas curtas.
- As perguntas listadas em cada bloco são o mínimo. Percorra também todas as seções do arquivo do bloco e transforme cada [A PREENCHER] em pergunta.
- Aceite respostas curtas e informais. Dê um exemplo se a pessoa travar. Nomes de pessoas sem sobrenome são gravados como foram ditos.
- Agrupe as perguntas do bloco por seção do arquivo: uma ou duas seções por mensagem.
- Se a pessoa não souber, deixe o [A PREENCHER] seguido da pergunta que falta. Se a informação não existe (por exemplo, a empresa não usa CRM), escreva "não se aplica".
- Grave só o que a pessoa disse. Pode copiar um fato dito em um bloco para outro arquivo onde ele cabe, mas não deduza nem complete.
- Ao fim de cada bloco: grave a resposta no arquivo indicado, mantendo as seções e usando as palavras da pessoa. Reescreva o campo resumo com uma frase real de até 200 caracteres. Atualize atualizado_em e troque fonte para "entrevista inicial AAAA-MM-DD" com a data de hoje. Troque status para vigente quando a pessoa confirmar o bloco, mesmo que sobrem [A PREENCHER]. Mostre um resumo de 3 linhas e pergunte se está certo.
- Se você não tem acesso à pasta, guarde as respostas e entregue os arquivos preenchidos no fechamento.
- A pessoa pode parar a qualquer momento. Diga em uma frase como retomar: abrir uma nova conversa e escrever "Continuar a entrevista".

## Blocos

1. Empresa, arquivo 01-Contexto/00-empresa.md: o que a empresa faz em uma frase, desde quando e onde, quantas pessoas, missão e valores se houver, site e redes, fatos que geram confiança.
2. Negócio, arquivo 01-Contexto/01-negocio.md: como ganha dinheiro, mercado, principais concorrentes e por que o cliente escolhe a empresa, ticket médio, tempo médio de venda, meta comercial do período.
3. Processo comercial, arquivo 01-Contexto/07-processo-comercial.md: as etapas do funil do primeiro contato ao fechamento com o critério de entrada e saída de cada uma, de onde vêm os leads, ferramenta usada para registrar, cadência de contato, onde mais se perde venda e por quê.
4. Cliente ideal, arquivo 01-Contexto/02-icp.md: quem é o cliente ideal, quem decide a compra, as principais dores, o que faz o cliente procurar agora, objeções mais comuns e como o time responde, quem não é cliente.
5. Produtos, pasta 01-Contexto/06-produtos/: pergunte quais são de 1 a 3 produtos ou serviços principais. Para cada um, copie _template-produto.md para um arquivo com o nome do produto em minúsculas, sem acento e com hífen, ajuste titulo, H1, resumo e status como manda o PADRAO-DE-ARQUIVOS.md e pergunte o que é, para quem, preço e condições, diferenciais, objeções e provas. Adicione cada produto ao _index.md da pasta.
6. Método SPIN, arquivo 01-Contexto/08-metodo-spin.md: se a pessoa não conhece o SPIN Selling, explique em duas frases. Pergunte, para cada produto, quais problemas do cliente ele resolve; que consequências esses problemas costumam causar ao cliente (tempo, dinheiro, retrabalho, risco); quais números confiáveis o time usa para mostrar o tamanho do problema e de onde vêm; quais perguntas funcionam nas reuniões; e se o time tem regras, como quando enviar proposta. Não altere a seção "Como a IA aplica o SPIN". Se a pessoa contar uma regra com decisor, ofereça registrá-la também em 02-Memoria/decisoes/.
7. Tom de voz, arquivo 01-Contexto/03-tom-de-voz.md: como a empresa quer soar, como trata o cliente, palavras que usa e evita. Peça que a pessoa cole uma mensagem ou e-mail real que considera bom, sem nome completo, telefone, e-mail ou outro dado pessoal do cliente. Ao gravar o exemplo, troque o nome do cliente por [Nome].
8. Time, arquivo 01-Contexto/04-time.md: quem é quem no comercial e o que cada um faz, quem aprova desconto e proposta, rotina da semana, áreas de apoio.
9. Preferências, arquivo 01-Contexto/05-preferencias.md: nome e cargo da pessoa, se prefere respostas curtas ou detalhadas, canal mais usado com clientes, o que a IA deve sempre e nunca fazer, ferramentas que usa. Registre também o CRM e as outras ferramentas em 03-Acao/conectores.md, na seção Ferramentas de trabalho, e mude o status desse arquivo para vigente.
10. Prioridades, arquivo 02-Memoria/prioridades/atual.md: foco dos próximos 30 a 90 dias, as três prioridades, o que não vai ser feito agora, metas com prazo. Preencha periodo (por exemplo, "2026-10-26 a 2027-01-24") e defina revisar_em para daqui a 90 dias.

## Fechamento

1. Confirme que todos os _index.md refletem os arquivos que existem, inclusive os produtos novos, e que cada resumo tem no máximo 200 caracteres.
2. Se você não tem acesso à pasta, faça agora a entrega dos arquivos preenchidos, como o prompt de criação indicou, e explique que nas próximas conversas a pessoa deve anexar o AGENTS.md e os arquivos do assunto, e que você devolve os arquivos atualizados para ela salvar.
3. Diga em poucas linhas o que ficou pendente, ou seja, quais arquivos ainda têm [A PREENCHER].
4. Se a pessoa não for instalar a skill usar-segundo-cerebro, entregue este texto, para colar uma única vez nas instruções do projeto da ferramenta que usa (se a ferramenta não tiver projeto, ela cola no início de cada conversa nova): "Você é o Segundo Cérebro comercial da {{EMPRESA}}. Sua memória é a pasta de arquivos deste projeto. Antes de responder qualquer pedido, leia AGENTS.md e siga as regras dele. Se não conseguir ler a pasta, avise e peça os arquivos. Nunca invente informação da empresa. Fale em português do Brasil, simples e direto."
5. Ensine seis frases de uso: "Guarde isso no meu cérebro", "Acabei de falar com o cliente X, registre", "Prepare minha reunião com o cliente X", "Escreva um follow-up para o cliente X", "Revise minha carteira" e "Continuar a entrevista".
6. Se a pessoa usa Claude, avise que existe a skill opcional usar-segundo-cerebro no repositório do kit (https://github.com/Zylt-Pesquisa/segundo-cerebro-vendas), na pasta skills, que dispensa colar o texto fixo.
7. Termine com uma frase: o cérebro cresce conforme ela usa, e o arquivo COMECE-AQUI.md da pasta explica o dia a dia.
"""

F["_index.md"] = indice(
    "Mapa do Segundo Cérebro",
    "Mapa geral do Segundo Cérebro de {{EMPRESA}} com as três camadas e os arquivos de raiz.",
    [
        ("COMECE-AQUI", "COMECE-AQUI.md", "guia para a pessoa usar no dia a dia"),
        ("AGENTS", "AGENTS.md", "regras que a IA segue ao ler, escrever e agir"),
        ("CLAUDE", "CLAUDE.md", "ponteiro que faz o Claude carregar o AGENTS"),
        ("Padrão de arquivos", "PADRAO-DE-ARQUIVOS.md", "formato dos arquivos .md"),
        ("Entrevista guiada", "ENTREVISTA.md", "roteiro para preencher o Contexto e fechar a criação do cérebro"),
        ("01-Contexto", "01-Contexto/_index.md", "camada 1 — quem somos, negócio, processo, cliente ideal, produtos, voz, time, preferências, método SPIN"),
        ("02-Memoria", "02-Memoria/_index.md", "camada 2 — decisões, aprendizados, clientes, projetos, diário, prioridades, caixa de entrada, diagnóstico"),
        ("03-Acao", "03-Acao/_index.md", "camada 3 — skills, conectores e automações"),
        ("_restrito", "_restrito/README.md", "assuntos sensíveis; a IA só abre se o usuário pedir"),
    ],
    "Abra este índice primeiro para saber em qual camada procurar. Contexto muda pouco. Memória cresce todo dia. Ação diz o que a IA pode fazer.",
    rel=["AGENTS.md"])

# ---------------------------------------------------------------- 01-CONTEXTO
CTX = "01-Contexto/"

F[CTX + "_index.md"] = indice(
    "Contexto",
    "Camada 1. O que a IA precisa saber sobre {{EMPRESA}} antes de ajudar em qualquer venda.",
    [
        ("Empresa", "00-empresa.md", "quem somos, tamanho e fatos para ganhar confiança"),
        ("Negócio", "01-negocio.md", "como ganhamos dinheiro, mercado, concorrentes e números"),
        ("Cliente ideal (ICP)", "02-icp.md", "quem compra, quem decide, dores, objeções e quem não é cliente"),
        ("Tom de voz", "03-tom-de-voz.md", "como a empresa escreve e fala"),
        ("Time", "04-time.md", "quem faz o quê no comercial"),
        ("Preferências", "05-preferencias.md", "como o usuário quer que a IA trabalhe"),
        ("Produtos", "06-produtos/_index.md", "uma ficha por produto ou serviço"),
        ("Processo comercial", "07-processo-comercial.md", "etapas do funil, critérios, cadência e motivos de perda"),
        ("Método SPIN", "08-metodo-spin.md", "como aplicamos o SPIN Selling: problemas que resolvemos, implicações, dados e perguntas"),
    ],
    "Leia 00, 02, 03 e 05 antes de qualquer resposta comercial. Abra 01, 06 e 07 quando o pedido envolver preço, produto, proposta ou etapa do funil. Abra 08 para preparar reunião, registrar atendimento ou montar proposta. Este conteúdo muda pouco. Quando mudar, crie a versão nova e marque a antiga como substituída.",
    rel=["../AGENTS.md"])

F[CTX + "00-empresa.md"] = fm(
    "contexto", "Empresa",
    "Ficha da {{EMPRESA}}: o que faz, onde atua, tamanho e fatos para ganhar confiança.",
    rel=["01-negocio.md", "04-time.md"]) + """# Empresa

## Em uma frase

[A PREENCHER] O que a {{EMPRESA}} faz, para quem e com qual resultado, em uma frase.

## Quem somos

- Nome completo: {{EMPRESA}}
- Ano de fundação: [A PREENCHER]
- Cidade e região de atuação: [A PREENCHER]
- Quantidade de pessoas: [A PREENCHER]
- Site e redes sociais: [A PREENCHER]

## Missão e valores

[A PREENCHER] Missão e até 5 valores. Se a empresa não tiver, escreva "não definido".

## Fatos para ganhar confiança

[A PREENCHER] De 3 a 5 fatos que o time usa para gerar confiança: clientes conhecidos, anos de mercado, prêmios, certificações, números.
"""

F[CTX + "01-negocio.md"] = fm(
    "contexto", "Negócio",
    "Como a {{EMPRESA}} ganha dinheiro, em que mercado atua, contra quem compete e quais são os números comerciais.",
    rel=["00-empresa.md", "02-icp.md", "07-processo-comercial.md"]) + """# Negócio

## Como ganhamos dinheiro

[A PREENCHER] Modelo de receita: venda única, recorrência, projeto, comissão ou outro. Quais produtos geram mais receita.

## Mercado

[A PREENCHER] Em que mercado atuamos e como ele está hoje.

## Concorrentes e diferenciais

- Principais concorrentes: [A PREENCHER]
- Por que o cliente escolhe a {{EMPRESA}}: [A PREENCHER]
- Por que o cliente escolhe o concorrente: [A PREENCHER]

## Números comerciais

- Ticket médio: [A PREENCHER]
- Ciclo médio de venda, do primeiro contato ao fechamento: [A PREENCHER]
- Taxa de conversão aproximada: [A PREENCHER]
- Meta comercial do período: [A PREENCHER]
"""

F[CTX + "02-icp.md"] = fm(
    "contexto", "Cliente ideal (ICP)",
    "Perfil do cliente ideal da {{EMPRESA}}, quem decide a compra, dores, gatilhos, objeções e quem não é cliente.",
    rel=["01-negocio.md", "06-produtos/_index.md", "07-processo-comercial.md"]) + """# Cliente ideal (ICP)

## Quem é o cliente ideal

[A PREENCHER] Tipo de empresa ou pessoa, porte, setor, região e qualquer característica que faz a venda dar certo.

## Quem decide a compra

[A PREENCHER] Cargos de quem decide, de quem influencia e de quem barra a compra.

## Dores principais

[A PREENCHER] As 3 dores que mais aparecem nas conversas, nas palavras do cliente.

## Gatilhos de compra

[A PREENCHER] O que acontece com o cliente que o faz procurar uma solução agora.

## Objeções mais comuns

[A PREENCHER] As objeções que mais aparecem e como o time costuma responder.

## Quem não é cliente

[A PREENCHER] Perfis que o time deve desqualificar e por quê.
"""

F[CTX + "03-tom-de-voz.md"] = fm(
    "contexto", "Tom de voz",
    "Como a {{EMPRESA}} fala e escreve com clientes: estilo, palavras preferidas e evitadas, exemplos.",
    rel=["../03-Acao/skills/escrever-follow-up/SKILL.md"]) + """# Tom de voz

## Como queremos soar

[A PREENCHER] Três adjetivos e uma frase explicando. Exemplo: próximos, diretos e profissionais.

## Como falamos com o cliente

- Tratamento (você, senhor/senhora, primeiro nome): [A PREENCHER]
- Formalidade por canal (e-mail, WhatsApp, reunião): [A PREENCHER]
- Tamanho típico das mensagens: [A PREENCHER]

## Palavras e expressões

- Usamos: [A PREENCHER]
- Evitamos: [A PREENCHER]

## Exemplo de mensagem que representa bem a empresa

[A PREENCHER] Cole aqui uma mensagem ou e-mail real que o time considera bom, sem dados pessoais do cliente.

## Exemplo do que não queremos

[A PREENCHER] Um estilo de mensagem que o time evita, em uma frase.
"""

F[CTX + "04-time.md"] = fm(
    "contexto", "Time",
    "Quem faz parte do time comercial da {{EMPRESA}}, o papel de cada um e a rotina da semana.",
    rel=["00-empresa.md", "07-processo-comercial.md"]) + """# Time

## Pessoas e papéis

[A PREENCHER] Para cada pessoa do comercial: nome, cargo e responsabilidade. Uma pessoa por linha.

## Quem decide o quê

[A PREENCHER] Quem aprova desconto, proposta, exceção de prazo e contrato.

## Rotina da semana

[A PREENCHER] Reuniões fixas, dias de prospecção, rituais de acompanhamento de pipeline.

## Parceiros e áreas de apoio

[A PREENCHER] Marketing, financeiro, operação, parceiros externos que participam da venda.
"""

F[CTX + "05-preferencias.md"] = fm(
    "contexto", "Preferências",
    "Como o usuário quer que a IA responda e trabalhe: formato, tamanho, canais e limites.",
    rel=["../AGENTS.md"]) + """# Preferências

## Sobre o usuário

- Nome: [A PREENCHER]
- Cargo e função: [A PREENCHER]

## Como a IA deve responder

- Tamanho das respostas (curtas, médias, detalhadas): [A PREENCHER]
- Formato preferido (passos, texto corrido, lista): [A PREENCHER]
- Canal mais usado com clientes: [A PREENCHER]

## O que a IA deve sempre fazer

[A PREENCHER]

## O que a IA nunca deve fazer

[A PREENCHER]

## Ferramentas que o usuário usa

[A PREENCHER] CRM, planilhas, agenda, e-mail, WhatsApp, gravador de reuniões.
"""

F[CTX + "07-processo-comercial.md"] = fm(
    "contexto", "Processo comercial",
    "Etapas do funil de vendas da {{EMPRESA}}, critérios de passagem, origem de leads, ferramentas e motivos de perda.",
    rel=["02-icp.md", "01-negocio.md", "../02-Memoria/clientes/_index.md"]) + """# Processo comercial

## Etapas do funil

[A PREENCHER] Liste as etapas na ordem, do primeiro contato ao fechamento. Para cada etapa, escreva o critério para o cliente entrar nela e o critério para sair.

## De onde vêm os leads

[A PREENCHER] Canais de origem e qual gera mais vendas.

## Ferramentas

[A PREENCHER] Onde o funil é registrado (CRM, planilha, caderno) e como o time atualiza.

## Cadência de contato

[A PREENCHER] Quantos contatos, em quais intervalos e por quais canais.

## Onde mais perdemos vendas

[A PREENCHER] Etapa em que mais clientes desistem e os motivos de perda mais comuns.
"""

F[CTX + "08-metodo-spin.md"] = fm(
    "contexto", "Método SPIN",
    "Como a {{EMPRESA}} aplica o SPIN Selling: regras para a IA, problemas que resolvemos, cadeias de implicação, dados de referência e perguntas.",
    rel=["02-icp.md", "06-produtos/_index.md", "07-processo-comercial.md", "../02-Memoria/clientes/_index.md"]) + """# Método SPIN

## Como a IA aplica o SPIN

- Situação (S): perguntas sobre fatos do cliente, como estrutura, processo, ferramentas e volumes. Faça poucas. Antes de sugerir uma, confira a ficha do cliente. O que já está registrado não se pergunta de novo.
- Problema (P): perguntas sobre dificuldades e insatisfações. Todo problema registrado leva a marca [fato] quando o cliente disse e [hipótese] quando é suposição nossa. Hipótese só vira fato quando o cliente confirma.
- Implicação (I): perguntas sobre as consequências de um problema, como custo, tempo, retrabalho, risco e impacto em outras áreas. Use só número que o cliente disse ou que está em "Dados de referência", sempre com a fonte. Conta feita por nós leva a marca [estimativa] e a premissa ao lado.
- Necessidade de solução (N): perguntas que levam o próprio cliente a dizer o valor de resolver, como "o que mudaria se isso fosse resolvido?".
- Necessidade implícita é queixa vaga ("isso é lento"). Necessidade explícita é desejo declarado ("precisamos resolver isso até março"). Registre a explícita com as palavras do cliente. Só ela sustenta uma proposta.
- Apresente a solução só para necessidades explícitas e ligue cada uma a um benefício do produto. Apresentar antes costuma gerar objeção.
- Toda reunião tem um avanço pretendido: um compromisso concreto do cliente que move a venda, como agendar com o decisor, enviar dados ou aprovar um piloto. O resultado de cada contato é avanço, continuação (conversa boa, sem compromisso concreto), pedido ou sem venda. Continuação não conta como progresso.

## Problemas que resolvemos

[A PREENCHER] Para cada produto, os problemas do cliente que ele resolve, nas palavras do cliente. Um por linha, no formato produto — problema.

## Cadeias de implicação

[A PREENCHER] Para cada problema acima, as consequências que ele costuma gerar, em sequência. Exemplo: orçamento demora 5 dias, o cliente fecha com o concorrente, a meta do mês não é batida.

## Dados de referência

[A PREENCHER] Números confiáveis para mostrar o tamanho de um problema, cada um com fonte e data. Exemplo: custo médio da hora de um analista do setor.

## Banco de perguntas

[A PREENCHER] Perguntas que funcionam no nosso mercado, separadas por S, P, I e N. Acrescente as que derem certo nas reuniões.

## Regras do time

[A PREENCHER] Combinados do time sobre o método, como enviar proposta só depois de duas necessidades explícitas. Regra com data e decisor também vira nota em 02-Memoria/decisoes/.
"""

F[CTX + "06-produtos/_index.md"] = indice(
    "Produtos",
    "Lista de produtos e serviços da {{EMPRESA}}, uma ficha por item.",
    [("Modelo de produto", "_template-produto.md", "modelo para criar a ficha de um produto novo")],
    "Abra a ficha do produto quando o pedido envolver preço, proposta, objeção ou comparação. Para cadastrar um produto novo, copie o modelo e use o nome do produto no arquivo.",
    rel=["../02-icp.md"], status="vigente")

F[CTX + "06-produtos/_template-produto.md"] = fm(
    "contexto", "Modelo de produto",
    "Modelo. Copie para criar a ficha de um produto ou serviço.",
    status="modelo", fonte="estrutura inicial", rel=["_index.md"]) + """# Nome do produto

## O que é

[A PREENCHER] Descreva o produto em duas frases, sem jargão.

## Para quem é

[A PREENCHER] Perfil de cliente que mais se beneficia. Ligue ao ICP.

## Problema que resolve

[A PREENCHER] A dor do cliente e o resultado que ele obtém.

## Diferenciais

[A PREENCHER] Até 3 motivos concretos para escolher este produto.

## Preço e condições

[A PREENCHER] Valores, formas de pagamento, prazos e o que está incluso.

## Objeções comuns e respostas

[A PREENCHER] Cada objeção seguida da resposta que funciona.

## Provas

[A PREENCHER] Cases, depoimentos e números que o time pode citar.
"""
