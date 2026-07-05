# Template Serviço Python — Contexto do Projeto

## Stack

- **Backend:** Python 3.11 + Flask
- **WSGI Server:** Gunicorn
- **Validação:** Pydantic
- **Testes:** pytest
- **Formatadores/Linter:** black, flake8, mypy
- **Ambiente:** Dev Containers

## Arquitetura

Estrutura limpa de microsserviço com rotas organizadas em Flask Blueprints.

## Status Atual

Template base funcional com um endpoint de exemplo e suite de testes configurada.
Backlog detalhado em `BACKLOG.md`.

## Proximos Passos

1. Configurar Ruff para substituir flake8/black/mypy
2. Adicionar logs estruturados e tracing
3. Implementar CI/CD basico via GitHub Actions
