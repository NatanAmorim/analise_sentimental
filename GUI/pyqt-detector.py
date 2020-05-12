import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
import re # Regex (expressão regular)
from unicodedata import normalize # utíl para tratamento de texto e compatibilidade
import pandas as pd
import nltk # Ferramentas de PLN
import sklearn # Ferramentas de aprendizado de máquina
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes

# https://www.kaggle.com/augustop/portuguese-tweets-for-sentiment-analysis
arquivo = ('dados_para_treinamento.csv')

df_tweets = pd.read_csv(arquivo, sep=";", usecols=['tweet_text','sentiment'],
                        index_col=None, header=0, dtype={"sentiment":"int16"})

# Deixando tudo em minúsculo
df_tweets['tweet_text'] = df_tweets['tweet_text'].str.lower()
# Removendo tudo entre []
df_tweets['tweet_text'] = df_tweets['tweet_text'].replace(to_replace='\[.*?\]', value='', regex=True)
# remover links
df_tweets['tweet_text'] = df_tweets['tweet_text'].replace(to_replace='https?://[A-Za-z0-9./]+', value='', regex=True)
df_tweets['tweet_text'] = df_tweets['tweet_text'].replace(to_replace='http?://[A-Za-z0-9./]+', value='', regex=True)
df_tweets['tweet_text'] = df_tweets['tweet_text'].replace(to_replace='wwww?://[A-Za-z0-9./]+', value='', regex=True)
df_tweets['tweet_text'] = df_tweets['tweet_text'].replace(to_replace='ftp?://[A-Za-z0-9./]+', value='', regex=True)
# Removendo números
df_tweets['tweet_text'] = df_tweets['tweet_text'].replace(to_replace='\d+', value='', regex=True)
# Removendo #rashtags
df_tweets['tweet_text'] = df_tweets['tweet_text'].replace(to_replace=r'(\#\w+)', value='', regex=True)
# Removendo @Mentions
df_tweets['tweet_text'] = df_tweets['tweet_text'].replace(to_replace=r'(\@\w+)', value='', regex=True)
# Removendo a pontuação (EX: "!?.,/|#$%¨&")
df_tweets['tweet_text'] = df_tweets['tweet_text'].replace(to_replace=r'[^\w\s]', value='', regex=True)
# Removendo acentuação
df_tweets['tweet_text'] = df_tweets['tweet_text'].str.normalize('NFKD').str.encode('ASCII', errors='ignore').str.decode('UTF-8')

# Uma stopword pode ser considerada uma palavra irrelevante para a análise
nltk.download('stopwords')
# RSLP(Removedor de Sufixos da Língua Portuguesa)
nltk.download('rslp')

# Criando uma lista de stopWords
stopWords = set(nltk.corpus.stopwords.words('portuguese'))
vetorizador = CountVectorizer(stop_words=stopWords)

X = vetorizador.fit_transform(df_tweets.tweet_text)
y = df_tweets.sentiment

# Separa em amostras de treino -> X_train, y_train e amostras de teste -> X_test y_test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

modelo = naive_bayes.MultinomialNB()
modelo.fit(X_train, y_train)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Detecção de emoções") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Frase:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('Detectar Emoção', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)        

    def clickMethod(self):
        frases = list()
        texto = self.line.text()
        # Deixando tudo em minúsculo
        texto.lower()
        # Removendo tudo entre []
        texto = re.sub(r'\[.*?\]', '', texto)
        # remover links
        texto = re.sub(r'https?://[A-Za-z0-9./]+', '', texto)
        texto = re.sub(r'http?://[A-Za-z0-9./]+', '', texto)
        texto = re.sub(r'ftp?://[A-Za-z0-9./]+', '', texto)
        texto = re.sub(r'ftps?://[A-Za-z0-9./]+', '', texto)
        texto = re.sub(r'wwww?://[A-Za-z0-9./]+', '', texto)
        # Removendo números
        texto = re.sub(r'\d+', '', texto)
        # Removendo #rashtags
        texto = re.sub(r'(\#\w+)', '', texto)
        # Removendo @Mentions
        texto = re.sub(r'(\@\w+)', '', texto)
        # Removendo a pontuação (EX: "!?.,/|#$%¨&")
        texto = re.sub(r'[^\w\s]', '', texto)
        # Removendo acentuação
        texto= normalize('NFKD', texto).encode('ASCII','ignore').decode('ASCII')
        
        frases.append(self.line.text())

        frases_count = vetorizador.transform(frases)
        teste = modelo.predict(frases_count)
        if (teste[0] == 1):
            sentimento = "Emoção Positiva" + " " + "\U0001f642"
        elif (teste[0] == 0):
            sentimento = "Emoção Negativa" + " " + "\U0001f641"
        else:
            sentimento = "None" + " " + "\U0001f610"
        msg = QMessageBox()
        msg.setWindowTitle("Emoção detectada")
        msg.setText('"' + frases[0] + '"')
        msg.setInformativeText(sentimento)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )