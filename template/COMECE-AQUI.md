---
tipo: guia
titulo: Comece aqui
resumo: Guia para a pessoa do comercial usar o Segundo Cérebro no dia a dia, sem conhecimento técnico.
status: vigente
atualizado_em: {{DATA}}
fonte: estrutura inicial
relacionados: [AGENTS.md, PADRAO-DE-ARQUIVOS.md]
---

# Comece aqui — Segundo Cérebro de {{EMPRESA}}

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
