# Dockerfile

# --- Estágio 1: Builder ---
    FROM python:3.11-slim as builder
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    # --- Estágio 2: Final ---
    FROM python:3.11-slim
    WORKDIR /app
    
    RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*
    
    COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
    COPY --from=builder /usr/local/bin /usr/local/bin
    
    COPY src/ src/
    ENV AMBIENTE=producao
    EXPOSE 8080
    CMD ["gunicorn", "--bind", "0.0.0.0:8080", "src.main:create_app()"]