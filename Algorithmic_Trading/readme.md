# Algorithmic Trading com Hugging Face e LangChain

Este repositório apresenta um projeto de Algorithmic Trading utilizando as bibliotecas Hugging Face e LangChain. O objetivo é demonstrar como a Inteligência Artificial pode ser aplicada para analisar dados financeiros e tomar decisões de negociação automatizadas.

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **Hugging Face Transformers**: Utilizado para processamento de linguagem natural (NLP) aplicado à análise de notícias e sentimentos do mercado financeiro.
- **LangChain**: Para integração eficiente de modelos de linguagem na tomada de decisão.
- **Pandas e NumPy**: Para manipulação e análise de dados financeiros.
- **yFinance**: Para coleta de dados financeiros.
- **PyCharm**: Ambiente de desenvolvimento utilizado.

## Funcionalidades
- Coleta de dados financeiros de fontes públicas.
- Análise de sentimentos de notícias e redes sociais usando modelos da Hugging Face.
- Tomada de decisão automatizada baseada na análise de sentimentos e técnicas quantitativas.
- Execução de ordens simuladas para validação da estratégia.

## Estrutura do Projeto
```
algorithmic-trading/
│── data/              # Dados financeiros coletados
│── models/            # Modelos treinados ou baixados
│── notebooks/         # Notebooks para exploração dos dados
│── src/               # Código-fonte principal
│   │── data_loader.py  # Script para coleta de dados
│   │── sentiment_analysis.py  # Script para análise de sentimentos
│   │── trading_strategy.py  # Lógica de tomada de decisão
│   │── main.py         # Arquivo principal de execução
│── README.md          # Documentação do projeto
│── requirements.txt   # Lista de dependências do projeto
```

## Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/algorithmic-trading.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd algorithmic-trading
   ```
3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute o script principal:
   ```bash
   python src/main.py
   ```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

