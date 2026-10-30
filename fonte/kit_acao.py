# -*- coding: utf-8 -*-
from collections import OrderedDict
from kit_common import fm, indice, PH

F = OrderedDict()
A = "03-Acao/"


def skill(name, description, corpo):
    return "---\nname: " + name + "\ndescription: " + description + "\n---\n\n" + corpo.strip() + "\n"


F[A + "_index.md"] = indice(
    "Ação",
    "Camada 3. O que a IA pode fazer pela {{EMPRESA}}: roteiros (skills), conectores e automações.",
    [
        ("Conectores", "conectores.md", "fontes e ferramentas externas e como cada uma entra no cérebro"),
        ("Automações", "automacoes/README.md", "reservado para rotinas automáticas futuras"),
        ("Salvar no cérebro", "skills/salvar-no-cerebro/SKILL.md", "guarda qualquer informação no lugar certo"),
        ("Registrar atendimento", "skills/registrar-atendimento/SKILL.md", "atualiza cliente e diário depois de um contato, separando o que foi dito pelo SPIN"),
        ("Preparar reunião com cliente", "skills/preparar-reuniao-cliente/SKILL.md", "monta um briefing SPIN de uma página com o avanço a buscar"),
        ("Escrever follow-up", "skills/escrever-follow-up/SKILL.md", "redige mensagem na voz da empresa"),
        ("Triagem da caixa de entrada", "skills/triagem-inbox/SKILL.md", "organiza o material bruto"),
        ("Modelo de skill", "skills/template-skill/SKILL.md", "modelo para criar uma skill nova"),
    ],
    "Skill é um roteiro em passos que a IA segue quando o pedido do usuário combina com a descrição dela. Para uma ação nova, copie o modelo de skill. Níveis de permissão estão no AGENTS.md.",
    rel=["../AGENTS.md"])

F[A + "conectores.md"] = fm(
    "conector", "Conectores",
    "Fontes e ferramentas externas, como cada uma entra no cérebro hoje e o nível de permissão.",
    rel=["_index.md", "../02-Memoria/_inbox/_index.md"]) + """# Conectores

## Como funciona hoje

Nesta versão tudo entra de forma manual: o usuário cola o texto na conversa e pede "guarde isso no meu cérebro". A IA grava na caixa de entrada e depois organiza. Quando um conector automático for ligado, troque a linha dele para "conectado" e registre o nível de permissão.

## Fontes de informação

- Reuniões gravadas (TL;DV, Meet, Zoom, Teams): cole o resumo ou a transcrição. Entrada manual. Nível 1. Status: manual.
- E-mail (Gmail, Outlook): cole a conversa. Entrada manual. Nível 1. Status: manual.
- WhatsApp: cole a conversa ou o trecho exportado. Entrada manual. Nível 1. Status: manual.
- Conversas com a IA (Claude, ChatGPT): peça "resuma esta conversa para o meu cérebro". Entrada manual. Nível 1. Status: manual.

## Ferramentas de trabalho

- CRM: [A PREENCHER] Nome da ferramenta e como o time usa.
- Agenda: [A PREENCHER]
- Outras ferramentas: [A PREENCHER]

## Regras

- Sem conector ligado, a IA só tem nível 0 e 1. Ela não envia, não agenda e não altera sistemas.
- Antes de ligar um conector, o usuário decide quais dados a IA pode ler e escreve aqui o limite.
- Dado de cliente é sensível. Cole apenas o necessário para o trabalho.
"""

F[A + "automacoes/README.md"] = fm(
    "guia", "Automações",
    "Espaço reservado para rotinas automáticas, como resumo semanal ou alerta de cliente sem contato.",
    status="reservado", fonte="estrutura inicial",
    rel=["../conectores.md"]) + """# Automações

## O que há aqui

Nada por enquanto. Este espaço guarda rotinas automáticas quando existirem.

## Quando usar

Crie uma automação só depois que o usuário repetir a mesma tarefa manualmente algumas vezes. Cada automação ganha um arquivo com o gatilho, os passos, o conector usado e o nível de permissão. Automação que age no mundo (nível 3) sempre pede confirmação.
"""

