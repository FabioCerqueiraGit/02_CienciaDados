# Fraud Detection Project

Este projeto visa detectar fraudes em transações financeiras utilizando técnicas de Machine Learning com o Hugging Face, LangChain e PyTorch. Através de um pipeline eficiente, o sistema analisa dados financeiros e realiza a previsão de possíveis fraudes. O modelo é treinado e avaliado usando o Hugging Face Hub e a framework LangChain para facilitar a integração com APIs e sistemas externos.

## Tecnologias Utilizadas

- **Hugging Face**: Utilizado para carregar e treinar modelos de aprendizado de máquina, bem como para interagir com o Hugging Face Hub.
- **PyTorch**: Framework para o treinamento e avaliação de modelos de Machine Learning.
- **LangChain**: Para orquestrar o fluxo de trabalho de dados e comunicação entre diferentes sistemas, facilitando o processo de detecção de fraudes.
- **huggingface-hub**: Para gerenciamento de modelos e integração com a plataforma Hugging Face.
- **torch**: Framework de deep learning para treinamento de redes neurais.
- **pandas**: Para manipulação de dados e pré-processamento.
- **scikit-learn**: Para avaliação de performance do modelo.

## Funcionalidades

- **Detecção de Fraudes**: Utiliza um modelo de aprendizado supervisionado para classificar transações como fraudulentas ou legítimas.
- **Integração com LangChain**: O LangChain é utilizado para orquestrar a interação do modelo com APIs externas que podem fornecer dados adicionais, como histórico de transações ou informações de usuários.
- **Treinamento de Modelo**: O projeto usa PyTorch para treinar o modelo em um conjunto de dados de transações financeiras.
- **Interface com Hugging Face Hub**: O modelo treinado é carregado e armazenado no Hugging Face Hub para fácil acesso e versionamento.

## Estrutura do Projeto

- `data/`: Contém os dados de transações financeiras utilizados no treinamento.
- `models/`: Scripts de treinamento e salvamento do modelo.
- `notebooks/`: Jupyter notebooks para análise e visualização de dados.
- `src/`: Código-fonte do sistema de detecção de fraudes, incluindo integração com LangChain.
- `requirements.txt`: Arquivo com as dependências do projeto.

## Instalação

Clone este repositório:

```bash
git clone https://github.com/fabiocerqueiragit/fraud_detection.git
cd fraud-detection

Instale as dependências:

pip install -r requirements.txt

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).


