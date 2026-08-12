---
name: project-conventions
description: Regras inegociaveis do template-servico-python (Flask, Gunicorn, Pydantic, Ruff, pytest). Conhecimento de fundo.
user-invocable: false
---

# Convencoes do template-servico-python

## Arquitetura e Padroes

- Estrutura de rotas baseada em Flask Blueprints.
- Schemas de dados definidos e validados estritamente via Pydantic.
- Gunicorn como WSGI principal para producao.

## Qualidade e Testes

- Formatador e linter: unificacao sob Ruff (atualmente flake8, black, mypy).
- Suíte de testes com `pytest`.

## Processo

- Commitar documentacao separada do de codigo.
- Conventional Commits em pt-BR.
