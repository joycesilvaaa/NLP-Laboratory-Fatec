# Sistema de Tradução de Texto

## Descrição

Este projeto consiste em um sistema simples de tradução de frases
desenvolvido em **Python**.\
O programa permite que o usuário digite uma frase e receba sua tradução
automaticamente para o idioma escolhido.

A aplicação utiliza a biblioteca **googletrans**, que realiza traduções
utilizando o serviço do Google Translate.

------------------------------------------------------------------------

## Funcionalidades

-   Tradução de frases digitadas pelo usuário
-   Escolha do idioma de destino (Português ou Inglês)
-   Detecção automática do idioma de origem
-   Interface simples via terminal

------------------------------------------------------------------------

## Tecnologias utilizadas

-   Python 3
-   googletrans
-   asyncio

------------------------------------------------------------------------

## Instalação

1.  Instale a biblioteca necessária:

``` bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Como executar

Execute o arquivo principal do projeto:

``` bash
python3 tradutor.py
```

------------------------------------------------------------------------

## Exemplo de uso

Entrada do usuário:

    Digite uma frase: I love programming

Saída do sistema:

    Tradução: Eu amo programar

------------------------------------------------------------------------

## Autor

Projeto desenvolvido para fins acadêmicos.
