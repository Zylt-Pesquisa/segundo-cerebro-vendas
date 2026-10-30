# -*- coding: utf-8 -*-
"""Textos dos três prompts.
PROMPT-CLAUDE e PROMPT-GPT vão dentro do README; PROMPT-COMPLETO é arquivo próprio.
Variáveis: @@N@@ arquivos, @@PASTAS@@ pastas, @@ZIP@@ link do zip, @@TAG@@ versão."""

AVISO_IA = "======== A PARTIR DAQUI É A INSTRUÇÃO PARA A IA ========\n"

# ------------------------------------------------------------------ blocos comuns
PAPEL = """
# Instrução para a IA

## Seu papel

Você vai construir, no computador desta pessoa, o Segundo Cérebro da empresa dela. É uma pasta de arquivos Markdown que guarda o contexto, a memória e as ferramentas da operação comercial, e que você mesmo vai ler nas próximas conversas para ajudá-la. A pessoa trabalha no comercial e não é técnica. Fale português do Brasil, com frases curtas e sem jargão. A pasta pertence à pessoa e à empresa dela.

## Regras de ouro

1. Os arquivos do kit são copiados como estão. Troque apenas {{EMPRESA}} e {{DATA}}. Não resuma, não reordene, não melhore, não pule nenhum arquivo.
2. Nunca invente informação sobre a empresa. Grave só o que a pessoa disse. O que você não souber fica como [A PREENCHER] seguido da pergunta que falta.
3. Faça no máximo 4 perguntas por mensagem e espere a resposta.
4. Não peça senhas, dados bancários nem documentos pessoais. Se a pessoa oferecer, peça que não envie.
5. Nunca sobrescreva arquivos que já existiam na pasta antes deste prompt. Se a pasta não estiver vazia, pare, avise e proponha criar uma subpasta nova. Os arquivos que você mesmo criou aqui podem ser preenchidos e atualizados na entrevista.
"""

PREPARAR = """
## Passo 1 — Preparar

Pergunte o nome da empresa (vira {{EMPRESA}}). A data de hoje (vira {{DATA}}) você usa da sua própria informação; só pergunte se não tiver acesso a ela. Escreva a data sempre no formato AAAA-MM-DD, convertendo se a pessoa responder de outro jeito.
"""

CONFERIR = """
## Passo 3 — Conferir antes de dizer que terminou

Confira cada item e corrija o que falhar:

- Existem @@N@@ arquivos (os do kit, mais os de produtos criados na entrevista) e cada um está no caminho certo.
- Nenhum arquivo ficou com {{EMPRESA}} ou {{DATA}} sem troca.
- Todo arquivo .md começa com o bloco entre linhas --- (frontmatter) e tem status, fonte e atualizado_em preenchidos.
- Cada resumo tem no máximo 200 caracteres e descreve o conteúdo real do arquivo.
- Cada pasta dentro de 01-Contexto e de 02-Memoria, e a pasta 03-Acao, tem um _index.md. Cada arquivo de 01-Contexto e de 02-Memoria aparece no _index.md da sua pasta. As skills e a pasta automacoes aparecem em 03-Acao/_index.md.
- Todo link entre arquivos, inclusive os do campo relacionados, aponta para um arquivo que existe.
- Os arquivos SKILL.md têm name igual ao nome da pasta onde estão.
- Se houver Python disponível e a pasta ferramentas do kit baixado tiver o arquivo validar.py, rode: python3 validar.py PASTA --esperado @@N@@ (o número sobe quando há produtos novos).

Faça esta conferência duas vezes: logo depois de criar a estrutura e de novo ao fim da entrevista, antes do fechamento. Na primeira, diga à pessoa, em até 4 linhas: quantos arquivos criou, onde estão e quais são as três camadas (Contexto, Memória, Ação) em uma frase cada, sem listar os arquivos, e comece a entrevista. Na segunda, não faça mensagem própria: corrija o que falhar e siga para o fechamento.
"""

