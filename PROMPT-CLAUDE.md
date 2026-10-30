# Prompt de criação do Segundo Cérebro comercial (para Claude)

Este arquivo cria, no seu computador, o Segundo Cérebro da sua empresa: uma pasta organizada que a IA lê antes de te ajudar a vender. A pasta é sua. Ninguém mais recebe cópia.

## Como usar

1. Instale o Google Drive para computador (ou use o OneDrive da empresa). É o que faz o backup do seu cérebro.
2. Dentro da pasta do Drive (Meu Drive), crie uma pasta vazia chamada Segundo Cerebro.
3. Abra o Claude Desktop, entre no Cowork e adicione essa pasta à conversa. O Claude Code também funciona, mas é feito para quem programa.
4. Cole este arquivo inteiro na conversa. Se preferir, anexe o arquivo e escreva: "Execute o prompt anexo".
5. Responda às perguntas. A conversa leva de 40 a 60 minutos e você pode parar e continuar depois.

======== A PARTIR DAQUI É A INSTRUÇÃO PARA A IA ========

# Instrução para a IA

## Seu papel

Você vai construir, no computador desta pessoa, o Segundo Cérebro da empresa dela. É uma pasta de arquivos Markdown que guarda o contexto, a memória e as ferramentas da operação comercial, e que você mesmo vai ler nas próximas conversas para ajudá-la. A pessoa trabalha no comercial e não é técnica. Fale português do Brasil, com frases curtas e sem jargão. A pasta pertence à pessoa e à empresa dela.

## Regras de ouro

1. Os arquivos do kit são copiados como estão. Troque apenas {{EMPRESA}} e {{DATA}}. Não resuma, não reordene, não melhore, não pule nenhum arquivo.
2. Nunca invente informação sobre a empresa. Grave só o que a pessoa disse. O que você não souber fica como [A PREENCHER] seguido da pergunta que falta.
3. Faça no máximo 4 perguntas por mensagem e espere a resposta.
4. Não peça senhas, dados bancários nem documentos pessoais. Se a pessoa oferecer, peça que não envie.
5. Nunca sobrescreva arquivos que já existiam na pasta antes deste prompt. Se a pasta não estiver vazia, pare, avise e proponha criar uma subpasta nova. Os arquivos que você mesmo criou aqui podem ser preenchidos e atualizados na entrevista.

## Passo 1 — Preparar

Pergunte o nome da empresa (vira {{EMPRESA}}). A data de hoje (vira {{DATA}}) você usa da sua própria informação; só pergunte se não tiver acesso a ela. Escreva a data sempre no formato AAAA-MM-DD, convertendo se a pessoa responder de outro jeito.

## Passo 2 — Baixar o kit e criar a estrutura

A pasta de destino é a que a pessoa selecionou. Se nenhuma pasta estiver selecionada, peça que ela crie uma pasta vazia dentro da pasta do Google Drive (Meu Drive) ou do OneDrive, sugerindo o nome "Segundo Cerebro", e a adicione à conversa. Se o caminho da pasta escolhida não indicar Google Drive, Meu Drive, My Drive ou OneDrive, avise em uma frase que, fora dessas pastas, o cérebro fica sem backup, e pergunte se ela quer seguir assim ou trocar de pasta. Não peça nenhuma instalação técnica: Python, Git e terminal não são necessários.

1. Baixe o kit (versão v1.1) deste endereço, para uma pasta de trabalho temporária FORA da pasta da pessoa, e descompacte: https://github.com/Zylt-Pesquisa/segundo-cerebro-vendas/archive/refs/tags/v1.1.zip
2. O kit descompactado tem uma pasta única com as pastas template e ferramentas, mais arquivos de apoio (README e prompts) que você ignora. Copie o conteúdo da pasta template (não a pasta template em si) para a pasta de destino, mantendo os mesmos caminhos. São 43 arquivos em 21 pastas além da raiz.
3. Dentro dos arquivos copiados, troque {{EMPRESA}} pelo nome da empresa e {{DATA}} pela data de hoje. Mais nada muda.
4. Se não conseguir baixar (sem internet, endereço bloqueado), peça que a pessoa abra o endereço no navegador, baixe o arquivo ZIP e o coloque na pasta de destino, e tente de novo com o arquivo local. O ZIP colocado pela pessoa não conta como arquivo existente na pasta. Se ainda assim não for possível, diga que ela deve usar o arquivo PROMPT-COMPLETO.md do mesmo kit e pare.
5. Não recrie arquivos do kit: copie os originais.
6. Quando terminar o Passo 3, apague a pasta temporária do kit e qualquer ZIP do kit que esteja na pasta de destino. Se não conseguir apagar, diga à pessoa quais arquivos ela deve apagar.

## Passo 3 — Conferir antes de dizer que terminou

Confira cada item e corrija o que falhar:

- Existem 43 arquivos (os do kit, mais os de produtos criados na entrevista) e cada um está no caminho certo.
- Nenhum arquivo ficou com {{EMPRESA}} ou {{DATA}} sem troca.
- Todo arquivo .md começa com o bloco entre linhas --- (frontmatter) e tem status, fonte e atualizado_em preenchidos.
- Cada resumo tem no máximo 200 caracteres e descreve o conteúdo real do arquivo.
- Cada pasta dentro de 01-Contexto e de 02-Memoria, e a pasta 03-Acao, tem um _index.md. Cada arquivo de 01-Contexto e de 02-Memoria aparece no _index.md da sua pasta. As skills e a pasta automacoes aparecem em 03-Acao/_index.md.
- Todo link entre arquivos, inclusive os do campo relacionados, aponta para um arquivo que existe.
- Os arquivos SKILL.md têm name igual ao nome da pasta onde estão.
- Se houver Python disponível e a pasta ferramentas do kit baixado tiver o arquivo validar.py, rode: python3 validar.py PASTA --esperado 43 (o número sobe quando há produtos novos).

Faça esta conferência duas vezes: logo depois de criar a estrutura e de novo ao fim da entrevista, antes do fechamento. Na primeira, diga à pessoa, em até 4 linhas: quantos arquivos criou, onde estão e quais são as três camadas (Contexto, Memória, Ação) em uma frase cada, sem listar os arquivos, e comece a entrevista. Na segunda, não faça mensagem própria: corrija o que falhar e siga para o fechamento.

## Passo 4 — Entrevista guiada e fechamento

Abra o arquivo ENTREVISTA.md do kit e siga-o do começo ao fim. Ele traz as regras, os 10 blocos de perguntas e o fechamento.
