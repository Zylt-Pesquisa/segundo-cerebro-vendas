# Fonte do kit

Os arquivos do template e os três prompts são gerados por estes scripts. Para mudar o kit, edite aqui e gere de novo. Nunca edite a pasta template nem os prompts à mão.

- kit_root.py, kit_memoria.py, kit_acao.py: conteúdo exato de cada arquivo do Segundo Cérebro.
- kit_common.py: funções de frontmatter e índices.
- kit_skill.py: a skill do Claude usar-segundo-cerebro e o guia de instalação dela.
- prompt_texto.py: texto dos prompts. Os prompts para Claude e para ChatGPT saem dentro do README. O PROMPT-COMPLETO sai como arquivo próprio.
- build.py: gera o repositório em out/repo. Variáveis: REPO_URL (endereço do repositório) e TAG (versão).
- validar.py: confere uma pasta contra o padrão. Uso: python3 validar.py PASTA --esperado 43

Gerar e validar: REPO_URL=https://github.com/ORG/REPO TAG=v1.0 python3 build.py e depois python3 validar.py out/referencia --esperado 43

Para publicar uma versão: copie o conteúdo de out/repo para o repositório, faça o commit e crie a tag (por exemplo v1.1). Os prompts apontam para a tag, não para o branch principal, para que ninguém altere o kit de quem já usa. Ao mudar a versão, gere de novo com a TAG nova.
