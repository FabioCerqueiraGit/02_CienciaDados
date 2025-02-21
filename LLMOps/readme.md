# **LLM Sentiment Analysis Pipeline**

Este projeto é um pipeline de engenharia de dados que utiliza Large Language Models (LLMs) para análise de sentimentos em textos. Ele combina técnicas de LLMOps, processamento de linguagem natural (NLP) e implantação de modelos para criar uma solução escalável e eficiente.

---

## **Tecnologias Utilizadas**
- **Hugging Face Transformers**: Para utilizar modelos pré-treinados de NLP.
- **LangChain**: Para criar fluxos de trabalho complexos com LLMs.
- **FastAPI**: Para expor o modelo como uma API REST.
- **Docker**: Para containerizar a aplicação.
- **MLflow**: Para gerenciar o ciclo de vida do modelo.
- **GitHub Actions**: Para CI/CD (Integração Contínua e Entrega Contínua).

---

## **Funcionalidades**
1. Coleta e pré-processamento de dados de texto.
2. Análise de sentimentos utilizando modelos pré-treinados do Hugging Face.
3. Gerenciamento de modelos com MLflow (versionamento, monitoramento, etc.).
4. Implantação do modelo como uma API REST com FastAPI.
5. Integração com LangChain para fluxos de trabalho avançados.
6. Containerização da aplicação com Docker.
7. CI/CD automatizado com GitHub Actions.

---

## **Estrutura do Projeto**

├── data/ # Dados brutos e processados
├── models/ # Modelos treinados
├── src/
│ ├── api/ # Código da API (FastAPI)
│ ├── data_processing/ # Scripts de pré-processamento
│ ├── llm_ops/ # Configurações de LLMOps (MLflow)
│ ├── pipelines/ # Fluxos de trabalho com LangChain
├── tests/ # Testes unitários e de integração
├── Dockerfile # Configuração do Docker
├── requirements.txt # Dependências do projeto
├── README.md # Documentação do projeto
└── .github/workflows/ # Configurações de CI/CD (GitHub Actions)