ENTREVISTA_REF = """
## Passo 4 — Entrevista guiada e fechamento

Abra o arquivo ENTREVISTA.md do kit e siga-o do começo ao fim. Ele traz as regras, os 10 blocos de perguntas e o fechamento.
"""

# ------------------------------------------------------------------ PROMPT-CLAUDE
CLAUDE_USO = """1. Instale o Google Drive para computador (ou use o OneDrive da empresa). É o que faz o backup do seu cérebro.
2. Dentro da pasta do Drive (Meu Drive), crie uma pasta vazia chamada Segundo Cerebro.
3. Abra o Claude Desktop, entre no Cowork e adicione essa pasta à conversa. O Claude Code também funciona, mas é feito para quem programa.
4. Copie o prompt abaixo (botão de copiar no canto direito do quadro) e cole na conversa.
5. Responda às perguntas. A conversa leva de 40 a 60 minutos e você pode parar e continuar depois.
"""

CLAUDE_P2 = """
## Passo 2 — Baixar o kit e criar a estrutura

A pasta de destino é a que a pessoa selecionou. Se nenhuma pasta estiver selecionada, peça que ela crie uma pasta vazia dentro da pasta do Google Drive (Meu Drive) ou do OneDrive, sugerindo o nome "Segundo Cerebro", e a adicione à conversa. Se o caminho da pasta escolhida não indicar Google Drive, Meu Drive, My Drive ou OneDrive, avise em uma frase que, fora dessas pastas, o cérebro fica sem backup, e pergunte se ela quer seguir assim ou trocar de pasta. Não peça nenhuma instalação técnica: Python, Git e terminal não são necessários.

1. Baixe o kit (versão @@TAG@@) deste endereço, para uma pasta de trabalho temporária FORA da pasta da pessoa, e descompacte: @@ZIP@@
2. O kit descompactado tem uma pasta única com as pastas template e ferramentas, mais arquivos de apoio (README e PROMPT-COMPLETO) que você ignora. Copie o conteúdo da pasta template (não a pasta template em si) para a pasta de destino, mantendo os mesmos caminhos. São @@N@@ arquivos em @@PASTAS@@ pastas além da raiz.
3. Dentro dos arquivos copiados, troque {{EMPRESA}} pelo nome da empresa e {{DATA}} pela data de hoje. Mais nada muda.
4. Se não conseguir baixar (sem internet, endereço bloqueado), peça que a pessoa abra o endereço no navegador, baixe o arquivo ZIP e o coloque na pasta de destino, e tente de novo com o arquivo local. O ZIP colocado pela pessoa não conta como arquivo existente na pasta. Se ainda assim não for possível, diga que ela deve usar o arquivo PROMPT-COMPLETO.md do mesmo kit e pare.
5. Não recrie arquivos do kit: copie os originais.
6. Quando terminar o Passo 3, apague a pasta temporária do kit e qualquer ZIP do kit que esteja na pasta de destino. Se não conseguir apagar, diga à pessoa quais arquivos ela deve apagar.
"""

# ------------------------------------------------------------------ PROMPT-GPT
GPT_USO = """1. Baixe o kit neste endereço (ele baixa um arquivo ZIP): @@ZIP@@
2. Abra uma conversa nova no ChatGPT, de preferência uma que tenha análise de dados ou execução de código ligada, e anexe o ZIP.
3. Copie o prompt abaixo (botão de copiar no canto direito do quadro) e cole na conversa.
4. Responda às perguntas. A conversa leva de 40 a 60 minutos.
5. No final você recebe um arquivo ZIP com a sua pasta pronta. Baixe e descompacte em uma pasta do seu computador, de preferência dentro do Google Drive ou do OneDrive. Essa é a pasta do seu Segundo Cérebro.

Se o ChatGPT não conseguir abrir o ZIP, ele vai pedir que você descompacte o kit no computador e anexe alguns arquivos. Siga o que ele pedir.
"""

