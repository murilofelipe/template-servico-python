# 📋 Backlog de Melhorias: template-servico-python

Este documento apresenta o planejamento de melhorias e evolução para o projeto **template-servico-python** (template padrão corporativo de microsserviço com Flask, Docker e CI/CD). O objetivo destas melhorias é modernizar a stack técnica do template, fornecer integrações prontas e reais, e aplicar as melhores práticas do ecossistema Python moderno para que seja um "golden path" na empresa e sirva perfeitamente como portfólio no GitHub.

**Sistema de Estimativa (Peso):** Story Points (1, 2, 3, 5, 8, 13)
**Complexidade:** Baixa, Média, Alta

---

## 🏛️ Épico 1: Modernização da Stack de Desenvolvimento e Qualidade
**Objetivo:** Trazer a stack de tooling e dependências para as versões mais atuais e estáveis do ecossistema Python, simplificando a manutenção do template.

### 🎫 Story 1.1: Unificação de Tooling com Ruff
- **Descrição:** Como desenvolvedor mantenedor, quero substituir a combinação Black + Flake8 pelo `ruff` para reduzir as dependências de desenvolvimento e ter execuções de linting/formatting extremamente rápidas.
- **Complexidade:** Baixa | **Peso:** 2
- **Justificativa do Peso:** Trocar dependências e remover arquivos de configuração antigos é uma tarefa simples e direta, com baixo risco de efeitos colaterais.
- **Tarefas:**
  - [ ] Remover `black` e `flake8` do arquivo `requirements-dev.txt`.
  - [ ] Adicionar `ruff` ao arquivo `requirements-dev.txt`.
  - [ ] Remover o arquivo de configuração `.flake8`.
  - [ ] Adicionar a configuração do `ruff` (linter e formatador) no `pyproject.toml`.
  - [ ] Atualizar as tarefas do `Makefile` (`make lint` e `make format`) para utilizarem o `ruff`.

### 🎫 Story 1.2: Upgrade de Dependências Principais (Flask e Pydantic)
- **Descrição:** Como arquiteto, quero atualizar as principais bibliotecas do projeto para as versões de mercado mais modernas (Flask 3.x e Pydantic v2.x).
- **Complexidade:** Média | **Peso:** 3
- **Justificativa do Peso:** Requer refatoração na sintaxe dos schemas (mudanças no Pydantic v2) e validação de compatibilidade. Há um risco moderado de quebra de contratos ou rotas.
- **Tarefas:**
  - [ ] Atualizar o Flask para a versão `3.0.x` em `requirements.txt`.
  - [ ] Atualizar o Pydantic para a versão `2.x` em `requirements.txt`.
  - [ ] Ajustar os schemas em `src/users/user_schemas.py` para utilizar a sintaxe do Pydantic v2 (ex: usar `model_validator`, `field_validator` e adequar tipos).
  - [ ] Atualizar o código em `src/users/user_routes.py` substituindo `user.dict()` por `user.model_dump()`.
  - [ ] Validar a compatibilidade com o Gunicorn e Werkzeug.

---

## 💾 Épico 2: Integração de Banco de Dados Real no Template
**Objetivo:** Transformar o mock em memória (`fake_db`) em uma conexão real com o banco PostgreSQL já configurado no Docker Compose.

### 🎫 Story 2.1: Adição de ORM e Ferramenta de Migrações
- **Descrição:** Como desenvolvedor que utiliza o template, quero ter o SQLAlchemy 2.0 (ou SQLModel) e Flask-Migrate configurados para não precisar criar a camada de dados do zero.
- **Complexidade:** Média | **Peso:** 3
- **Justificativa do Peso:** Envolve a configuração inicial de bibliotecas essenciais (SQLAlchemy e Alembic) e adaptação do `Makefile`, mas sem necessidade de refatorar regras de negócio ainda.
- **Tarefas:**
  - [ ] Adicionar `Flask-SQLAlchemy` e `Flask-Migrate` (ou `Alembic`) ao `requirements.txt`.
  - [ ] Criar a estrutura inicial de banco em `src/database.py` ou similar e registrar na aplicação em `src/main.py`.
  - [ ] Inicializar o ambiente de migrações com `flask db init`.
  - [ ] Configurar os scripts do Makefile para aplicar as migrações automaticamente ao subir o ambiente.

