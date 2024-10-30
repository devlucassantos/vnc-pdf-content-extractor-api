# vnc-pdf-content-extractor-api

🌍 *[English](README.md) ∙ [Português](README_pt.md)*

`vnc-pdf-content-extractor-api` is the service responsible for extracting the content of PDFs used by the
[Você na Câmara (VNC)](#você-na-câmara-vnc) platform. In this repository you will find the source code of the VNC PDF
content extractor API and also the container responsible for executing this code, so you can easily run the project.

## How to run

### Running via Docker

To run the API you will need to have [Docker](https://www.docker.com) installed on your machine and run the following
commands in the root directory of this project:

````shell
docker compose up
````

### Documentation

After running the project, all the available routes for accessing the API can be found via the link:

> [http://localhost:8084/api/documentation](http://localhost:8084/api/documentation)

## Você na Câmara (VNC)

Você na Câmara (VNC) is a news platform that seeks to simplify the propositions under debate in the Chamber of Deputies
of Brazil aiming to synthesize the ideas of these propositions through the use of Artificial Intelligence (AI) so that
these documents can have their ideas expressed in a simple and objective way for the general population.