GPT_P2 = """
## Passo 2 — Abrir o kit e preparar a estrutura

Escolha o caminho, sem pedir detalhes técnicos à pessoa:

- Caminho B (você tem ferramenta de código): descompacte o ZIP anexo. Ele tem uma pasta única com as pastas template e ferramentas, mais arquivos de apoio (README e PROMPT-COMPLETO) que você ignora. Copie o conteúdo da pasta template (não a pasta template em si) para uma pasta de trabalho chamada Segundo-Cerebro- seguido do nome da empresa sem acentos, sem espaços e com hífen, mantendo os mesmos caminhos. São @@N@@ arquivos em @@PASTAS@@ pastas além da raiz. Troque {{EMPRESA}} e {{DATA}} dentro dos arquivos. Na entrevista, grave as respostas direto nesses arquivos e, assim que ela terminar, compacte a pasta em um ZIP com o mesmo nome e entregue o link para download. Se a pessoa parar no meio, entregue na hora o ZIP com o que existe. Se o link falhar, o ambiente reiniciar ou o arquivo sumir, refaça o ZIP e entregue de novo; se continuar falhando, passe para o Caminho C.
- Caminho C (você não consegue abrir o ZIP nem executar código): diga em duas linhas o que a pessoa deve fazer: descompactar o ZIP no computador e anexar nesta conversa os arquivos AGENTS.md e ENTREVISTA.md, os arquivos da pasta 01-Contexto (incluindo o modelo da subpasta 06-produtos), 02-Memoria/prioridades/atual.md e 03-Acao/conectores.md. Quando receber, faça a entrevista e entregue só os arquivos que você preencheu, em lotes de no máximo 8 mil caracteres, numerados ("Lote 2 de 4"), cada arquivo com o caminho completo como título e o conteúdo em um bloco de código. Peça que a pessoa salve cada um por cima do arquivo de mesmo nome na pasta do kit. Ensine em poucas linhas: no Windows, Bloco de Notas, Arquivo, Salvar como, Tipo "Todos os arquivos", nome com extensão .md e codificação UTF-8; no Mac, TextEdit, Formato, Converter para texto simples. Os arquivos que você não alterou continuam como vieram no kit e ainda têm {{EMPRESA}} e {{DATA}}, o que não atrapalha: o AGENTS.md ensina a IA a lidar com isso.

Diga em uma frase qual caminho vai usar e siga.
"""

# ------------------------------------------------------------------ PROMPT-COMPLETO
COMPLETO_CAB = """# Prompt de criação do Segundo Cérebro comercial (versão completa, sem baixar nada)

Este arquivo cria, no seu computador, o Segundo Cérebro da sua empresa: uma pasta organizada que a IA lê antes de te ajudar a vender. A pasta é sua. Ninguém mais recebe cópia. Esta versão traz todos os arquivos dentro dela e não precisa baixar nada. Use quando a versão curta do seu Claude ou ChatGPT não funcionar.

## Como usar

1. Abra o Claude (Cowork ou Claude Code) ou o ChatGPT.
2. Se a ferramenta permitir, selecione uma pasta vazia do seu computador para a IA trabalhar. Se não permitir, siga assim mesmo.
3. Cole este arquivo inteiro na conversa. Se preferir, anexe o arquivo e escreva: "Execute o prompt anexo".
4. Responda às perguntas. A conversa leva de 40 a 60 minutos e você pode parar e continuar depois.

"""

COMPLETO_REGRAS_EXTRA = """6. Não mostre o conteúdo dos arquivos na conversa, exceto no Caminho C, em que a entrega é feita na própria conversa. Diga só o que importa para a pessoa.
7. Leia o ANEXO inteiro antes de começar. Ele é longo. Se a leitura vier cortada, continue lendo até a linha final "FIM DO ANEXO". Nunca crie arquivos a partir de um ANEXO lido pela metade.
"""

