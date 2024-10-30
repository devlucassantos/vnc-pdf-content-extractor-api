# vnc-pdf-content-extractor-api

🌍 *[English](README.md) ∙ [Português](README_pt.md)*

`vnc-pdf-content-extractor-api` é o serviço responsável por realizar a extração de conteúdo dos PDFs utilizados pela
plataforma [Você na Câmara (VNC)](#você-na-câmara-vnc). Neste repositório você encontrará o código-fonte da API do
extrator de conteúdo dos PDFs e também o container responsável por executar este código, deste modo você poderá
facilmente rodar o projeto.

## Como Executar

### Executando via Docker

Para executar a API você precisará ter o [Docker](https://www.docker.com) instalado na sua máquina e executar o seguinte
comando no diretório raiz deste projeto:

````shell
docker compose up
````

### Documentação

Após a execução do projeto, todas as rotas disponíveis para acesso à API podem ser encontradas através do link:

> [http://localhost:8084/api/documentation](http://localhost:8084/api/documentation)

## Você na Câmara (VNC)

Você na Câmara (VNC) é uma plataforma de notícias que busca simplificar as proposições que tramitam pela Câmara dos
Deputados do Brasil visando sintetizar as ideias destas proposições através do uso da Inteligência Artificial (IA)
de modo que estes documentos possam ter suas ideias expressas de maneira simples e objetiva para a população em geral.
