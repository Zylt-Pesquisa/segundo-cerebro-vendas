# -*- coding: utf-8 -*-
"""Gera o repositório do kit: template/, três prompts, ferramentas/ e fonte/.
Uso: REPO_URL=https://github.com/ORG/REPO TAG=v1.0 python3 build.py
"""
import os, sys, shutil, zipfile
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit_root, kit_memoria, kit_acao
import prompt_texto as T
import kit_skill

REPO_URL = os.environ.get("REPO_URL", "https://github.com/ORG/segundo-cerebro").rstrip("/")
TAG = os.environ.get("TAG", "v1.0")
ZIP_URL = os.environ.get("ZIP_URL", REPO_URL + "/archive/refs/tags/" + TAG + ".zip")
OUT = os.path.join(HERE, "out")
REPO = os.path.join(OUT, "repo")

FILES = OrderedDict()
for mod in (kit_root, kit_memoria, kit_acao):
    FILES.update(mod.F)

ORDEM_RAIZ = ["COMECE-AQUI.md", "AGENTS.md", "CLAUDE.md", "PADRAO-DE-ARQUIVOS.md", "ENTREVISTA.md", "_index.md"]
TOPO = {"01-Contexto": 1, "02-Memoria": 2, "03-Acao": 3, "_restrito": 4}


def chave(p):
    return (TOPO.get(p.split("/")[0], 0), p)


resto = sorted([p for p in FILES if p not in ORDEM_RAIZ], key=chave)
paths = [p for p in ORDEM_RAIZ if p in FILES] + resto
assert set(paths) == set(FILES), "arquivo fora da ordem"

n = len(paths)
todas = set()
for p in paths:
    d = os.path.dirname(p)
    while d:
        todas.add(d)
        d = os.path.dirname(d)
pastas_n = len(todas)


def fill(txt):
    return (txt.replace("@@N@@", str(n)).replace("@@PASTAS@@", str(pastas_n))
            .replace("@@ZIP@@", ZIP_URL).replace("@@TAG@@", TAG))


def write(path, txt):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(txt)


if os.path.exists(OUT):
    shutil.rmtree(OUT)

# ---- template (com marcadores)
for p in paths:
    write(os.path.join(REPO, "template", *p.split("/")), FILES[p].rstrip("\n") + "\n")

# ---- prompts
write(os.path.join(REPO, "PROMPT-CLAUDE.md"), fill(T.prompt_claude()))
write(os.path.join(REPO, "PROMPT-GPT.md"), fill(T.prompt_gpt()))
anexo = ""
for p in paths:
    anexo += "<<<ARQUIVO: " + p + ">>>\n" + FILES[p].rstrip("\n") + "\n<<<FIM>>>\n\n"
write(os.path.join(REPO, "PROMPT-COMPLETO.md"), fill(T.prompt_completo()) + "\n" + anexo + "======== FIM DO ANEXO ========\n")

# ---- skill do Claude (fora do template)
write(os.path.join(REPO, "skills", kit_skill.NOME, "SKILL.md"), kit_skill.SKILL)
write(os.path.join(REPO, "skills", "LEIA-ME.md"), kit_skill.LEIA_ME)
_sz = os.path.join(OUT, kit_skill.NOME + ".zip")
with zipfile.ZipFile(_sz, "w", zipfile.ZIP_DEFLATED) as _z:
    _z.write(os.path.join(REPO, "skills", kit_skill.NOME, "SKILL.md"), kit_skill.NOME + "/SKILL.md")
shutil.copy(_sz, os.path.join(REPO, "skills", kit_skill.NOME + ".zip"))

# ---- ferramentas e fonte
os.makedirs(os.path.join(REPO, "ferramentas"), exist_ok=True)
shutil.copy(os.path.join(HERE, "validar.py"), os.path.join(REPO, "ferramentas", "validar.py"))
os.makedirs(os.path.join(REPO, "fonte"), exist_ok=True)
for f in ("kit_common.py", "kit_root.py", "kit_memoria.py", "kit_acao.py", "kit_skill.py", "prompt_texto.py", "build.py", "validar.py"):
    shutil.copy(os.path.join(HERE, f), os.path.join(REPO, "fonte", f))
