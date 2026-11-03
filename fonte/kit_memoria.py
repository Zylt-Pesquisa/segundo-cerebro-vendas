# -*- coding: utf-8 -*-
from collections import OrderedDict
from kit_common import fm, indice, PH

F = OrderedDict()
M = "02-Memoria/"

F[M + "_index.md"] = indice(
    "Memória",
    "Camada 2. O que aconteceu e foi decidido na {{EMPRESA}}: decisões, aprendizados, clientes, projetos, diário e caixa de entrada.",
    [
        ("Caixa de entrada", "_inbox/_index.md", "material bruto esperando triagem"),
        ("Decisões", "decisoes/_index.md", "o que foi decidido, por quê e até quando"),
        ("Aprendizados", "aprendizados/_index.md", "o que funcionou ou não, para repetir ou evitar"),
        ("Prioridades", "prioridades/_index.md", "foco atual do time, em um único arquivo vivo"),
        ("Diário", "diario/_index.md", "registro do dia a dia comercial"),
        ("Projetos", "projetos/_index.md", "iniciativas em andamento"),
        ("Clientes", "clientes/_index.md", "uma ficha por cliente, com as oportunidades dentro dela"),
        ("Sucesso", "sucesso/_index.md", "planos de sucesso dos clientes depois da venda"),
        ("Diagnóstico", "diagnostico/_index.md", "reservado para o diagnóstico da empresa"),
    ],
    "Esta camada cresce todo dia. Procure sempre pelo índice da subpasta e pelo campo resumo antes de abrir notas. Material novo entra primeiro em _inbox e só vira nota curada com confirmação do usuário.",
    rel=["../01-Contexto/_index.md"])

# ---------------------------------------------------------------- INBOX
F[M + "_inbox/_index.md"] = indice(
    "Caixa de entrada",
    "Zona de entrada. Material bruto de reuniões, e-mails, WhatsApp e conversas com IA, esperando triagem.",
    [("Modelo de item", "_template-item.md", "modelo para guardar material bruto")],
    "Guarde aqui tudo que chegar sem organização. Cada item tem processado: nao até a triagem. A skill triagem-inbox decide o destino e marca processado: sim.",
    rel=["../../03-Acao/skills/triagem-inbox/SKILL.md"])

F[M + "_inbox/_template-item.md"] = fm(
    "inbox", "Modelo de item da caixa de entrada",
    "Modelo. Copie para guardar material bruto ainda não organizado.",
    status="modelo", fonte="estrutura inicial", rel=["_index.md"],
    extra={"origem": "reuniao | email | whatsapp | sessao-ia | outro",
           "data": "AAAA-MM-DD", "cliente": "nome-da-ficha | vazio", "processado": "nao"}) + """# Assunto do item

## Conteúdo bruto

[A PREENCHER] Cole aqui o texto original, sem editar.

## O que parece importante

[A PREENCHER] A IA preenche na triagem, em até 5 linhas: fatos, decisões, pedidos e prazos.

## Destino sugerido

[A PREENCHER] Para onde vai: decisão, aprendizado, cliente, projeto, diário ou descarte.
"""

# ---------------------------------------------------------------- DECISOES
F[M + "decisoes/_index.md"] = indice(
    "Decisões",
    "Registro das decisões comerciais da {{EMPRESA}} com motivo, alternativas e data de revisão.",
    [("Modelo de decisão", "_template-decisao.md", "modelo para registrar uma decisão")],
    "Consulte antes de sugerir algo que possa contrariar uma decisão anterior. Liste as decisões em ordem da mais recente para a mais antiga, uma linha cada. Decisão substituída permanece na lista com a marca (substituído).",
    rel=["../_index.md"])

F[M + "decisoes/_template-decisao.md"] = fm(
    "decisao", "Modelo de decisão",
    "Modelo. Copie para registrar uma decisão com contexto, alternativas e data de revisão.",
    status="modelo", fonte="estrutura inicial", rel=["_index.md"],
    extra={"data": "AAAA-MM-DD", "decisor": PH, "cliente": "nome-da-ficha | vazio",
           "projeto": "opcional", "revisar_em": "AAAA-MM-DD",
           "substituido_por": "vazio"}) + """# Decisão em uma frase

## Decisão

[A PREENCHER] O que foi decidido, em uma frase afirmativa.

## Contexto

[A PREENCHER] O que estava acontecendo e qual problema a decisão resolve.

## Alternativas consideradas

[A PREENCHER] Outras opções e por que ficaram de fora.

## Por que decidimos assim

[A PREENCHER] Os motivos principais, com dados quando houver.

## Consequências e próximos passos

[A PREENCHER] O que muda a partir de agora, quem faz o quê e até quando.
"""

