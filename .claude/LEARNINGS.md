# Template Serviço Python — Aprendizados

> Erros e boas praticas aprendidos.

## Qualidade de Codigo

- Executar `black`, `flake8` e `mypy` localmente antes de commitar para evitar falhas de lint em produção.
- Ruff e o candidato ideal para unificar as ferramentas de qualidade no futuro.

## Testes

- Sempre usar fixtures do pytest para banco ou cliente de teste para evitar vazamento de estado entre testes.