COMPLETO_P1B = """
Depois escolha como vai entregar os arquivos, na ordem abaixo, sem pedir detalhes técnicos à pessoa:

- Caminho A — Você consegue criar arquivos em uma pasta do computador da pessoa (Claude Cowork com pasta conectada, Claude Code ou ferramenta parecida). Se ela já selecionou uma pasta, crie tudo direto nela. Se não, peça que selecione ou crie uma pasta vazia, sugerindo o nome "Segundo Cérebro - {{EMPRESA}}".
- Caminho B — Você não acessa pasta, mas consegue gerar arquivos para download (por exemplo, ChatGPT com análise de dados). Crie todos os arquivos, compacte em um único arquivo chamado Segundo-Cerebro- seguido do nome da empresa sem acentos, sem espaços e com hífen, e entregue o link. Peça que ela descompacte em uma pasta do computador. Se o link não funcionar ou expirar, passe para o Caminho C.
- Caminho C — Você só consegue escrever na conversa. Entregue os arquivos em lotes de no máximo cerca de 8 mil caracteres, numerados ("Lote 3 de 7"). Cada arquivo aparece com o caminho completo como título e o conteúdo em um bloco de código. Ao fim de cada lote, peça: "Salve esses arquivos e diga próximo". Se a pessoa pedir "lote N" ou "refazer", reenvie só esse lote. Ensine a salvar em poucas linhas. No Windows: criar a pasta e as subpastas, abrir o Bloco de Notas, colar, usar Arquivo, Salvar como, escolher "Todos os arquivos" em Tipo, digitar o nome com a extensão .md e a codificação UTF-8. No Mac: criar as pastas, abrir o TextEdit, usar Formato, Converter para texto simples, colar e salvar com o nome terminado em .md.

Diga em uma frase qual caminho vai usar e siga. No Caminho C, avise antes, com franqueza: são @@N@@ arquivos para salvar à mão, o que leva cerca de 40 minutos de copiar e colar, e indique que o Claude (Cowork ou Code) ou o ChatGPT com análise de dados fazem isso sozinhos. Pergunte se a pessoa quer seguir assim mesmo.
"""

COMPLETO_P2 = """
## Passo 2 — Criar a estrutura

Crie os @@N@@ arquivos do ANEXO, em @@PASTAS@@ pastas além da raiz, com exatamente os mesmos caminhos. Dentro de cada arquivo, troque {{EMPRESA}} pelo nome da empresa e {{DATA}} pela data de hoje. Mais nada muda.

No Caminho B e no Caminho C, não entregue a estrutura em branco. Vá direto para o Passo 4, guarde as respostas na memória da conversa e, no fim da entrevista, volte a este passo e entregue todos os arquivos já preenchidos, em uma única entrega (no Caminho C, dividida em lotes). Se a pessoa parar a entrevista no meio, entregue os arquivos com o que existe até ali.
"""

COMPLETO_ANEXO_FMT = """
## Formato do ANEXO

Cada arquivo começa em uma linha de abertura e termina em uma linha de fechamento. A linha de abertura tem três sinais de menor, a palavra ARQUIVO, dois-pontos, o caminho do arquivo e três sinais de maior. A linha de fechamento tem três sinais de menor, a palavra FIM e três sinais de maior. O conteúdo entre as duas linhas é o arquivo inteiro, desde o primeiro --- do frontmatter até a última linha. As linhas de abertura e fechamento não fazem parte do arquivo. O ANEXO termina na linha "FIM DO ANEXO".

======== ANEXO — OS @@N@@ ARQUIVOS ========
"""


def prompt_claude():
    return PAPEL.lstrip("\n") + PREPARAR + CLAUDE_P2 + CONFERIR + ENTREVISTA_REF


def prompt_gpt():
    return PAPEL.lstrip("\n") + PREPARAR + GPT_P2 + CONFERIR + ENTREVISTA_REF


def prompt_completo():
    papel = PAPEL.rstrip("\n") + "\n" + COMPLETO_REGRAS_EXTRA
    return (COMPLETO_CAB + AVISO_IA + papel + PREPARAR.rstrip("\n") + "\n"
            + COMPLETO_P1B + COMPLETO_P2 + CONFERIR + ENTREVISTA_REF + COMPLETO_ANEXO_FMT)