# ---------------------------------------------------------------- APRENDIZADOS
F[M + "aprendizados/_index.md"] = indice(
    "Aprendizados",
    "Lições comerciais da {{EMPRESA}} sobre objeções, abordagens, produtos e processo.",
    [("Modelo de aprendizado", "_template-aprendizado.md", "modelo para registrar um aprendizado")],
    "Consulte antes de preparar reunião, proposta ou mensagem. Registre um aprendizado quando algo funcionou ou falhou de forma que valha repetir ou evitar. Liste do mais recente para o mais antigo.",
    rel=["../_index.md"])

F[M + "aprendizados/_template-aprendizado.md"] = fm(
    "aprendizado", "Modelo de aprendizado",
    "Modelo. Copie para registrar o que funcionou ou falhou e como aplicar na próxima vez.",
    status="modelo", fonte="estrutura inicial", rel=["_index.md"],
    extra={"data": "AAAA-MM-DD", "origem": "cliente, projeto ou reunião de origem",
           "cliente": "nome-da-ficha | vazio",
           "categoria": "objecao | abordagem | produto | processo | outro"}) + """# Aprendizado em uma frase

## O que aprendemos

[A PREENCHER] A lição, em uma frase afirmativa.

## Em que situação

[A PREENCHER] Onde e quando isso apareceu.

## Evidência

[A PREENCHER] O que aconteceu que comprova. Cite a nota ou a reunião de origem.

## Como aplicar da próxima vez

[A PREENCHER] A ação concreta para repetir ou evitar.
"""

# ---------------------------------------------------------------- PRIORIDADES
F[M + "prioridades/_index.md"] = indice(
    "Prioridades",
    "Aponta para o arquivo vivo com o foco comercial atual da {{EMPRESA}}.",
    [("Prioridades atuais", "atual.md", "foco do período, top 3 prioridades e metas")],
    "Leia antes de sugerir o que fazer primeiro, de priorizar clientes ou de aceitar uma nova iniciativa. Ao mudar o foco, não crie outro arquivo. Reescreva atual.md e registre a mudança como decisão em decisoes/.",
    rel=["../_index.md"])

F[M + "prioridades/atual.md"] = fm(
    "prioridade", "Prioridades atuais",
    "Foco comercial atual da {{EMPRESA}}: top 3 prioridades, o que fica de fora e metas do período.",
    rel=["../../01-Contexto/01-negocio.md", "../projetos/_index.md"],
    extra={"periodo": PH, "revisar_em": "AAAA-MM-DD"}) + """# Prioridades atuais

## Foco do período

[A PREENCHER] Em uma frase, o foco dos próximos 30 a 90 dias.

## Top 3 prioridades

[A PREENCHER] Três prioridades em ordem, cada uma com o resultado esperado.

## O que não vamos fazer agora

[A PREENCHER] O que está fora do foco neste período.

## Metas e números

[A PREENCHER] Metas de receita, volume ou conversão com prazo.
"""

# ---------------------------------------------------------------- DIARIO
F[M + "diario/_index.md"] = indice(
    "Diário",
    "Registro diário do trabalho comercial da {{EMPRESA}}, uma nota por dia.",
    [("Modelo de diário", "_template-diario.md", "modelo para a nota do dia")],
    "Use para lembrar o que aconteceu em um dia ou semana. Uma nota por dia, nome AAAA-MM-DD.md. A skill registrar-atendimento acrescenta atendimentos aqui.",
    rel=["../_index.md"])

F[M + "diario/_template-diario.md"] = fm(
    "diario", "Modelo de diário",
    "Modelo. Copie para a nota do dia com o que aconteceu, o que ficou decidido e as pendências.",
    status="modelo", fonte="estrutura inicial", rel=["_index.md"],
    extra={"data": "AAAA-MM-DD", "clientes": "nomes das fichas citadas, separados por vírgula | vazio"}) + """# Diário AAAA-MM-DD

## O que aconteceu

[A PREENCHER] Atendimentos, reuniões e fatos do dia, um por linha.

## Decisões e aprendizados

[A PREENCHER] Links para as notas de decisão e aprendizado criadas hoje.

## Pendências para o próximo dia

[A PREENCHER] O que ficou aberto, com responsável e data.
"""

