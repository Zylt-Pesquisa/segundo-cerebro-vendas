# -*- coding: utf-8 -*-
"""Helpers compartilhados pelo gerador do kit Segundo Cérebro."""

PH = "[A PREENCHER]"


def fm(tipo, titulo, resumo, status="rascunho", fonte="modelo do kit",
       rel=None, extra=None):
    """Frontmatter padrão. Valores sem dois-pontos para manter YAML válido."""
    linhas = [
        "---",
        "tipo: " + tipo,
        "titulo: " + titulo,
        "resumo: " + resumo,
        "status: " + status,
        "atualizado_em: {{DATA}}",
        "fonte: " + fonte,
        "relacionados: [" + ", ".join(rel or []) + "]",
    ]
    for k, v in (extra or {}).items():
        # no frontmatter, colchetes viram lista YAML; usa texto simples
        linhas.append(k + ": " + ("A PREENCHER" if v == PH else v))
    linhas.append("---")
    return "\n".join(linhas) + "\n\n"


def indice(titulo, resumo, itens, quando, rel=None, status="vigente"):
    """Gera um _index.md. itens = lista de (nome, caminho, descricao)."""
    corpo = fm("indice", titulo, resumo, status=status,
               fonte="estrutura inicial", rel=rel)
    corpo += "# " + titulo + "\n\n## O que há aqui\n\n"
    for nome, caminho, desc in itens:
        corpo += "- [" + nome + "](" + caminho + ") — " + desc + "\n"
    corpo += "\n## Quando usar\n\n" + quando.strip() + "\n"
    return corpo
