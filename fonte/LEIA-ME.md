# Fonte do kit

Os arquivos do template e os três prompts são gerados por estes scripts. Para mudar o kit, edite aqui e gere de novo. Nunca edite a pasta template nem os prompts à mão.

- kit_root.py, kit_memoria.py, kit_acao.py: conteúdo exato de cada arquivo do Segundo Cérebro.
- kit_common.py: funções de frontmatter e índices.
- kit_skill.py: a skill do Claude usar-segundo-cerebro e o guia de instalação dela.
- prompt_texto.py: texto dos prompts. Os prompts para Claude e para ChatGPT saem dentro do README. O PROMPT-COMPLETO sai como arquivo próprio.
- build.py: gera o repositório em out/repo. Variável opcional: REPO_URL (endereço do repositório; o padrão é o do projeto).
- validar.py: confere uma pasta contra o padrão. Uso: python3 validar.py PASTA --esperado 44

Gerar e validar: python3 build.py e depois python3 validar.py out/referencia --esperado 44

Para publicar: copie o conteúdo de out/repo para o repositório, faça o commit e o push no branch main. Os prompts baixam sempre o branch main, então quem instalar depois do push já recebe o kit atualizado. Quem já criou o cérebro não é afetado, porque a pasta dele é uma cópia.