# ---------------------------------------------------------------- PROJETOS
F[M + "projetos/_index.md"] = indice(
    "Projetos",
    "Iniciativas comerciais em andamento na {{EMPRESA}}, com objetivo, responsável e próximos passos.",
    [("Modelo de projeto", "_template-projeto.md", "modelo para registrar um projeto")],
    "Use para iniciativas com começo, fim e responsável, como uma campanha, um processo novo ou a entrada em um mercado. Liste só os projetos em andamento no topo e os concluídos abaixo.",
    rel=["../prioridades/atual.md"])

F[M + "projetos/_template-projeto.md"] = fm(
    "projeto", "Modelo de projeto",
    "Modelo. Copie para registrar uma iniciativa com objetivo, situação, responsável e próximos passos.",
    status="modelo", fonte="estrutura inicial", rel=["_index.md"],
    extra={"responsavel": PH, "prazo": "AAAA-MM-DD",
           "andamento": "planejado | em-andamento | pausado | concluido"}) + """# Nome do projeto

## Objetivo

[A PREENCHER] O resultado que o projeto precisa entregar, com medida.

## Situação atual

[A PREENCHER] Onde o projeto está hoje, em três linhas.

## Responsáveis

[A PREENCHER] Quem faz o quê.

## Próximos passos

[A PREENCHER] As próximas ações com data e responsável.

## Riscos e bloqueios

[A PREENCHER] O que pode atrapalhar e o que já está travado.
"""

# ---------------------------------------------------------------- CLIENTES
F[M + "clientes/_index.md"] = indice(
    "Clientes",
    "Fichas de clientes e oportunidades da {{EMPRESA}} com etapa do funil e próximo contato.",
    [("Modelo de cliente", "_template-cliente.md", "modelo para criar a ficha de um cliente")],
    "Abra a ficha antes de qualquer contato com o cliente. Uma ficha por empresa cliente (ou por pessoa, quando o cliente é pessoa física), com as oportunidades dentro dela. Nome do arquivo em minúsculas com hífen. Liste cada cliente com a etapa do funil e os apelidos na descrição, para a IA reconhecer o cliente por outros nomes. As seções Situação, Problemas, Implicações e Necessidades explícitas seguem o método SPIN descrito em 01-Contexto/08-metodo-spin.md.",
    rel=["../../01-Contexto/07-processo-comercial.md", "../../01-Contexto/08-metodo-spin.md"])

F[M + "clientes/_template-cliente.md"] = fm(
    "cliente", "Modelo de cliente",
    "Modelo. Copie para criar a ficha de um cliente (empresa ou pessoa), com suas oportunidades, organizada pelo método SPIN.",
    status="modelo", fonte="estrutura inicial",
    rel=["_index.md", "../../01-Contexto/08-metodo-spin.md"],
    extra={"nome": PH, "apelidos": "outros nomes pelos quais o cliente é chamado, separados por vírgula | vazio",
           "id_crm": "código do cliente no CRM | vazio", "responsavel": PH,
           "etapa_funil": PH, "produto": PH, "proximo_contato": "AAAA-MM-DD",
           "ultimo_resultado": "avanco | continuacao | pedido | sem-venda"}) + """# Nome do cliente

## Quem é

[A PREENCHER] Empresa ou pessoa, setor, porte e como chegou até nós.

## Situação

[A PREENCHER] Fatos já confirmados sobre o cliente: estrutura, processo atual, ferramentas, volumes e momento da compra. Tudo que está aqui não se pergunta de novo.

## Problemas

[A PREENCHER] Um por linha, com a marca [fato] (o cliente disse) ou [hipótese] (suposição nossa), a data e quem falou.

## Implicações

[A PREENCHER] Consequências de cada problema, ligadas a ele. Número só com fonte (quem disse e quando). Conta nossa leva [estimativa] e a premissa.

## Necessidades explícitas

[A PREENCHER] O que o cliente disse que quer resolver ou conseguir, entre aspas e com as palavras dele, com a data. Queixa vaga fica em Problemas.

## Decisores e contatos

[A PREENCHER] Nome, cargo e papel na decisão. Sem dados sensíveis.

## Oportunidades

[A PREENCHER] Uma linha por oportunidade aberta ou encerrada com este cliente: produto, etapa do funil, valor se houver, situação (aberta, ganha ou perdida) e data. Os campos etapa_funil e produto do topo valem para a oportunidade principal.

## Histórico

[A PREENCHER] Contatos em ordem do mais recente para o mais antigo, cada um com data, canal, oportunidade (produto), o que foi dito, objeções, o combinado e o resultado (avanço, continuação, pedido ou sem venda).

## Próximo passo

[A PREENCHER] O avanço pretendido no próximo contato, com data e responsável.
"""

