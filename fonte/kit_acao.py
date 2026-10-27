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
        ("Registrar atendimento", "skills/registrar-atendimento/SKILL.md", "atualiza cliente e diário depois de um contato"),
        ("Preparar reunião com cliente", "skills/preparar-reuniao-cliente/SKILL.md", "monta um briefing de uma página"),
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
4. Preencha o que souber. O que faltar fica como `[A PREENCHER]` com a pergunta. Escreva um `resumo` real de até 200 caracteres e converta datas relativas em AAAA-MM-DD.
5. Adicione a linha do arquivo novo no `_index.md` da pasta.
6. Responda em até duas linhas: o que foi salvo, em qual arquivo, e uma pergunta só se faltar algo importante.

## Saída esperada

Um arquivo novo com frontmatter completo, índice atualizado e confirmação curta ao usuário.

## Regras

Nível 1. Não invente fatos. Não grave senha, dado bancário ou documento pessoal. Se o conteúdo for sensível, pergunte antes e use `_restrito/` apenas com o nome do assunto.
""")

F[S + "registrar-atendimento/SKILL.md"] = skill(
    "registrar-atendimento",
    "Registra um contato com cliente na ficha dele e no diário. Use quando o usuário disser que falou, atendeu, ligou, reuniu ou trocou mensagens com um cliente ou lead, e quiser registrar.",
    """
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
""")

F[S + "preparar-reuniao-cliente/SKILL.md"] = skill(
    "preparar-reuniao-cliente",
    "Monta um briefing de uma página antes de uma reunião ou ligação com cliente. Use quando o usuário pedir para preparar, se preparar ou revisar o que sabemos antes de falar com um cliente ou lead.",
    """
# Preparar reunião com cliente

## Quando usar

O usuário tem uma reunião, ligação ou visita com um cliente e quer chegar preparado.

## Antes de começar

Leia a ficha em `02-Memoria/clientes/`. Leia `01-Contexto/02-icp.md`, `01-Contexto/03-tom-de-voz.md`, `02-Memoria/prioridades/atual.md`, a ficha do produto em `01-Contexto/06-produtos/`, as decisões de `02-Memoria/decisoes/` que se apliquem ao produto ou ao cliente e os itens recentes de `02-Memoria/_inbox/` e `02-Memoria/aprendizados/` que citem o cliente ou o produto.

## Passos

1. Confirme com o usuário quem é o cliente, a data e o objetivo da reunião, se ainda não souber.
2. Monte o briefing com estas partes: quem é o cliente, histórico em três linhas, objetivo da reunião, cinco perguntas de descoberta, objeções prováveis com resposta, produto ou oferta a apresentar e próximo passo sugerido.
3. Cite o arquivo de onde veio cada fato. Se uma decisão vigente limita o que pode ser oferecido ou prometido (por exemplo, uma regra para cotar), destaque no briefing. Se faltar informação, diga o que falta em vez de supor.
4. Ofereça salvar o briefing na nota de diário do dia.

## Saída esperada

Um briefing de até uma página, em passos curtos, pronto para ler em dois minutos.

## Regras

Nível 2. Mostre ao usuário antes de considerar pronto. Não invente dados do cliente.
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
