---
tipo: guia
titulo: Entrevista guiada
resumo: Roteiro da entrevista que preenche o Contexto da empresa, e o fechamento da criação do cérebro. Também serve para continuar a entrevista depois.
status: vigente
atualizado_em: {{DATA}}
fonte: estrutura inicial
relacionados: [AGENTS.md, PADRAO-DE-ARQUIVOS.md, 01-Contexto/_index.md]
---

# Entrevista guiada

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
6. Tom de voz, arquivo 01-Contexto/03-tom-de-voz.md: como a empresa quer soar, como trata o cliente, palavras que usa e evita. Peça que a pessoa cole uma mensagem ou e-mail real que considera bom, sem nome completo, telefone, e-mail ou outro dado pessoal do cliente. Ao gravar o exemplo, troque o nome do cliente por [Nome].
7. Time, arquivo 01-Contexto/04-time.md: quem é quem no comercial e o que cada um faz, quem aprova desconto e proposta, rotina da semana, áreas de apoio.
8. Preferências, arquivo 01-Contexto/05-preferencias.md: nome e cargo da pessoa, se prefere respostas curtas ou detalhadas, canal mais usado com clientes, o que a IA deve sempre e nunca fazer, ferramentas que usa. Registre também o CRM e as outras ferramentas em 03-Acao/conectores.md, na seção Ferramentas de trabalho, e mude o status desse arquivo para vigente.
9. Prioridades, arquivo 02-Memoria/prioridades/atual.md: foco dos próximos 30 a 90 dias, as três prioridades, o que não vai ser feito agora, metas com prazo. Preencha periodo (por exemplo, "2026-10-26 a 2027-01-24") e defina revisar_em para daqui a 90 dias.

## Fechamento

1. Confirme que todos os _index.md refletem os arquivos que existem, inclusive os produtos novos, e que cada resumo tem no máximo 200 caracteres.
2. Se você não tem acesso à pasta, faça agora a entrega dos arquivos preenchidos, como o prompt de criação indicou, e explique que nas próximas conversas a pessoa deve anexar o AGENTS.md e os arquivos do assunto, e que você devolve os arquivos atualizados para ela salvar.
3. Diga em poucas linhas o que ficou pendente, ou seja, quais arquivos ainda têm [A PREENCHER].
4. Se a pessoa não for instalar a skill usar-segundo-cerebro, entregue este texto, para colar uma única vez nas instruções do projeto da ferramenta que usa (se a ferramenta não tiver projeto, ela cola no início de cada conversa nova): "Você é o Segundo Cérebro comercial da {{EMPRESA}}. Sua memória é a pasta de arquivos deste projeto. Antes de responder qualquer pedido, leia AGENTS.md e siga as regras dele. Se não conseguir ler a pasta, avise e peça os arquivos. Nunca invente informação da empresa. Fale em português do Brasil, simples e direto."
5. Ensine cinco frases de uso: "Guarde isso no meu cérebro", "Acabei de falar com o cliente X, registre", "Prepare minha reunião com o cliente X", "Escreva um follow-up para o cliente X" e "Continuar a entrevista".
6. Se a pessoa usa Claude, avise que existe a skill opcional usar-segundo-cerebro no repositório do kit, na pasta skills, que dispensa colar o texto fixo.
7. Termine com uma frase: o cérebro cresce conforme ela usa, e o arquivo COMECE-AQUI.md da pasta explica o dia a dia.