F[M + "sucesso/_index.md"] = """---
tipo: indice
titulo: Sucesso
resumo: Planos de sucesso dos clientes da {{EMPRESA}} depois da venda: metas, marcos, saúde e próximos contatos.
status: vigente
atualizado_em: {{DATA}}
fonte: estrutura inicial
relacionados: [../../01-Contexto/12-sucesso-do-cliente.md, ../clientes/_index.md]
---

# Sucesso

## O que há aqui

- [Modelo de plano de sucesso](_template-plano-sucesso.md) — modelo para criar o plano de sucesso de um cliente

## Quando usar

Abra o plano antes de qualquer contato de pós-venda. Um plano por cliente, com o mesmo nome de arquivo da ficha em clientes. Na descrição de cada linha, escreva a saúde atual (verde, amarelo ou vermelho).
"""

F[M + "sucesso/_template-plano-sucesso.md"] = """---
tipo: cliente
titulo: Modelo de plano de sucesso
resumo: Modelo. Copie para criar o plano de sucesso de um cliente depois da venda.
status: modelo
atualizado_em: {{DATA}}
fonte: estrutura inicial
relacionados: [_index.md, ../../01-Contexto/12-sucesso-do-cliente.md]
nome: A PREENCHER
cliente: nome-da-ficha
responsavel: A PREENCHER
segmento: A PREENCHER
inicio: AAAA-MM-DD
primeiro_valor_previsto: AAAA-MM-DD
primeiro_valor_real: AAAA-MM-DD
saude: verde | amarelo | vermelho
proxima_revisao: AAAA-MM-DD
proximo_contato: AAAA-MM-DD
---

# Plano de sucesso — nome do cliente

## Resultado desejado

[A PREENCHER] Resultado necessário: o que o cliente precisa alcançar, com as palavras dele (necessidades explícitas da venda) e a data. Experiência apropriada: como ele espera chegar lá (prazo, acompanhamento, esforço).

## Encaixe no perfil

[A PREENCHER] Se o cliente está dentro do ICP e, se não estiver, em que ponto foge e o risco que isso traz.

## Metas combinadas

[A PREENCHER] Uma por linha: meta — como medir — linha de base — prazo.

## Primeiro valor

[A PREENCHER] Qual é o primeiro resultado que o cliente vai perceber, a data prevista e a data em que aconteceu.

## Promessas da venda

[A PREENCHER] O que o vendedor prometeu (prazos, entregas, condições). Promessa não cumprida é risco.

## Patrocinador e contatos

[A PREENCHER] Quem defende o projeto no cliente, quem usa e quem decide a renovação. Ter mais de um contato reduz o risco. Sem dados sensíveis.

## Marcos

[A PREENCHER] Marco — data prevista — data real — situação.

## Saúde

[A PREENCHER] Avaliação mais recente com data, os critérios de 12-sucesso-do-cliente.md, os sinais observados e o motivo da cor.

## Valor entregue

[A PREENCHER] Resultados medidos, com número, data e fonte. Alimenta a revisão de valor e o banco de provas.

## Histórico de presença

[A PREENCHER] Contatos em ordem do mais recente para o mais antigo: data, canal, o que foi feito e o valor entregue no contato.

## Oportunidades

[A PREENCHER] Expansões, indicações e depoimentos possíveis, com o momento certo de pedir.
"""

# ---------------------------------------------------------------- DIAGNOSTICO (reservado)
F[M + "diagnostico/_index.md"] = fm(
    "indice", "Diagnóstico",
    "Espaço reservado para o diagnóstico da empresa. Ainda não use.",
    status="reservado", fonte="estrutura inicial",
    rel=["../_index.md"]) + """# Diagnóstico

## O que há aqui

Nada por enquanto. Este espaço está reservado para guardar o diagnóstico da {{EMPRESA}} quando ele for realizado.

## Quando usar

Só quando o usuário trouxer o resultado do diagnóstico e pedir para guardar. Até lá, não crie arquivos aqui e não use esta pasta como fonte.
"""
