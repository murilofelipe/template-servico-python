# 📋 Backlog de Melhorias: template-servico-python

Este documento apresenta o planejamento de melhorias e evolução para o projeto **template-servico-python** (template padrão corporativo de microsserviço com Flask, Docker e CI/CD). O objetivo destas melhorias é modernizar a stack técnica do template e fornecer integrações prontas e reais (como banco de dados funcional) para acelerar a criação de novos microsserviços.

---

## 🏛️ Épico 1: Modernização da Stack de Desenvolvimento e Qualidade
**Objetivo:** Trazer a stack de tooling e dependências para as versões mais atuais e estáveis do ecossistema Python, simplificando a manutenção do template.

### 🎫 Story 1.1: Unificação de Tooling com Ruff
- **Descrição:** Como desenvolvedor mantenedor do template, quero substituir a combinação Black + Flake8 pelo `ruff` para reduzir as dependências de desenvolvimento e ter execuções de linting/formatting extremamente rápidas.
- **Tarefas:**
  - [ ] Remover `black` e `flake8` do arquivo `requirements-dev.txt`.
  - [ ] Adicionar `ruff` ao arquivo `requirements-dev.txt`.
  - [ ] Remover o arquivo de configuração `.flake8`.
  - [ ] Adicionar a configuração do `ruff` (linter e formatador) no `pyproject.toml`.
  - [ ] Atualizar as tarefas do `Makefile` (`make lint` e `make format`) para utilizarem o `ruff`.

### 🎫 Story 1.2: Upgrade de Dependências Principais (Flask e Pydantic)
- **Descrição:** Como arquiteto, quero atualizar as principais bibliotecas do projeto para as versões de mercado mais modernas (Flask 3.x e Pydantic v2.x).
- **Tarefas:**
  - [ ] Atualizar o Flask para a versão `3.0.x` em `requirements.txt`.
  - [ ] Atualizar o Pydantic para a versão `2.x` em `requirements.txt`.
  - [ ] Ajustar os schemas em `src/users/user_schemas.py` para utilizar a sintaxe do Pydantic v2 (ex: usar `model_validator`, `field_validator` se necessário, e adequar tipos).
  - [ ] Atualizar o código em `src/users/user_routes.py` substituindo as chamadas de `user.dict()` por `user.model_dump()`.
  - [ ] Validar a compatibilidade com o Gunicorn e Werkzeug.

---

## 💾 Épico 2: Integração de Banco de Dados Real no Template
**Objetivo:** Transformar o mock em memória (`fake_db`) em uma conexão real com o banco PostgreSQL já configurado no Docker Compose.

### 🎫 Story 2.1: Adição de ORM e Ferramenta de Migrações
- **Descrição:** Como desenvolvedor que utiliza o template, quero ter o SQLAlchemy (ou SQLModel) e Flask-Migrate configurados para não precisar criar a camada de dados do zero.
- **Tarefas:**
  - [ ] Adicionar `Flask-SQLAlchemy` e `Flask-Migrate` (ou `Alembic`) ao `requirements.txt`.
  - [ ] Criar a estrutura inicial de banco em `src/database.py` ou similar e registrar na aplicação em `src/main.py`.
  - [ ] Inicializar o ambiente de migrações com `flask db init`.
  - [ ] Configurar os scripts do Makefile para aplicar as migrações automaticamente ao subir o ambiente.

### 🎫 Story 2.2: Persistência de Dados de Usuários no Banco de Dados
- **Descrição:** Como desenvolvedor, quero que as rotas de exemplo `/users` busquem e salvem informações de verdade no banco de dados.
- **Tarefas:**
  - [ ] Mapear a classe de domínio de usuários para um modelo do SQLAlchemy/SQLModel.
  - [ ] Refatorar `src/users/user_controller.py` para utilizar sessões do banco de dados em vez de ler/escrever na lista `fake_db`.
  - [ ] Ajustar os testes automatizados utilizando um banco SQLite em memória (`sqlite:///:memory:`) para os testes unitários/integração.

---

## 📖 Épico 3: Documentação de API Dinâmica e Configurações
**Objetivo:** Tornar a documentação de API e as configurações do projeto mais flexíveis, automáticas e seguras.

### 🎫 Story 3.1: Geração Automática de Documentação Swagger/OpenAPI
- **Descrição:** Como consumidor da API, quero que a documentação Swagger seja gerada dinamicamente com base no código-fonte, evitando a necessidade de sincronizar manualmente um arquivo `openapi.yml`.
- **Tarefas:**
  - [ ] Adicionar a biblioteca `apiflask` ou `flask-smorest` ao projeto.
  - [ ] Refatorar a aplicação para usar as anotações do framework de documentação nas rotas.
  - [ ] Desativar o serviço `docs` (Swagger UI estático) no `docker-compose.yml` e passar a expor o Swagger direto na rota `/docs` ou `/swagger` da própria aplicação.

### 🎫 Story 3.2: Gerenciamento Centralizado de Configurações
- **Descrição:** Como administrador do sistema, quero gerenciar as variáveis de ambiente utilizando Pydantic Settings para garantir validação de tipos de dados de configuração em tempo de execução.
- **Tarefas:**
  - [ ] Instalar a biblioteca `pydantic-settings`.
  - [ ] Criar um arquivo `src/core/config.py` declarando as configurações exigidas pela aplicação (ex: `DATABASE_URL`, `PORT`, `DEBUG`).
  - [ ] Ajustar o `src/main.py` e o conector de banco para ler as configurações a partir do objeto `settings`.

### 🎫 Story 3.3: Health Check Avançado
- **Descrição:** Como operador do sistema, quero que o endpoint `/health` verifique se o banco de dados está online e respondendo adequadamente.
- **Tarefas:**
  - [ ] Modificar `src/healthcheck/health_routes.py` para realizar uma query simples de teste (ex: `SELECT 1`) no banco de dados.
  - [ ] Retornar status de erro HTTP correspondente (`503 Service Unavailable`) caso o banco de dados falhe no teste.
