[Leia em Português](README.md)

# Python Microservice Template

This is the standard Golden Path template for creating new Python microservices at **[Your Company Name]**. The goal of this template is to accelerate development by ensuring new services are born with best practices for containerization, project structure, code quality, and a modern, consistent development experience.

[![Quality & Deploy](https://github.com/murilofelipe/template-servico-python/actions/workflows/ci.yml/badge.svg)](https://github.com/murilofelipe/template-servico-python/actions/workflows/ci.yml)
[![Image Cleanup](https://github.com/murilofelipe/template-servico-python/actions/workflows/cleanup-images.yml/badge.svg)](https://github.com/murilofelipe/template-servico-python/actions/workflows/cleanup-images.yml)


## What's Included?

* **Dev Container Environment:** Full VSCode Dev Containers configuration for a one-click setup.
* **Language:** Python 3.11.
* **Database:** Ready-to-use Postgres container.
* **Web Framework:** Flask with a Blueprint-based organization.
* **WSGI Server:** Gunicorn as a robust production server.
* **Automated Code Quality:** Black, Flake8, and Mypy.
* **Testing:** Ready-to-use testing structure with `pytest`.
* **Containerization:** Optimized multi-stage `Dockerfile`.
* **Automation:** `Makefile` with shortcuts for all common tasks.
* **CI/CD:** GitHub Actions pipeline that validates, tests, and deploys code for staging and production.

## Execution Modes

This project can be run in two ways:

### 🧩 1. Dev Container Environment (recommended)

- Runs directly via VSCode with a full-featured development environment.
- The web server (`gunicorn`) starts automatically with hot reload.
- The database and Swagger documentation are also ready to use.

💡 The best development experience is guaranteed with this approach.

### 🐳 2. Manual Execution with Docker Compose

- Useful for running the project without the Dev Container integration.
- Requires manual use of commands like `make up`, `make run-dev`, etc.
- Recommended for advanced users or local CI/CD scenarios.


## Getting Started (Dev Container Workflow)

1.  **Prerequisites:** Ensure you have **Docker** and **VSCode** with the [**Dev Containers**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension installed.

2.  **Open the Project:** Clone this repository and open the folder in VSCode.

3.  **Start the Environment:** A notification will appear in the bottom-right corner. Click on **"Reopen in Container"**. The first time, this will take a few minutes.
    
    If the notification does not appear:
    - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS).
    - Type and select: **“Dev Containers: Rebuild Container”**.
    - Wait for the initial environment build. This may take a few minutes the first time.


4.  **Environment Ready:** At the end of the process, the environment will be 100% ready:
    * The `app` and `db` containers will be running.
    * A terminal will appear executing `make run-dev`, with the web server already started.

5.  **Start Developing!** The application is available at `http://localhost:8080`. Open a new terminal (`Ctrl+'`) to run other commands.

## Makefile Commands

The `Makefile` is the project's control panel. Run `make` or `make help` to see the list of all available commands.

### 🧩 Development Commands (inside the Dev Container)

| Command         | Description |
|-----------------|-----------|
| `make test`     | 🧪 Runs all automated tests with `pytest`. |
| `make lint`     | 🔍 Runs code quality checks with Flake8 and Mypy. |
| `make format`   | 🎨 Formats the code with Black. |
| `make run-dev`  | ▶️ Starts the server manually with hot reload (optional in the Dev Container). |

### 🐳 Environment Commands (outside the Dev Container)

| Command             | Description |
|---------------------|-----------|
| `make up`           | 🚀 Brings up the complete environment with Docker Compose. |
| `make down`         | ⛔ Stops and removes the containers. |
| `make logs`         | 📜 Shows real-time logs. |
| `make restart`      | 🔄 Restarts all services. |
| `make clean`        | 🧹 Removes containers and volumes (useful for a full reset). |
| `make install-dev`  | 📦 Installs local dependencies to run without Docker (alternative mode). |

ℹ️ **Note:** Inside the Dev Container, the `make up` and `make run-dev` commands are generally not needed, as the server and database will already be running automatically.

## Workflow (Gitflow)

This project uses a workflow based on Gitflow to ensure code organization and quality. The main branches are:

* **`main`**: Reflects the code in **production**. It is a stable and protected branch.
* **`develop`**: The integration branch that contains the latest features ready for the **staging** environment.
* **`feature/*`**, **`bugfix/*`**, etc.: All new work must be done in its own branch, created from `develop`.

### Standard Development Cycle

Follow these steps to add a new feature or fix a bug.

**1. Create Your Working Branch**
From the `develop` branch, create a new branch for your work.
```bash
# Sync with the latest version of develop
git checkout develop
git pull

# Create your new branch
git checkout -b feature/your-feature-name
```

**2. Develop and Commit**
Work on the code and make small, logical commits. Use `Makefile` commands (`make test`, `make lint`) to validate your progress.
```bash
# Add your changes
git add .

# Create the commit
git commit
```

**3. Push Your Branch to GitHub**
```bash
git push origin feature/your-feature-name
```

**4. Open a Pull Request**
This is the review and validation step.
- Go to the repository on GitHub. A prompt to create a Pull Request for your branch will appear. Click on it.
- Set the `base` branch to **`develop`** and the `compare` branch to your feature branch.
- Give your Pull Request a clear title and description.
- Click "Create pull request".

**5. Review and Automated Validation**
- The CI pipeline will run automatically to execute tests and linting.
- The team will perform a Code Review, leaving comments and suggestions.

**6. Approval and Merge**
- After approvals and a successful CI run, the **"Merge pull request"** button will become available.
- **Clicking this button** finalizes the process, merging your code into `develop`.

**7. Staging Deploy**
- The merge into `develop` will trigger the deployment pipeline, which will publish a new staging image with the `:develop` tag.

### Releasing a New Version to Production

Releasing a new version to production is a deliberate, manual process executed by the Project Manager or Tech Lead. It is triggered by creating a **Git tag** on the `main` branch.

**Prerequisite:** The `main` branch must be up-to-date with the content from `develop` (usually via a Pull Request from `develop` to `main`).

**Steps for Release (e.g., version v1.2.3):**

1.  **Sync your local `main` branch:**
    ```bash
    git checkout main
    git pull origin main
    ```

2.  **Create an annotated version tag:**
    ```bash
    git tag -a v1.2.3 -m "Release v1.2.3: Adds social login and fixes bug X."
    ```

3.  **Push the tag to GitHub (This is the trigger!):**
    ```bash
    git push origin v1.2.3
    ```
    Upon receiving this new tag, GitHub Actions will initiate the production pipeline.

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