### 🎫 Story 2.2: Persistência de Dados de Usuários no Banco de Dados
- **Descrição:** Como desenvolvedor, quero que as rotas de exemplo `/users` busquem e salvem informações de verdade no banco de dados.
- **Complexidade:** Média | **Peso:** 5
- **Justificativa do Peso:** Esforço considerável pois envolve mapeamento entidade-relacionamento, mudança nos controllers, remoção do mock e adaptação de múltiplos testes (unitários/integração) para refletir a persistência real.
- **Tarefas:**
  - [ ] Mapear a classe de domínio de usuários para um modelo do SQLAlchemy/SQLModel.
  - [ ] Refatorar `src/users/user_controller.py` para utilizar sessões do banco de dados em vez de ler/escrever na lista `fake_db`.
  - [ ] Ajustar os testes automatizados utilizando um banco SQLite em memória (`sqlite:///:memory:`) para testes.

---

## 📖 Épico 3: Documentação de API Dinâmica e Configurações
**Objetivo:** Tornar a documentação de API e as configurações do projeto mais flexíveis, automáticas e seguras.

### 🎫 Story 3.1: Geração Automática de Documentação Swagger/OpenAPI
- **Descrição:** Como consumidor da API, quero que a documentação Swagger seja gerada dinamicamente com base no código-fonte.
- **Complexidade:** Média | **Peso:** 5
- **Justificativa do Peso:** Requer adicionar e validar decoradores em todas as rotas existentes, lidar com a tipagem de entrada/saída e também remover/substituir o serviço Swagger externo do `docker-compose.yml`.
- **Tarefas:**
  - [ ] Adicionar a biblioteca `apiflask` ou `flask-smorest` ao projeto.
  - [ ] Refatorar a aplicação para usar as anotações do framework de documentação nas rotas.
  - [ ] Desativar o serviço `docs` no `docker-compose.yml` e usar a rota `/docs` da própria aplicação.

### 🎫 Story 3.2: Gerenciamento Centralizado de Configurações
- **Descrição:** Como administrador do sistema, quero gerenciar variáveis de ambiente usando Pydantic Settings para garantir validação de tipos de dados.
- **Complexidade:** Baixa | **Peso:** 2
- **Justificativa do Peso:** Tarefa autocontida e de rápida implementação. Consiste em instanciar uma classe do `pydantic-settings` e trocar os `os.getenv` nas chamadas espalhadas pelo projeto.
- **Tarefas:**
  - [ ] Instalar a biblioteca `pydantic-settings`.
  - [ ] Criar um arquivo `src/core/config.py` declarando as configurações exigidas pela aplicação (ex: `DATABASE_URL`, `PORT`, `DEBUG`).
  - [ ] Ajustar o `src/main.py` e o conector de banco para ler as configurações a partir do objeto `settings`.

### 🎫 Story 3.3: Health Check Avançado
- **Descrição:** Como operador, quero que o endpoint `/health` verifique se o banco de dados está online.
- **Complexidade:** Baixa | **Peso:** 2
- **Justificativa do Peso:** Modificação isolada em apenas um endpoint e com uma query extremamente simples (`SELECT 1`). Risco e esforço muito baixos.
- **Tarefas:**
  - [ ] Modificar `src/healthcheck/health_routes.py` para realizar uma query de teste (`SELECT 1`) no banco.
  - [ ] Retornar `503 Service Unavailable` caso o banco falhe.

---

## 🛡️ Épico 4: Segurança, Observabilidade e Boas Práticas (Portfólio Tier)
**Objetivo:** Adicionar padrões maduros de mercado para um serviço pronto para produção e de alta qualidade para o portfólio.

