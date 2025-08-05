[Leia em Português](README.md)

# Python Microservice Template

This is the standard Golden Path template for creating new Python microservices at **[Your Company Name]**. The goal is to accelerate development by ensuring new services are born with best practices for containerization, project structure, code quality, and a modern, consistent development experience.

[![CI Quality Checks](https://github.com/YOUR-USERNAME/template-servico-python/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR-USERNAME/template-servico-python/actions/workflows/ci.yml)

## What's Included?

* **Dev Container Environment:** Full VSCode Dev Containers configuration for a one-click setup.
* **Language:** Python 3.11
* **Database:** Ready-to-use Postgres container.
* **Web Framework:** Flask with a Blueprint-based organization.
* **WSGI Server:** Gunicorn as a robust production server.
* **Automated Code Quality:** Black, Flake8, and Mypy.
* **Testing:** Ready-to-use testing structure with `pytest`.
* **Containerization:** Optimized multi-stage `Dockerfile`.
* **Automation:** `Makefile` with shortcuts for all common tasks.
* **Basic CI:** GitHub Actions pipeline that validates the build, tests, and code quality.

## Getting Started (Dev Container Workflow)

1.  **Prerequisites:** Ensure you have **Docker** and **VSCode** with the [**Dev Containers**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension installed.

2.  **Open the Project:** Clone this repository and open the folder in VSCode.

3.  **Start the Environment:** A notification will appear in the bottom-right corner. Click on **"Reopen in Container"**. The first time, this will take a few minutes.

4.  **Environment Ready:** At the end of the process, the environment will be 100% ready:
    * The `app`, `db`, and `docs` containers will be running.
    * A terminal will appear executing `make run-dev`, with the web server already started.

5.  **Start Developing!** The application is available at `http://localhost:8080` and the API docs at `http://localhost:8081`. Open a new terminal (`Ctrl+'`) to run other commands.

## Makefile Commands

The `Makefile` is the project's control panel. Run `make` or `make help` to see the list of all available commands.

### Development Commands (to be used INSIDE the Dev Container)

| Command      | Description                                                                              |
| :----------- | :--------------------------------------------------------------------------------------- |
| `make test`    | 🧪 Runs the full test suite with `pytest`.                                               |
| `make lint`    | 🔍 Runs code quality checks (Flake8 and Mypy) to find errors and style issues.         |
| `make format`  | 🎨 Formats all code automatically with `Black` to ensure a consistent style.               |
| `make run-dev` | ▶️ Starts the web server manually with hot-reload (optional in the Dev Container).     |


### Environment Management Commands (to be used OUTSIDE the Dev Container)

| Command             | Description                                                                                 |
| :------------------ | :------------------------------------------------------------------------------------------ |
| `make up`           | 🚀 Brings up the entire environment (app and db) in the background.                           |
| `make down`         | ⛔ Stops and removes all containers from the environment.                                     |
| `make logs`         | 📜 Shows the real-time logs from all containers.                                              |
| `make restart`      | 🔄 Restarts the entire environment (equivalent to `make down` then `make up`).                |
| `make clean`        | 🧹 Stops the environment and removes persistent data (database volumes). Use with caution. |
| `make install-dev`  | 📦 Installs local dependencies to run without Docker (alternative mode).                    |

ℹ️ **Note:** Inside the Dev Container, the `make up` and `make run-dev` commands are generally not needed, as the server and database will already be running automatically.

## Workflow (Gitflow)

This project uses a workflow based on Gitflow to ensure code organization and quality. The main branches are:

* **`main`**: Reflects the code in **production**. It is a stable and protected branch. No direct pushes are allowed.
* **`develop`**: The integration branch that contains the latest features ready for the **staging** environment. It serves as the base for all new development.
* **`feature/*`**, **`bugfix/*`**, etc.: All new work must be done in its own branch, created from `develop`.

The development cycle is as follows:
1.  Create a new branch from `develop` (e.g., `feature/advanced-login`).
2.  Make your work commits on this branch.
3.  When finished, open a **Pull Request** from your branch to `develop`.
4.  The CI/CD pipeline will run tests and quality checks. The team will perform a Code Review.
5.  After approval and a successful CI run, the Pull Request is merged into `develop`, which triggers a new image build for the staging environment.

### Releasing a New Version to Production (Manual Process)

Releasing a new version to production is a deliberate, manual process to be executed by the Project Manager or Tech Lead. It is triggered by creating a **Git tag** on the `main` branch.

**Prerequisite:** The `main` branch must be up-to-date with the content from `develop` (usually via a Pull Request from `develop` to `main`).

**Steps for Release (e.g., version v1.2.3):**

1.  **Sync your local `main` branch:**
    ```bash
    git checkout main
    git pull origin main
    ```

2.  **Create an annotated version tag:**
    ```bash
    # The -a creates an annotated tag, and -m adds a release message
    git tag -a v1.2.3 -m "Release v1.2.3: Adds social login and fixes bug X."
    ```

3.  **Push the tag to GitHub (This is the trigger!):**
    ```bash
    git push origin v1.2.3
    ```
    Upon receiving this new tag, GitHub Actions will initiate the production pipeline, which will build the final image and tag it with `latest` and `v1.2.3`.

## Project Structure

The folder structure is designed to be scalable and organized:
```
.
├── .devcontainer/ # Dev Container configuration
├── .github/      # GitHub Actions Workflows (CI/CD)
├── .vscode/      # VSCode tasks and settings (Debug, Tasks)
├── deploy/       # (Future) Deployment manifests
├── docs/         # Documentation (ADRs, OpenAPI)
├── src/          # Application source code
├── tests/        # Unit and integration tests
├── .gitignore
├── Dockerfile    # PRODUCTION image build definition
├── Makefile      # Shortcuts for common commands
├── README.md     # This documentation (Portuguese)
├── README.en.md  # This documentation (English)
├── docker-compose.yml # Service orchestrator (app, db)
├── pyproject.toml     # Quality tools configuration
├── requirements-dev.txt # Development dependencies
└── requirements.txt   # Production dependencies
```

## API Endpoints

| Method | Endpoint      | Description                     |
| :----- | :------------ | :------------------------------ |
| `GET`  | `/health`     | Checks the application's health.|
| `GET`  | `/users/`     | Returns a sample list of users.   |
| `GET`  | `/users/<id>` | Fetches a specific user by ID.    |

## Connecting to the Database

You can connect to the Postgres database running in the `db` container using your favorite database tool (DBeaver, DataGrip, etc.) with the following parameters:

* **Host:** `localhost`
* **Port:** `5432`
* **User:** `myuser`
* **Password:** `mypassword`
* **Database:** `mydatabase`

## How to Use This Template for a New Service

1.  Navigate to the main page of this repository on GitHub.
2.  Click the green **"Use this template"** button and select "Create a new repository".
3.  Name your new microservice and follow the "Getting Started" guide above.