# ---------------------------------------------------------------- SKILLS
S = A + "skills/"

F[S + "template-skill/SKILL.md"] = skill(
    "template-skill",
    "Modelo. Copie esta pasta para criar uma skill nova. Escreva aqui o que a skill faz e quando usar, com as frases que o usuário costuma dizer. Máximo de 1024 caracteres.",
    """
# Nome da skill

## Quando usar

[A PREENCHER] Situações e frases do usuário que ativam esta skill.

## Antes de começar

[A PREENCHER] Arquivos que a IA deve ler antes, com caminho.

## Passos

[A PREENCHER] Passos numerados, cada um com uma ação só.

## Saída esperada

[A PREENCHER] O que o usuário recebe e onde o resultado é gravado.

## Regras

[A PREENCHER] Permissão necessária (nível 0 a 3) e o que nunca fazer.
""")

F[S + "salvar-no-cerebro/SKILL.md"] = skill(
    "salvar-no-cerebro",
    "Guarda uma informação no lugar certo do Segundo Cérebro. Use quando o usuário disser guarde, anote, salve, registre ou lembre disso, ou colar um texto de reunião, e-mail, WhatsApp ou conversa com IA para guardar.",
    """
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
""")

F[S + "registrar-atendimento/SKILL.md"] = skill(
    "registrar-atendimento",
    "Registra um contato com cliente na ficha dele e no diário, separando o que foi dito pelo método SPIN: situação, problemas, implicações, necessidades explícitas e o resultado do contato (avanço ou continuação). Use quando o usuário disser que falou, atendeu, ligou, reuniu ou trocou mensagens com um cliente ou lead, ou colar o resumo ou a transcrição de uma reunião, e quiser registrar.",
    """
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
8. Atualize a linha da oportunidade em Oportunidades e, no frontmatter, `etapa_funil`, `proximo_contato`, `ultimo_resultado` e `atualizado_em`. Reescreva o `resumo` se a situação mudou. Em Próximo passo, escreva o avanço a buscar no próximo contato.
9. Se apareceu uma objeção nova ou uma lição concreta, proponha criar uma nota em `aprendizados/`, com o campo `cliente` preenchido, já com "O que aprendemos" e "Como aplicar da próxima vez" preenchidos. Se uma pergunta funcionou bem, proponha acrescentá-la ao Banco de perguntas do `08-metodo-spin.md`. Se houve uma decisão, proponha uma nota em `decisoes/`. Só crie depois de o usuário confirmar.
10. Acrescente uma linha na nota de diário do dia e inclua o cliente no campo `clientes`. Se a nota não existir, crie copiando `_template-diario.md` com o nome AAAA-MM-DD.md.
11. Pergunte, no máximo, a etapa do funil, a data do próximo contato e o resultado, se o usuário não disse. Responda em até quatro linhas com o que foi atualizado e um alerta SPIN quando couber, como "ainda não há necessidade explícita registrada" ou "segunda continuação seguida".

## Saída esperada

Ficha do cliente atualizada nas seções SPIN, Histórico com o resultado do contato, diário do dia atualizado e, se couber, uma proposta de aprendizado, decisão ou pergunta nova.

## Regras

Nível 1. Registre só o que o usuário contou. Não preencha motivos ou intenções do cliente por suposição. Nunca marque como [fato] o que o cliente não disse, e nunca transforme queixa vaga em necessidade explícita. Nunca grave na ficha de um cliente sem ter certeza de que é ele.
""")

