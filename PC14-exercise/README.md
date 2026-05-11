# PC14 Exercise

Este projeto é uma aplicação Flask simples que corrige frases em português usando `pyspellchecker`.

## Pré-requisitos

- Python 3.10 ou superior
- `pip` instalado
- Opcional: `uv` instalado para executar a aplicação com o comando `uv run`

## Instalação com pip

1. Abra um terminal na pasta do projeto.
2. Crie um ambiente virtual (recomendado):

```bash
python -m venv .venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executar com pip

Na pasta do projeto, execute:

```bash
python api/main.py
```

Em seguida, abra o navegador em:

```text
http://127.0.0.1:5000
```

## Executar com uv (opcional)

Se você quiser usar o `uv`, instale-o primeiro:

```bash
pip install uv
```

Depois execute a aplicação com:

```bash
uv run python api/main.py
```

Após a execução, acesse:

```text
http://127.0.0.1:5000
```

## Observações

- O ponto de entrada da aplicação é `api/main.py`.
- Se o modo debug estiver ativo, qualquer alteração no código reiniciará o servidor automaticamente.