### 🎫 Story 4.1: Logging Estruturado e Padronizado
- **Descrição:** Adicionar logs em formato JSON, ideais para observabilidade moderna (ELK Stack, Datadog).
- **Complexidade:** Média | **Peso:** 3
- **Justificativa do Peso:** Requer injeção de middlewares no Flask para capturar entradas e saídas e a configuração global do logger (como o `structlog`) para unificar o formato em toda a aplicação.
- **Tarefas:**
  - [ ] Integrar `structlog` ou configurar o módulo padrão `logging` em formato JSON.
  - [ ] Injetar IDs de Requisição (Request ID/Trace ID) nos logs para rastreamento.
  - [ ] Adicionar logs baseados em middleware/decorador para entrada e saída de requisições.

### 🎫 Story 4.2: Segurança Básica (CORS, Rate Limiting, Headers)
- **Descrição:** Preparar a API para um consumo seguro, blindando contra ataques básicos.
- **Complexidade:** Média | **Peso:** 3
- **Justificativa do Peso:** Instalação e configuração de múltiplos middlewares de segurança. Exige testes para garantir que a configuração estrita (principalmente CORS e Headers) não quebre integrações ou requests legítimos.
- **Tarefas:**
  - [ ] Integrar `Flask-CORS` (configurando origens permitidas).
  - [ ] Integrar `Flask-Limiter` para proteger contra força bruta e DDoS.
  - [ ] Adicionar headers de segurança recomendados (ex: usar `flask-talisman`).

### 🎫 Story 4.3: Automação de Análise de Segurança (SAST)
- **Descrição:** Integrar análise estática no fluxo de CI para barrar vulnerabilidades conhecidas no código.
- **Complexidade:** Baixa | **Peso:** 2
- **Justificativa do Peso:** Adição de uma etapa (Bandit) no workflow do GitHub Actions. Não requer grandes mudanças lógicas na base de código, e tem implementação direta no pipeline existente.
- **Tarefas:**
  - [ ] Instalar a ferramenta `bandit` no ambiente dev.
  - [ ] Adicionar step de verificação de segurança no GitHub Actions (`ci.yml`).

---

## 📦 Épico 5: Infraestrutura, Testes e CI/CD Avançado
**Objetivo:** Garantir uma imagem imbatível e garantir a integridade do código com cobertura real de testes.

### 🎫 Story 5.1: Dockerfile Otimizado, Multistage e Non-root
- **Descrição:** Reduzir o tamanho da imagem de produção e aumentar a segurança rodando sem permissões de root.
- **Complexidade:** Média | **Peso:** 3
- **Justificativa do Peso:** Modificar a estrutura do Dockerfile exige testes práticos para garantir que as permissões (usuário non-root) não quebrem a execução do Gunicorn ou causem problemas ao ler/gravar diretórios.
- **Tarefas:**
  - [ ] Refatorar o `Dockerfile` atual para utilizar cache do pip e builds multi-stage.
  - [ ] Criar e configurar um usuário não-root (ex: `appuser`) no contêiner de produção.
  - [ ] Adicionar e otimizar regras do arquivo `.dockerignore`.

### 🎫 Story 5.2: Relatórios de Cobertura de Testes (Coverage)
- **Descrição:** Mensurar a cobertura dos testes unitários/integração e evitar merges que abaixem a cobertura.
- **Complexidade:** Baixa | **Peso:** 2
- **Justificativa do Peso:** Trata-se da configuração de ferramentas maduras (`pytest-cov`). A maior parte do trabalho é apenas amarrar a ferramenta ao CI e atualizar os atalhos do `Makefile`.
- **Tarefas:**
  - [ ] Instalar biblioteca `pytest-cov`.
  - [ ] Atualizar o comando do `Makefile` (`make test`) para incluir a flag `--cov=src`.
  - [ ] Adicionar bloqueio/check de CI/CD para cobertura mínima (ex: fail under 80%).