F[S + "preparar-reuniao-cliente/SKILL.md"] = skill(
    "preparar-reuniao-cliente",
    "Monta um briefing SPIN de uma página antes de uma reunião ou ligação com cliente: o que já sabemos, as lacunas, perguntas de Situação, Problema, Implicação e Necessidade de solução, objeções prováveis e o avanço a buscar. Use quando o usuário pedir para preparar, se preparar, montar as perguntas ou revisar o que sabemos antes de falar com um cliente ou lead.",
    """
# Preparar reunião com cliente

## Quando usar

O usuário tem uma reunião, ligação ou visita com um cliente e quer chegar preparado.

## Antes de começar

Leia `01-Contexto/08-metodo-spin.md` e a ficha em `02-Memoria/clientes/`, identificada pela regra 8 de "Como escrever" do `AGENTS.md`. Se houver mais de uma oportunidade aberta, pergunte de qual a reunião trata. Leia `01-Contexto/02-icp.md`, `01-Contexto/03-tom-de-voz.md`, `02-Memoria/prioridades/atual.md`, a ficha do produto em `01-Contexto/06-produtos/`, as decisões de `02-Memoria/decisoes/` que se apliquem ao produto ou ao cliente e as notas de `02-Memoria/_inbox/`, `02-Memoria/aprendizados/` e `02-Memoria/decisoes/` cujo campo `cliente` seja esta ficha, além das que citem o produto. Se `03-Acao/conectores.md` tiver um CRM conectado, consulte o histórico do cliente nele, só para leitura.

## Passos

1. Confirme com o usuário quem é o cliente, a data e o objetivo da reunião, se ainda não souber.
2. Se o usuário pedir e a ferramenta permitir busca na internet, pesquise informações públicas da empresa do cliente e cite o endereço de cada fato.
3. Situação: liste o que já sabemos, com o arquivo de origem. Depois liste só as lacunas que importam para a venda. Elas viram no máximo três perguntas de Situação.
4. Problema: junte os problemas [fato] da ficha e as [hipótese] tiradas de "Problemas que resolvemos" e das dores do ICP que combinam com este cliente. Escreva uma ou duas perguntas de Problema para cada um, dando prioridade às hipóteses que precisam ser confirmadas.
5. Implicação: para os dois ou três problemas mais relevantes, monte a cadeia de consequências usando "Cadeias de implicação" e escreva perguntas de Implicação. Se houver número na ficha ou em "Dados de referência", mostre o tamanho do problema com a fonte. Se não houver, marque [estimativa] com a premissa ou não quantifique.
6. Necessidade de solução: escreva perguntas que levem o cliente a dizer o valor de resolver esses problemas.
7. Mostre as necessidades explícitas já registradas. A oferta a apresentar só entra no briefing se houver necessidade explícita, ligando cada necessidade a um benefício do produto. Se não houver, diga que o foco da reunião é descoberta.
8. Liste as objeções prováveis com resposta. Destaque as decisões vigentes que limitam o que pode ser oferecido ou prometido, como uma regra para cotar.
9. Defina o avanço pretendido e um avanço mínimo aceitável. Se o último resultado na ficha foi continuação, diga isso e sugira como pedir um compromisso concreto.
10. Ofereça salvar o briefing na nota de diário do dia.

## Saída esperada

Um briefing de até uma página, pronto para ler em dois minutos, nesta ordem: cliente em três linhas, o que já sabemos, lacunas, perguntas de Situação, Problema, Implicação e Necessidade de solução, necessidades explícitas já ditas, oferta (se couber), objeções e avanço pretendido. No total, cerca de doze perguntas, com mais peso em Problema e Implicação.

## Regras

Nível 2. Mostre ao usuário antes de considerar pronto. Não invente dados do cliente. Hipótese nunca aparece como fato. Não sugira pergunta de Situação cuja resposta já está nos arquivos. Se a ficha for do modelo antigo, use a seção Dor e interesse como fonte de problemas.
""")

