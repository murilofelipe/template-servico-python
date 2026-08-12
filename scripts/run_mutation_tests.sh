#!/bin/bash
set -e

echo "Instalando dependências de desenvolvimento..."
pip install -r requirements.txt
pip install -r requirements-dev.txt

echo "Rodando testes unitários e de integração com pytest..."
python -m pytest tests/

echo "Rodando testes de mutação com mutmut..."
# Limpa cache antigo do mutmut, se existir
rm -f .mutmut-cache
mutmut run


# Checa se mutmut encontrou mutantes que sobreviveram
SURVIVING=$(mutmut results | grep "Surviving" -A 10 || true)
if [[ -n "$SURVIVING" ]]; then
    echo "Falha: Mutantes sobreviveram aos testes!"
    mutmut results
    exit 1
else
    echo "Sucesso: Todos os mutantes foram pegos pelos testes."
fi
