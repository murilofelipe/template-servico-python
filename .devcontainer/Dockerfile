# .devcontainer/Dockerfile

# ATUALIZE A VERSÃO BASE AQUI
FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y vim git curl make bash && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt .
COPY requirements-dev.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

RUN useradd -m vscode
USER vscode

RUN git config --global core.editor vim

WORKDIR /workspace
CMD ["sleep", "infinity"]