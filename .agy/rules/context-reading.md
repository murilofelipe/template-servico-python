---
name: read-context
description: Sempre ler a documentação de contexto ao iniciar a sessão deste projeto
---

# Regra: Leitura de Contexto Obrigatória

Ao iniciar o trabalho neste projeto (`template-servico-python`), o agente DEVE, antes de executar tarefas de codificação, análise ou criação de mockups, visualizar e ler os seguintes arquivos para se nortear sobre o sistema:

1. A pasta `docs/` (especialmente arquivos de arquitetura, READMEs ou backups relevantes).
2. Arquivos ocultos de prompt/instrução na raiz do projeto, especificamente `.claude`, `.claude.md`, `.junie` ou `.junie.md`, caso existam.

Essa regra garante que as mudanças propostas estejam alinhadas com as diretrizes e o contexto global preestabelecido pelo usuário e equipe.
