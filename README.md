[Read this in English](README.en.md)

# Template de Microsserviço em Python

Este é o template padrão (Golden Path) para a criação de novos microsserviços em Python na **[Nome da Sua Empresa]**. O objetivo deste template é acelerar o desenvolvimento, garantindo que novos serviços já nasçam com as melhores práticas de containerização, estrutura de projeto, qualidade de código e uma experiência de desenvolvimento moderna e consistente.

[![Qualidade e Deploy](https://github.com/murilofelipe/template-servico-python/actions/workflows/ci.yml/badge.svg)](https://github.com/murilofelipe/template-servico-python/actions/workflows/ci.yml)
[![Limpeza de Imagens](https://github.com/murilofelipe/template-servico-python/actions/workflows/cleanup-images.yml/badge.svg)](https://github.com/murilofelipe/template-servico-python/actions/workflows/cleanup-images.yml)

## O que está incluído?

* **Ambiente de Desenvolvimento em Contêiner:** Configuração completa com VSCode Dev Containers para um setup com um clique.
* **Linguagem:** Python 3.11.
* **Banco de Dados:** Contêiner Postgres pronto para uso.
* **Framework Web:** Flask com organização por Blueprints.
* **Servidor WSGI:** Gunicorn como servidor de produção robusto.
* **Qualidade de Código Automatizada:** Black, Flake8 e Mypy.
* **Testes:** Estrutura de testes pronta com `pytest`.
* **Containerização:** `Dockerfile` otimizado com build multi-stage.
* **Automação:** `Makefile` com atalhos para todas as tarefas comuns.
* **CI/CD:** Pipeline com GitHub Actions que valida o código, testa, e faz deploy para homologação e produção.

## Modos de Execução

Este projeto pode ser executado de duas formas:

### 🧩 1. Ambiente com Dev Container (recomendado)

- Executado diretamente via VSCode com suporte completo de desenvolvimento.
- O servidor web (`gunicorn`) já inicia automaticamente com hot reload.
- O banco de dados e a documentação Swagger também estão prontos para uso.

💡 A melhor experiência de desenvolvimento é garantida com essa abordagem.

### 🐳 2. Execução manual com Docker Compose

- Útil para rodar o projeto sem Dev Container.
- Requer uso manual dos comandos `make up`, `make run-dev`, etc.
- Indicado para usuários avançados ou CI/CD local.


## Primeiros Passos (Fluxo com Dev Container)

1.  **Pré-requisitos:** Garanta que você tenha **Docker** e **VSCode** com a extensão [**Dev Containers**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) instalada.

2.  **Abra o Projeto:** Clone este repositório e abra a pasta no VSCode.

3.  **Inicie o Ambiente:** Uma notificação aparecerá no canto inferior direito. Clique em **"Reopen in Container"**. Na primeira vez, isso levará alguns minutos.
    
    Se não aparecer a notificação:
    - Pressione `Ctrl+Shift+P` (ou `Cmd+Shift+P` no macOS).
    - Digite e selecione: **“Dev Containers: Rebuild Container”**.
    - Aguarde a construção inicial do ambiente. Isso pode levar alguns minutos na primeira vez.


4.  **Ambiente Pronto:** Ao final do processo, o ambiente estará 100% pronto:
    * Os contêineres `app` e `db` estarão rodando.
    * Um terminal aparecerá executando `make run-dev`, com o servidor web já iniciado.

5.  **Comece a Desenvolver!** A aplicação está disponível em `http://localhost:8080`. Abra um novo terminal (`Ctrl+'`) para executar outros comandos.

## Comandos do Makefile

O `Makefile` é o painel de controle do projeto. Execute `make` ou `make help` para visualizar todos os comandos disponíveis.

### 🧩 Comandos de Desenvolvimento (dentro do Dev Container)

| Comando         | Descrição |
|-----------------|-----------|
| `make test`     | 🧪 Executa todos os testes automatizados com `pytest`. |
| `make lint`     | 🔍 Roda checagens de qualidade de código com Flake8 e Mypy. |
| `make format`   | 🎨 Formata o código com Black. |
| `make run-dev`  | ▶️ Inicia o servidor manualmente com hot reload (opcional no Dev Container). |

### 🐳 Comandos de Ambiente (fora do Dev Container)

| Comando             | Descrição |
|---------------------|-----------|
| `make up`           | 🚀 Sobe o ambiente completo com Docker Compose. |
| `make down`         | ⛔ Para e remove os contêineres. |
| `make logs`         | 📜 Mostra logs em tempo real. |
| `make restart`      | 🔄 Reinicia todos os serviços. |
| `make clean`        | 🧹 Remove contêineres e volumes (útil para resetar tudo). |
| `make install-dev`  | 📦 Instala dependências locais para rodar sem Docker (modo alternativo). |

ℹ️ **Nota:** Dentro do Dev Container, os comandos `make up` e `make run-dev` geralmente não são necessários, pois o servidor e banco de dados já estarão rodando automaticamente.

## Fluxo de Trabalho (Gitflow)

Este projeto utiliza um fluxo de trabalho baseado no Gitflow para garantir a organização e a qualidade do código. As branches principais são:

* **`main`**: Reflete o código em **produção**. É uma branch estável e protegida.
* **`develop`**: Branch de integração que contém as features mais recentes prontas para o ambiente de **homologação (staging)**.
* **`feature/*`**, **`bugfix/*`**, etc.: Todo trabalho novo deve ser feito em uma branch própria, criada a partir da `develop`.

### Ciclo de Desenvolvimento Padrão

Siga estes passos para adicionar uma nova funcionalidade ou corrigir um bug.

**1. Crie sua Branch de Trabalho**
A partir da branch `develop`, crie uma nova branch para o seu trabalho.
```bash
# Sincronize com a versão mais recente da develop
git checkout develop
git pull

# Crie sua nova branch
git checkout -b feature/nome-da-sua-feature
```

**2. Desenvolva e Faça Commits**
Trabalhe no código e faça commits pequenos e lógicos. Use os comandos do `Makefile` (`make test`, `make lint`) para validar seu progresso.
```bash
# Adicione suas alterações
git add .

# Crie o commit
git commit
```

**3. Envie sua Branch para o GitHub**
```bash
git push origin feature/nome-da-sua-feature
```

**4. Abra o Pull Request (O "Merge via Browser")**
Esta é a etapa de revisão e validação.
- Acesse o repositório no GitHub. Uma mensagem sugerindo a criação de um Pull Request para a sua branch aparecerá. Clique nela.
- Defina a branch `base` como **`develop`** e a `compare` como a sua branch de feature.
- Dê um título e uma descrição claros para o seu Pull Request.
- Clique em "Create pull request".

**5. Revisão e Validação Automática**
- O pipeline de CI será executado automaticamente para rodar testes e linting.
- A equipe fará a revisão do código (Code Review), deixando comentários e sugestões.

**6. Aprovação e Merge**
- Após as aprovações e o sucesso do CI, o botão **"Merge pull request"** ficará disponível.
- **Clicar neste botão** finaliza o processo, mesclando seu código na `develop`.

**7. Deploy em Homologação**
- O merge na `develop` acionará o pipeline de deploy, que publicará uma nova imagem de homologação com a tag `:develop`.

### Lançando uma Nova Versão para Produção

Lançar uma nova versão para produção é um processo manual e deliberado, a ser executado pelo Gerente de Projeto ou Líder Técnico. Ele é acionado pela criação de uma **tag Git** na branch `main`.

**Pré-requisito:** A branch `main` deve estar atualizada com o conteúdo da `develop` (através de um Pull Request de `develop` para `main`).

**Passos para o Lançamento (ex: versão v1.2.3):**

1.  **Sincronize sua branch `main` local:**
    ```bash
    git checkout main
    git pull origin main
    ```

2.  **Crie a tag de versão anotada:**
    ```bash
    # O -a cria uma tag anotada, e -m adiciona uma mensagem de release
    git tag -a v1.2.3 -m "Release v1.2.3: Adiciona login social e corrige bug X."
    ```

3.  **Empurre a tag para o GitHub (Este é o gatilho!):**
    ```bash
    git push origin v1.2.3
    ```
    Ao receber esta nova tag, o GitHub Actions iniciará o pipeline de produção, que construirá a imagem final e a tagueará com `latest` e `v1.2.3`.

## Estrutura do Projeto

A estrutura de pastas foi pensada para ser escalável e organizada:

```
.
├── .devcontainer/ # Configuração do Ambiente de Desenvolvimento em Contêiner
├── .github/      # Workflows do GitHub Actions (CI/CD)
├── .vscode/      # Tarefas e configurações do VSCode (Debug, Tasks)
├── deploy/       # (Futuro) Manifestos de deploy
├── docs/         # Documentação (ADRs, OpenAPI)
├── src/          # Código-fonte da aplicação
├── tests/        # Testes unitários e de integração
├── .gitignore
├── Dockerfile    # Contrato de construção da imagem de PRODUÇÃO
├── Makefile      # Atalhos para comandos comuns
├── README.md     # Esta documentação
├── README.en.md  # Versão em inglês da documentação
├── docker-compose.yml # Orquestrador dos serviços (app, db)
├── pyproject.toml     # Configuração das ferramentas de qualidade
├── requirements-dev.txt # Dependências de desenvolvimento
└── requirements.txt   # Dependências de produção
```

## Endpoints da API

| Método | Endpoint      | Descrição                               |
| :----- | :------------ | :-------------------------------------- |
| `GET`  | `/health`     | Verifica a saúde da aplicação.          |
| `GET`  | `/users/`     | Retorna uma lista de usuários de exemplo. |
| `GET`  | `/users/<id>` | Busca um usuário específico por ID.     |

## Conectando ao Banco de Dados

Você pode se conectar ao banco de dados Postgres que está rodando no contêiner `db` usando sua ferramenta de banco de dados preferida (DBeaver, DataGrip, etc.) com os seguintes parâmetros:

* **Host:** `localhost`
* **Porta:** `5432`
* **Usuário:** `myuser`
* **Senha:** `mypassword`
* **Database:** `mydatabase`

## Como Usar este Template para um Novo Serviço

1.  Navegue até a página principal deste repositório no GitHub.
2.  Clique no botão verde **"Use this template"** e selecione "Create a new repository".
3.  Dê um nome ao seu novo microsserviço e siga os "Primeiros Passos" acima.