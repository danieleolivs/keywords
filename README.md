# Extração de Palavras-chave de Acórdãos

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.7+-brightgreen.svg)

## 🎯 Objetivo

Este projeto oferece uma ferramenta para extrair e analisar as palavras-chave mais frequentes de uma base de dados de acórdãos do Superior Tribunal de Justiça (STJ). A ementa, segundo o manual de padronização do STJ, é o "conjunto de palavras-chave que indicam o assunto discutido e a regra resultante do julgamento". A análise dessas palavras-chave permite categorizar documentos, identificar tendências e facilitar a busca e classificação de jurisprudência de forma eficiente.

## ✨ Funcionalidades

* Processa arquivos JSON contendo dados de acórdãos.
* Extrai todas as palavras-chave listadas.
* Realiza a contagem de frequência de cada palavra-chave.
* Exibe os termos mais recorrentes em formato de tabela.

## 🛠️ Pré-requisitos

* [Python](https.py) (versão 3.7 ou superior)
* [Git](https://git-scm.com/downloads/) para clonar o repositório
* `pip` (gerenciador de pacotes do Python)

## 🚀 Instalação e Configuração

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/danieleolivs/keywords.git
    ```

2.  **Adicione sua base de dados:**
    Coloque seu arquivo de acórdãos em formato `.json` dentro do diretório do projeto. Você pode utilizar a base de dados sugerida, disponível em:
    * [Base de Dados de Acórdãos do STJ](https://github.com/danieleolivs/dataframe)

## 💭 Como Executar

Com o ambiente configurado, você pode rodar os scripts de análise. 

1.  **Execute o script Python:**
    ```bash
    python keywords.py
    ```

2. Passe, como forma de upload, a base de dados que deseja extrair as palavras-chave

## 📚 Referências

* **Manual de Padronização de Textos do STJ:** Disponível [neste link](https://www.tjes.jus.br/corregedoria/wp-content/uploads/2016/07/STJ-Manual-Padroniza%C3%A7%C3%A3o-Textos.pdf).
* **Pesquisa de Jurisprudência do STF:** Disponível [neste link](https://jurisprudencia.stf.jus.br/pages/search?base=acordaos&pesquisa_inteiro_teor=false&sinonimo=true&plural=true&radicais=false&buscaExata=true&page=1&pageSize=10&queryString=anatel&sort=date&sortBy=desc).