F[S + "escrever-follow-up/SKILL.md"] = skill(
    "escrever-follow-up",
    "Escreve mensagem ou e-mail de follow-up para um cliente na voz da empresa. Use quando o usuário pedir uma mensagem, um e-mail, um retorno ou um follow-up para um cliente ou lead.",
    """
# Escrever follow-up

## Quando usar

O usuário quer uma mensagem para um cliente depois de uma conversa, proposta ou silêncio.

## Antes de começar

Leia a ficha do cliente em `02-Memoria/clientes/`, `01-Contexto/03-tom-de-voz.md`, `01-Contexto/05-preferencias.md`, as decisões de `02-Memoria/decisoes/` que se apliquem ao que será prometido e, se citar produto ou preço, a ficha em `01-Contexto/06-produtos/`.

## Passos

1. Descubra o canal (e-mail ou WhatsApp) e o objetivo da mensagem, se o usuário não disse. Uma pergunta por vez.
2. Escreva duas versões: uma curta e uma completa. Use o tom de voz, o nome do cliente e o último combinado do histórico.
3. Termine cada versão com um próximo passo claro e uma data ou pergunta objetiva.
4. Para e-mail, inclua uma linha de assunto.
5. Pergunte se o usuário quer ajustar e, se enviar, ofereça registrar o contato com a skill registrar-atendimento.

## Saída esperada

Duas versões prontas para copiar, marcadas como rascunho.

## Regras

Nível 2. Nunca envie a mensagem. Não prometa prazo, preço, cobertura ou desconto que não esteja nos arquivos, e respeite as decisões vigentes e as preferências, mesmo que um exemplo de tom pareça sugerir o contrário. Se faltar o dado, deixe `[A PREENCHER]` na mensagem e avise.
""")

F[S + "triagem-inbox/SKILL.md"] = skill(
    "triagem-inbox",
    "Organiza a caixa de entrada do Segundo Cérebro. Use quando o usuário pedir para organizar, triar, limpar ou processar o que está esperando na caixa de entrada.",
    """
# Triagem da caixa de entrada

## Quando usar

Há itens em `02-Memoria/_inbox/` com `processado: nao` e o usuário quer organizá-los.

## Antes de começar

Leia `02-Memoria/_inbox/_index.md` e abra cada item com `processado: nao`.

## Passos

1. Para cada item, preencha a seção "O que parece importante" com até 5 linhas e sugira um destino: decisão, aprendizado, cliente, projeto, diário ou descarte. Se o item fala de um cliente e o campo `cliente` está vazio, identifique a ficha pela regra 8 de "Como escrever" do `AGENTS.md` e mostre qual ficha você acha que é.
2. Mostre ao usuário uma lista curta: item, resumo em uma linha, destino sugerido.
3. Espere a confirmação do usuário. Ele pode aprovar tudo, ajustar item a item ou pular.
4. Para cada destino confirmado, crie a nota copiando o `_template-*` certo, preencha (inclusive o campo `cliente`), atualize o índice da pasta e ligue a nota ao item em `relacionados`.
5. Marque o item como `processado: sim` e `status: arquivado`. Não apague.
6. Termine dizendo quantos itens foram organizados e quantos ficaram.

## Saída esperada

Notas criadas nos destinos confirmados, itens da caixa marcados como processados e um resumo de duas linhas.

## Regras

Nível 1. Nada vira nota curada sem confirmação. Descarte significa arquivar, nunca apagar.
""")

R = OrderedDict()
R["_restrito/README.md"] = fm(
    "guia", "Área restrita",
    "Pasta para assuntos sensíveis. A IA só abre se o usuário pedir.",
    status="vigente", fonte="estrutura inicial",
    rel=["../AGENTS.md"]) + """# Área restrita

## O que há aqui

Esta pasta é para assuntos sensíveis da {{EMPRESA}}, como negociações confidenciais ou informações estratégicas que não devem aparecer em respostas comuns.

## Quando usar

A IA não abre esta pasta por conta própria. Só abre quando o usuário pedir de forma explícita naquela conversa. Nunca guarde aqui senhas, dados bancários nem documentos pessoais. Se precisar lembrar que algo sensível existe, escreva só o nome do assunto e onde o dado real está guardado.
"""
F.update(R)
