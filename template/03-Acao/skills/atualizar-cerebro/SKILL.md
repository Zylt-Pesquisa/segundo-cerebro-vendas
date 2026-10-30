---
name: atualizar-cerebro
description: Atualiza um Segundo Cérebro já criado com a versão mais recente do kit, trocando só os arquivos que são do kit (instruções, guias, modelos e skills) e acrescentando os arquivos novos, sem mexer em clientes, decisões, contexto preenchido e anotações. Use quando o usuário pedir para atualizar o cérebro, atualizar o kit, trazer as melhorias novas ou quando uma skill citar um arquivo que não existe na pasta.
---

# Atualizar o cérebro

## Quando usar

O cérebro foi criado com uma versão antiga do kit e o usuário quer as regras, os modelos e as skills mais recentes.

## Antes de começar

Leia `AGENTS.md`, `01-Contexto/00-empresa.md` (nome da empresa) e o `_index.md` da raiz. Confirme que a pasta conectada é o Segundo Cérebro: um `AGENTS.md` ao lado de `01-Contexto`, `02-Memoria` e `03-Acao`.

## Passos

1. Baixe o kit do endereço https://github.com/Zylt-Pesquisa/segundo-cerebro-vendas/archive/refs/heads/main.zip para uma pasta temporária FORA da pasta do cérebro e descompacte. O que vale é a pasta template de dentro do ZIP. Se não conseguir baixar, peça que o usuário abra o endereço no navegador, baixe o ZIP e o coloque na pasta do cérebro, e use esse arquivo.
2. Compare a pasta template com o cérebro e separe três listas.
   - Trocar (arquivos do kit): `AGENTS.md`, `CLAUDE.md`, `COMECE-AQUI.md`, `PADRAO-DE-ARQUIVOS.md`, `ENTREVISTA.md`, `_restrito/README.md`, `03-Acao/automacoes/README.md`, todo arquivo que começa com `_template-` e todo `SKILL.md` de `03-Acao/skills/` que também existe no kit.
   - Acrescentar: arquivos do kit que não existem no cérebro, como um arquivo novo de `01-Contexto/`, uma pasta nova de `02-Memoria/` ou uma skill nova.
   - Não tocar: todo o resto, inclusive os arquivos de `01-Contexto/` que já existem, fichas, decisões, aprendizados, diário, caixa de entrada, prioridades, `03-Acao/conectores.md` e skills criadas pelo usuário.
3. Para os arquivos da lista Trocar, ignore os que já são iguais ao do kit depois de trocar os marcadores. Mostre ao usuário, em poucas linhas, quantos arquivos serão trocados e quantos acrescentados, com os nomes dos principais, e peça confirmação.
4. Com o sim, guarde uma cópia de cada arquivo que será trocado em `_backup-kit/AAAA-MM-DD/`, no mesmo caminho e com `.bak` no fim do nome. Depois copie os arquivos do kit para o cérebro.
5. Em todo arquivo copiado, troque o marcador de empresa pelo nome da empresa e o marcador de data pela data de hoje, como na criação do cérebro.
6. Atualize os índices sem apagar nada: acrescente a linha de cada arquivo ou pasta nova no `_index.md` da pasta e, quando o índice do kit tiver um texto novo em "Quando usar", acrescente esse texto.
7. Não migre fichas antigas de uma vez. As skills completam os campos e as seções que faltarem quando cada ficha for usada.
8. Apague a pasta temporária e o ZIP do kit, se ele estiver na pasta do cérebro. Se não conseguir apagar, diga quais arquivos o usuário deve apagar.
9. Acrescente na nota de diário do dia a linha "Kit do Segundo Cérebro atualizado", com o número de arquivos trocados e acrescentados.
10. Responda em até cinco linhas: o que mudou, onde ficou a cópia dos arquivos antigos e que o usuário pode apagar a pasta `_backup-kit` quando quiser. Se alguma skill citada pelo usuário mudou de nome ou deixou de existir, diga qual.

## Saída esperada

Os arquivos do kit atualizados, os arquivos novos acrescentados, os índices completos, uma cópia dos arquivos antigos em `_backup-kit/` e um resumo curto para o usuário.

## Regras

Esta skill troca arquivos, por isso só age depois da confirmação do passo 3. Nunca sobrescreva nem apague fichas, decisões, aprendizados, diário, caixa de entrada, prioridades, conectores ou arquivos de `01-Contexto/` que já existem. Nunca abra `_restrito/` além do `README.md`. Se a pasta não for um Segundo Cérebro, pare e avise.