write(os.path.join(REPO, "fonte", "LEIA-ME.md"), """# Fonte do kit

Os arquivos do template e os três prompts são gerados por estes scripts. Para mudar o kit, edite aqui e gere de novo. Nunca edite a pasta template nem os prompts à mão.

- kit_root.py, kit_memoria.py, kit_acao.py: conteúdo exato de cada arquivo do Segundo Cérebro.
- kit_common.py: funções de frontmatter e índices.
- kit_skill.py: a skill do Claude usar-segundo-cerebro e o guia de instalação dela.
- prompt_texto.py: texto dos prompts (PROMPT-CLAUDE, PROMPT-GPT e PROMPT-COMPLETO).
- build.py: gera o repositório em out/repo. Variáveis: REPO_URL (endereço do repositório) e TAG (versão).
- validar.py: confere uma pasta contra o padrão. Uso: python3 validar.py PASTA --esperado """ + str(n) + """

Gerar e validar: REPO_URL=https://github.com/ORG/REPO TAG=v1.0 python3 build.py e depois python3 validar.py out/referencia --esperado """ + str(n) + """

Para publicar uma versão: copie o conteúdo de out/repo para o repositório, faça o commit e crie a tag (por exemplo v1.1). Os prompts apontam para a tag, não para o branch principal, para que ninguém altere o kit de quem já usa. Ao mudar a versão, gere de novo com a TAG nova.
""")

write(os.path.join(REPO, "README.md"), """# Segundo Cérebro comercial

Um kit para criar, no seu computador, o Segundo Cérebro da sua empresa: uma pasta de arquivos organizados que o Claude ou o ChatGPT lê antes de te ajudar a vender. A pasta é sua e da sua empresa. Este repositório só distribui o modelo vazio. Nenhum dado seu vem para cá.

Versão atual: """ + TAG + """

## Como criar o seu

- **Você usa Claude (Cowork ou Claude Code):** abra o arquivo PROMPT-CLAUDE.md, selecione uma pasta vazia no Claude, cole o conteúdo na conversa e responda às perguntas.
- **Você usa ChatGPT:** baixe o kit em """ + ZIP_URL + """ , anexe o ZIP em uma conversa nova, cole o conteúdo do arquivo PROMPT-GPT.md e responda às perguntas. No fim você baixa a sua pasta pronta.
- **Nenhum dos dois funcionou, ou sem internet:** use o PROMPT-COMPLETO.md. Ele traz todos os arquivos dentro dele.

## O que tem aqui

- template: os """ + str(n) + """ arquivos do Segundo Cérebro, com marcadores {{EMPRESA}} e {{DATA}} que a IA troca.
- PROMPT-CLAUDE.md, PROMPT-GPT.md, PROMPT-COMPLETO.md: os prompts de criação.
- skills: a skill usar-segundo-cerebro para Claude (ZIP pronto e guia de instalação). Opcional.
- ferramentas: script que confere se uma pasta segue o padrão.
- fonte: os scripts que geram tudo isso, para quem mantém o kit.

## O que você ganha

Três camadas: Contexto (quem somos, negócio, processo comercial, cliente ideal, produtos, voz, time), Memória (decisões, aprendizados, clientes, diário, projetos) e Ação (roteiros para registrar atendimento, preparar reunião e escrever follow-up). Depois de criada, use frases como "Guarde isso no meu cérebro" e "Prepare minha reunião com o cliente X". O arquivo COMECE-AQUI.md da sua pasta explica o dia a dia.
""")

# ---- referência (marcadores trocados) para o validador
for p in paths:
    write(os.path.join(OUT, "referencia", *p.split("/")),
          FILES[p].rstrip("\n").replace("{{EMPRESA}}", "Empresa Exemplo").replace("{{DATA}}", "2026-10-26") + "\n")

# ---- zip no formato do GitHub (pasta única na raiz), para teste e publicação manual
raiz = "segundo-cerebro-" + TAG.lstrip("v")
zpath = os.path.join(OUT, raiz + ".zip")
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for d, _, fs in os.walk(REPO):
        rel = os.path.relpath(d, REPO)
        if rel.split(os.sep)[0] in ("fonte", "__pycache__"):
            continue
        for f in fs:
            full = os.path.join(d, f)
            arc = os.path.join(raiz, os.path.relpath(full, REPO))
            z.write(full, arc)

for nome in ("PROMPT-CLAUDE.md", "PROMPT-GPT.md", "PROMPT-COMPLETO.md"):
    t = open(os.path.join(REPO, nome), encoding="utf-8").read()
    print(nome, "palavras:", len(t.split()))
print("arquivos no template:", n, "| pastas:", pastas_n, "| zip:", os.path.getsize(zpath), "bytes")
