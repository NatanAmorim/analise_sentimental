# Leia me

- [Sobre](#sobre)
- [Requisitos](#requisitos)
- [Bibliotecas](#bibliotecas)
- [Pull Requests](#pull-requests)
- [Corrigindo Bugs](#corrigindo-bugs)
- [Criadores](#criadores)
- [Referências](#referencias)

## Sobre

Esse é um repositório para compartilhar um trabalho em Python 3 de análise sentimental.

* Testado em Python 3.8.2

* Objetivos: 
  * Web Scraping
  * Análise sentimental 
    * Classificação de texto usando Naive Bayes (Algoritimo de aprendizado de máquina supervisionado.)
  * plotagem de gráficos.

* Não foi criado para uso profissional, para isso precisa de melhorias, por exemplo:
  * Alguma coisa como "map reduce" para processar big data.
  * melhor classificação de dados como verbos, adjetivos, substantivos...
    * Polissemia (muitos significados) é um problema
    * Sinônimos também podem dificultar a analise
    * Se tiver interesse fazer uma melhor classificação de uma olhada em [openWordnet-PT](https://github.com/own-pt/openWordnet-PT)
  * melhor otimização dos scripts para processar mais rápidamente.

## Requisitos

* Python 3.5+ / Anaconda 3 (opcional)
* Jupyter Notebook
* Baixe os dados para o treinamento da IA em [Portuguese Tweets for Sentiment Analysis](https://www.kaggle.com/augustop/portuguese-tweets-for-sentiment-analysis), descompacte os arquivos, copie um dos arquivos [ Train50, Train100, Train200, Train300, Train400, Train500 ] de dentro da pasta TrainingDatasets/ renomeie esse arquivo para 'dados_para_treinamento.csv' e cole nas pastas Scripts/ e GUI/

## Bibliotecas 

- Essas são as bibliotecas de Python 3 usadas neste trabalho.
- Comando para atualizar o pip  `pip3 install --upgrade pip`

| Biblioteca | Comando para Instalar |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| [Jupyter Notebook](https://jupyter.readthedocs.io/en/latest/install.html) | `pip3 install jupyter` |
| [Numpy](https://pypi.org/project/numpy/) | `pip3 install numpy` |
| [pandas](https://pypi.org/project/pandas/) | `pip3 install pandas` |
| [requests](https://pypi.org/project/requests/) | `pip3 install requests` |
| [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) | `pip3 install beautifulsoup4` |
| [scipy](https://pypi.org/project/scipy/) | `pip install scipy` |
| [Unidecode](https://pypi.org/project/Unidecode/) | `pip install Unidecode` |
| [scikit-learn](https://pypi.org/project/scikit-learn/) | `pip install scikit-learn` |
| [nltk](https://pypi.org/project/nltk/) | `pip install nltk` |
| [Matplotlib](https://pypi.org/project/matplotlib/) | `pip3 install matplotlib` |
| [Seaborn](https://pypi.org/project/seaborn/) | `pip3 install seaborn` |
| [PyQt5](https://pypi.org/project/PyQt5/) | `pip install PyQt5` |

## Pull Requests

1. Descreva de forma clara o que deve ser consertado ou adicionado.
2. Tente minimizar a quantidade de alterações no código, use estilos/funções já existentes.

## Corrigindo Bugs

Para facilitar a resposta a problemas por favor siga essas orientações quando for explicar o problema.

1. Descreva de forma clara o que deve ser consertado, se for relevante anexe log/screenshots.
2. Descreva como os desenvolvedores podem reproduzir o bug para que possa ser consertado.

## Referências
    
- [Processamento de Linguagem Natural - Introdução](http://professor.ufabc.edu.br/~jesus.mena/courses/pln-2q-2019/PLN-aula01.pdf)
- [Processamento de Linguagem Natural - Expressões regulares](http://professor.ufabc.edu.br/~jesus.mena/courses/pln-2q-2019/PLN-aula02.pdf)
- [Processamento de Linguagem Natural -  Normalização de texto](http://professor.ufabc.edu.br/~jesus.mena/courses/pln-2q-2019/PLN-aula03.pdf)
- [Natural Language Processing in Python](https://www.youtube.com/watch?v=xvqsFTUsOmc&t=3685s)
- [NLP in python tutorial](https://github.com/adashofdata/nlp-in-python-tutorial)
- [Classificação de textos em python](https://www.linkedin.com/pulse/classifica%C3%A7%C3%A3o-de-textos-em-python-luiz-felipe-araujo-nunes/)
- [Portuguese Tweets for Sentiment Analysis](https://www.kaggle.com/augustop/portuguese-tweets-for-sentiment-analysis)
- [NLP Sentiment Analysis on IMDB Review](https://www.kaggle.com/crissilvaeng/nlp-sentiment-analysis-on-imdb-review/data)
- [Machine Learning Tutorial Python - 14: Naive Bayes Part 1](https://www.youtube.com/watch?v=PPeaRc-r1OI)
- [Machine Learning Tutorial Python - 15: Naive Bayes Part 2](https://www.youtube.com/watch?v=nHIUYwN-5rM)
- [Convert a collection of text documents to a matrix of token counts](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)


## Criadores

* Natan Amorim Souza Gomes de Moraes
* Andrey Cardoso Gil
