# CLAUDE.md — Template de Microsserviço em Python

> Carregado automaticamente no inicio de toda sessao neste projeto.

## Comece pelo snapshot (economia de contexto)

Para a maioria das tarefas, `docs/context-snapshot.md` traz o estado atual e
regras — comece por ele. Quem alterar arquitetura deve atualizar o snapshot.

## Leia antes de tarefas que toquem no assunto

1. `.junie/PROJECT_CONTEXT.md` — stack, convencoes, status atual
2. `.junie/LEARNINGS.md` — erros recorrentes e regras aprendidas
3. `BACKLOG.md` — backlog e sprints planejados

## Regras deste projeto

- Flask com organizacao por Blueprints para rotas.
- Gunicorn como servidor WSGI de producao.
- Pydantic para schemas e validacao de dados.
- Qualidade de codigo: Black, Flake8 e Mypy (para unificar em Ruff no futuro).
- Testes automatizados com `pytest` (unitarios e integracao).
- Dev Containers para configuracao rapida do ambiente.

## Ao final de uma sessao que mudou arquitetura ou aprendizado

Ofereca atualizar `.junie/PROJECT_CONTEXT.md` e `.junie/LEARNINGS.md`.
