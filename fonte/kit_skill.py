# -*- coding: utf-8 -*-
"""Skill do Claude que ativa e ensina a usar o Segundo Cérebro (fica fora do template)."""

NOME = "usar-segundo-cerebro"

SKILL = """---
name: usar-segundo-cerebro
description: Ativa e ensina a usar o Segundo Cérebro comercial do usuário, uma pasta de arquivos Markdown com o contexto da empresa, a memória de clientes e decisões e os roteiros de ação. Use quando o usuário falar em Segundo Cérebro ou meu cérebro, pedir para guardar, anotar ou registrar algo da empresa, contar um atendimento ou reunião com cliente, pedir para preparar uma reunião, escrever follow-up ou mensagem para cliente, organizar a caixa de entrada, continuar a entrevista, consultar prioridades, clientes, decisões, produtos ou objeções da empresa, ou perguntar como usar o cérebro. Use também quando a pasta de trabalho tiver um AGENTS.md que cite o Segundo Cérebro. Não use para pedidos sem relação com vendas ou com a empresa.
---

# Usar o Segundo Cérebro

Esta skill liga a IA ao Segundo Cérebro do usuário e ensina a usá-lo. Ela não tem regras próprias: as regras estão no arquivo AGENTS.md da pasta do cérebro. Se algo aqui contradisser o AGENTS.md, vale o AGENTS.md.

## Quando usar

- O usuário pede algo que depende do contexto da empresa dele: guardar uma informação, registrar um atendimento, preparar reunião, escrever follow-up, consultar cliente ou decisão.
- O usuário pergunta como usar o cérebro ou o que pode pedir.
- O usuário quer continuar a entrevista que preenche o Contexto.
- O usuário consulta o que o cérebro sabe: prioridades, clientes, decisões, produtos, objeções.

Se o pedido claramente não tem a ver com vendas nem com a empresa do usuário (por exemplo, traduzir uma frase ou um assunto pessoal), ignore esta skill.

## Passo 1 — Achar a pasta do cérebro

1. Procure primeiro na pasta de trabalho atual e depois nas pastas conectadas um arquivo AGENTS.md que mencione o Segundo Cérebro e que tenha ao lado as pastas 01-Contexto, 02-Memoria e 03-Acao.
2. Se achar mais de uma, pergunte qual empresa o usuário quer usar.
3. Se não achar nenhuma, diga em uma ou duas frases que não encontrou a pasta do Segundo Cérebro e peça que o usuário selecione ou conecte a pasta e repita o pedido. Se o pedido era para guardar algo, devolva o texto que seria guardado para que ele não se perca. Se o usuário ainda não criou o cérebro, diga que a criação é feita com o arquivo PROMPT-CLAUDE.md do kit do Segundo Cérebro, que está no repositório indicado no material da imersão. Não crie a estrutura de memória por conta própria e não responda como se conhecesse a empresa.

## Passo 2 — Ler e seguir o AGENTS.md

1. Leia o AGENTS.md da pasta e siga as regras dele: ordem de leitura, regras de escrita, níveis de permissão e o roteiro de cada tipo de pedido.
2. Quando o pedido combinar com uma skill listada no AGENTS.md, abra o SKILL.md indicado em 03-Acao/skills e siga os passos dele. Se o pedido tiver mais de um roteiro, faça um de cada vez, na ordem pedida.
3. Para consultas sem roteiro (prioridades, clientes, decisões, produtos), siga a regra "o que sabemos sobre X" do AGENTS.md.
4. Se não conseguir ler o AGENTS.md, ou se a pasta for somente leitura, avise o usuário e não grave nada.

## Passo 3 — Quando o usuário quer aprender a usar

1. Leia o COMECE-AQUI.md da pasta e responda a partir dele, adaptando à pergunta do usuário. Não invente recursos que não estão lá.
2. Em geral, explique em poucas linhas: as três camadas (Contexto, Memória, Ação), as frases que funcionam e os cuidados com dados sensíveis.
3. Sugira um próximo passo concreto ligado ao momento do usuário. Exemplo: se algum arquivo de 01-Contexto está com status rascunho, sugira "Continuar a entrevista". Se há itens com processado: nao em 02-Memoria/_inbox, sugira "Organize minha caixa de entrada".

## Regras

- Não repita nem reescreva as regras do AGENTS.md. Leia-o a cada nova conversa.
- Não abra a pasta _restrito, a menos que o usuário peça de forma explícita.
"""

LEIA_ME = """# Skill usar-segundo-cerebro

Faz o Claude reconhecer e usar o Segundo Cérebro sem precisar colar texto nas instruções do projeto. Só funciona no Claude.

## Como instalar

1. Baixe o arquivo usar-segundo-cerebro.zip deste repositório.
2. No Claude, abra Customize e depois Skills (claude.ai/customize/skills).
3. Clique em "+", escolha "Create skill" e depois "Upload a skill".
4. Envie o ZIP e deixe a skill ligada.

Requisito: a execução de código e criação de arquivos precisa estar ligada na sua conta (em Configurações, Capacidades). Em contas de empresa, o administrador pode precisar liberar skills.

## Como saber que funcionou

Abra uma conversa com a pasta do Segundo Cérebro conectada e escreva: "Como eu uso o meu Segundo Cérebro?". O Claude deve responder com base no COMECE-AQUI.md da sua pasta.
"""
