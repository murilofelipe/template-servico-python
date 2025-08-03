# Makefile

# Define o nome do projeto, usado para nomear os contêineres e outros recursos do Docker.
COMPOSE_PROJECT_NAME=template-servico

# .DEFAULT_GOAL é executado se você digitar apenas "make" no terminal.
.DEFAULT_GOAL := help

# O .PHONY garante que o make execute o comando mesmo que exista um arquivo com o mesmo nome.
.PHONY: help build up down logs clean restart install-dev test lint format run-dev

# ====================================================================================
# GERENCIAMENTO DO AMBIENTE DOCKER (Para ser usado na máquina Host)
# ====================================================================================

# Sobe todo o ambiente definido no docker-compose.yml em modo detached (segundo plano).
up:
	docker compose up --build -d

# Derruba todo o ambiente (para e remove os contêineres e a rede).
down:
	docker compose down

# Constrói (ou reconstrói) as imagens sem iniciar os contêineres.
build:
	docker compose build

# Mostra os logs de todos os serviços em tempo real.
logs:
	docker compose logs -f

# Um atalho para derrubar o ambiente e subi-lo novamente.
restart: down up

# Limpa tudo de forma mais agressiva: derruba o ambiente e remove os volumes anônimos.
clean:
	docker compose down -v


# ====================================================================================
# DESENVOLVIMENTO E QUALIDADE DE CÓDIGO (Para ser usado DENTRO do Dev Container)
# ====================================================================================

# Roda o servidor de desenvolvimento com hot-reload.
run-dev:
	gunicorn --bind 0.0.0.0:8080 --reload "src.main:create_app()"

# Roda todos os testes automatizados usando pytest.
test:
	pytest -v

# Roda as ferramentas de qualidade de código (linting e checagem de tipos).
lint:
	@echo "🔍 Verificando estilo do código com Flake8..."
	flake8 src/ tests/
	@echo "🧐 Verificando tipos com Mypy..."
	mypy src/
	@echo "✅ Checagens de qualidade concluídas!"

# Formata todo o código automaticamente com Black.
format:
	@echo "🎨 Formatando o código com Black..."
	black src/ tests/


# ====================================================================================
# SETUP (Fluxo alternativo sem Dev Container)
# ====================================================================================

# Instala todas as dependências de produção e desenvolvimento em um venv local.
install-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt


# ====================================================================================
# AJUDA
# ====================================================================================

# Comando de ajuda que se auto-documenta, explicando o que cada comando faz.
help:
	@echo "Comandos disponíveis para o projeto $(COMPOSE_PROJECT_NAME):"
	@echo ""
	@echo "  🐳 Gerenciamento do Ambiente via Docker Compose (fora do DevContainer):"
	@echo "---------------------------------------------------------------------"
	@echo "  make up           🚀 Sobe o ambiente completo (para uso manual, fora do DevContainer)."
	@echo "  make down         ⛔ Para e remove os contêineres."
	@echo "  make logs         📜 Mostra os logs dos serviços em tempo real."
	@echo "  make restart      🔄 Reinicia os serviços do Docker Compose."
	@echo "  make clean        🧹 Remove os contêineres e volumes (dados persistentes)."
	@echo ""
	@echo "  🧩 Desenvolvimento (usado dentro do DevContainer):"
	@echo "---------------------------------------------------------------------"
	@echo "  make run-dev      ▶️  Inicia a aplicação manualmente (caso deseje rodar sem gunicorn no Compose)."
	@echo "  make test         🧪 Executa os testes automatizados com pytest."
	@echo "  make lint         🔍 Verifica estilo e tipos de código (flake8, mypy)."
	@echo "  make format       🎨 Formata o código com Black."
	@echo "  make install-dev  📦 Instala dependências (caso queira rodar local sem container)."
	@echo ""
	@echo "ℹ️  Observação: No DevContainer, o servidor já está ativo via Docker Compose (porta 8080)."
	@echo "               Os comandos 'make up' e 'make run-dev' são opcionais nesse fluxo."
