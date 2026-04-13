# Nome do interpretador
PYTHON = python3

# Ambiente virtual
VENV = venv
ACTIVATE = source $(VENV)/bin/activate

# Executar o projeto
run:
	$(PYTHON) src/main.py

# Criar ambiente virtual
venv:
	$(PYTHON) -m venv $(VENV)

# Instalar dependências
install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

# Limpar cache
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +

# Rodar com venv (Linux/Mac)
run-venv:
	. $(VENV)/bin/activate && $(PYTHON) src/main.pyv