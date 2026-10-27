# -*- coding: utf-8 -*-
"""Valida uma pasta de Segundo Cérebro contra o padrão.
Uso: python3 validar.py PASTA [--esperado N] [--vazio-ok]
"""
import os, re, sys

TIPOS = {"contexto", "decisao", "aprendizado", "cliente", "projeto", "diario",
         "prioridade", "inbox", "indice", "guia", "conector"}
STATUS = {"rascunho", "vigente", "substituido", "arquivado", "modelo", "reservado"}
COMUNS = ["tipo", "titulo", "resumo", "status", "atualizado_em", "fonte", "relacionados"]
DATA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)\)")


def frontmatter(texto):
    if not texto.startswith("---\n"):
        return None, texto
    fim = texto.find("\n---\n", 4)
    if fim < 0:
        return None, texto
    bloco = texto[4:fim]
    campos = {}
    for ln in bloco.split("\n"):
        if ":" in ln:
            k, v = ln.split(":", 1)
            campos[k.strip()] = v.strip()
    return campos, texto[fim + 5:]


def main():
    raiz = sys.argv[1]
    esperado = None
    if "--esperado" in sys.argv:
        esperado = int(sys.argv[sys.argv.index("--esperado") + 1])
    erros, avisos = [], []
    arquivos = []
    for d, _, fs in os.walk(raiz):
        if ".obsidian" in d.split(os.sep) or ".git" in d.split(os.sep):
            continue
        for f in fs:
            if f.endswith(".md"):
                arquivos.append(os.path.relpath(os.path.join(d, f), raiz).replace(os.sep, "/"))
    arquivos.sort()
    if esperado is not None and len(arquivos) != esperado:
        erros.append("esperava %d arquivos .md, achei %d" % (esperado, len(arquivos)))
    existentes = set(arquivos)

    for p in arquivos:
        t = open(os.path.join(raiz, p), encoding="utf-8").read()
        if "{{" in t or "}}" in t:
            erros.append(p + ": placeholder {{ }} sem troca")
        if "```" in t:
            erros.append(p + ": bloco de código não permitido")
        if "<<<" in t:
            erros.append(p + ": marcador do manifesto vazou para o arquivo")
        if p.endswith("SKILL.md"):
            fmv, corpo = frontmatter(t)
            if not fmv or "name" not in fmv or "description" not in fmv:
                erros.append(p + ": SKILL.md sem name/description")
                continue
            pasta = p.split("/")[-2]
            if fmv["name"] != pasta:
                erros.append(p + ": name '%s' difere da pasta '%s'" % (fmv["name"], pasta))
            if len(fmv["description"]) > 1024:
                erros.append(p + ": description > 1024")
            if not re.fullmatch(r"[a-z0-9-]{1,64}", fmv["name"]):
                erros.append(p + ": name inválido")
            if len(corpo.split("\n")) > 500:
                erros.append(p + ": corpo > 500 linhas")
            continue
        fmv, corpo = frontmatter(t)
        if fmv is None:
            erros.append(p + ": sem frontmatter")
            continue
        for c in COMUNS:
            if c not in fmv:
                erros.append(p + ": falta campo " + c)
        if fmv.get("tipo") not in TIPOS:
            erros.append(p + ": tipo inválido '%s'" % fmv.get("tipo"))
        if fmv.get("status") not in STATUS:
            erros.append(p + ": status inválido '%s'" % fmv.get("status"))
        if len(fmv.get("resumo", "")) > 200:
            erros.append(p + ": resumo > 200 caracteres")
        if not fmv.get("resumo"):
            erros.append(p + ": resumo vazio")
        if fmv.get("status") != "modelo" and not DATA.match(fmv.get("atualizado_em", "")):
            erros.append(p + ": atualizado_em inválido '%s'" % fmv.get("atualizado_em"))
        if fmv.get("status") != "modelo":
            h1 = re.search(r"^# (.+)$", corpo, re.M)
            if not h1:
                erros.append(p + ": sem H1")
        if len(corpo.split()) > 700:
            avisos.append(p + ": mais de 700 palavras")
        # links relativos
        base = os.path.dirname(p)
        for alvo in LINK.findall(corpo):
            if re.match(r"^[a-z]+:", alvo):
                continue
            destino = os.path.normpath(os.path.join(base, alvo)).replace(os.sep, "/")
            if destino not in existentes:
                erros.append(p + ": link quebrado -> " + alvo)
        # relacionados
        rel = fmv.get("relacionados", "").strip("[]")
        for alvo in [x.strip() for x in rel.split(",") if x.strip()]:
            destino = os.path.normpath(os.path.join(base, alvo)).replace(os.sep, "/")
            if destino not in existentes:
                erros.append(p + ": relacionado inexistente -> " + alvo)

    # cada pasta de nível 1 e 2 tem _index.md (skills tem SKILL.md; _restrito/automacoes tem README)
    pastas = set()
    for p in arquivos:
        partes = p.split("/")[:-1]
        for i in range(1, min(len(partes), 2) + 1):
            pastas.add("/".join(partes[:i]))
    for pasta in sorted(pastas):
        if not (pasta.startswith("01-Contexto") or pasta.startswith("02-Memoria") or pasta == "03-Acao"):
            continue
        if pasta + "/_index.md" not in existentes:
            erros.append(pasta + ": sem _index.md")

    # índices listam todos os irmãos
    for p in arquivos:
        if not p.endswith("/_index.md") and p != "_index.md":
            continue
        base = os.path.dirname(p)
        t = open(os.path.join(raiz, p), encoding="utf-8").read()
        for q in arquivos:
            if q == p:
                continue
            if os.path.dirname(q) == base:
                nome = os.path.basename(q)
            elif os.path.dirname(os.path.dirname(q)) == base and os.path.basename(q) in ("_index.md", "README.md", "SKILL.md"):
                nome = q[len(base) + 1:] if base else q
            else:
                continue
            if base == "" and "/" in q and os.path.basename(q) != "_index.md" and os.path.basename(q) != "README.md":
                continue
            if nome not in t and q[len(base) + 1:] not in t:
                avisos.append(p + ": não lista " + nome)

    lacunas = 0
    for p in arquivos:
        t = open(os.path.join(raiz, p), encoding="utf-8").read()
        fmv, _ = frontmatter(t)
        if fmv and fmv.get("status") in ("rascunho", "vigente") and fmv.get("tipo") in ("contexto", "prioridade", "conector"):
            c = t.count("[A PREENCHER]")
            if c:
                lacunas += c
                avisos.append(p + ": %d lacuna(s) [A PREENCHER]" % c)
    print("arquivos .md:", len(arquivos), "| lacunas abertas no Contexto:", lacunas)
    for e in erros:
        print("ERRO  ", e)
    for a in avisos:
        print("AVISO ", a)
    print("RESULTADO:", "OK" if not erros else "%d erro(s)" % len(erros))
    sys.exit(1 if erros else 0)


main()
