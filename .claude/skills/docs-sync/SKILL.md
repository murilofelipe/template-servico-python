---
name: docs-sync
description: Sincroniza a documentacao do template-servico-python a partir do que mudou no codigo.
disable-model-invocation: true
---

# Sincronizar documentacao com o codigo

## Passos

1. `git diff develop...HEAD` para mapear alteracoes.
2. Atualize docs vivos aplicaveis:
   - `Makefile`/`README` se mudou execucao/dependencia.
   - `docs/context-snapshot.md` / `.claude/PROJECT_CONTEXT.md` se mudou arquitetura.
   - `.claude/LEARNINGS.md` se pegou um bug recorrente ou regra nova.
3. Commitar documentacao separada do codigo.
