# vnc-pdf-content-extractor-api

🌍 *[English](README.md) ∙ [Português](README_pt.md)*

`vnc-pdf-content-extractor-api` is the service responsible for extracting content from the PDFs used by the
[Você na Câmara (VNC)](#você-na-câmara) platform. In this repository, you will find the source code for the PDF
content extractor API, which uses technologies such as Python and FastAPI. Additionally, the Docker container
responsible for running this code is available, allowing you to execute the project quickly and easily.

## How to run

### Running via Docker

To run the API, you will need to have [Docker](https://www.docker.com) installed on your machine and run the following
command in the root directory of this project:

````shell
docker compose up --build
````

### Documentation

After running the project, all the available routes for accessing the API can be found through the link:

> [http://localhost:8084/api/documentation](http://localhost:8084/api/documentation)
<img width="2880" height="1266" alt="image" src="https://github.com/user-attachments/assets/55278567-b073-4192-b187-bee2686f77cc" />

## Você na Câmara

Você na Câmara (VNC) is a news platform developed to simplify and make accessible the legislative propositions being
processed in the Chamber of Deputies of Brazil. Through the use of Artificial Intelligence, the platform synthesizes the
content of these legislative documents, transforming technical and complex information into clear and objective
summaries for the general public.

This project is part of the Final Paper of the platform's developers and was conceived based on architectures such as
hexagonal and microservices. The solution was organized into several repositories, each with specific responsibilities
within the system:

* [`vnc-databases`](https://github.com/devlucassantos/vnc-databases): Responsible for managing the platform's data
  infrastructure. Main technologies used: PostgreSQL, Redis, Liquibase, and Docker.
* [`vnc-pdf-content-extractor-api`](https://github.com/devlucassantos/vnc-pdf-content-extractor-api): Responsible for
  extracting content from the PDFs used by the platform. Main technologies used: Python, FastAPI, and Docker.
* [`vnc-domains`](https://github.com/devlucassantos/vnc-domains): Responsible for centralizing the platform's domains
  and business logic. Main technology used: Go.
* [`vnc-summarizer`](https://github.com/devlucassantos/vnc-summarizer): Responsible for the software that extracts data
  and summarizes the propositions available on the platform. Main technologies used: Go, PostgreSQL,
  Amazon Web Services (AWS), and Docker.
* [`vnc-api`](https://github.com/devlucassantos/vnc-api): Responsible for providing data to the platform's frontend.
  Main technologies used: Go, Echo, PostgreSQL, Redis, and Docker.
* [`vnc-web-ui`](https://github.com/devlucassantos/vnc-web-ui): Responsible for providing the platform's web interface.
  Main technologies used: TypeScript, SCSS, React, Vite, and Docker.
