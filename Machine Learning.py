# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:25:44 2020

@author: bruni
"""

import pandas as pd                     
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import pickle




df = pd.read_csv("Arquivo CSV")
atributos = ["Colunas de Atributos"]
atrib_prev = ["Coluna Preventiva"]
"Separa no X as Colunas do Atributo"
X = df[atributos].values
Y = df[atrib_prev].values 
split_test_size = 0.30
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, test_size = split_test_size, random_state = 42)
print("{0:0.2f}% nos dados de treino".format((len(X_treino)/len(df.index)) * 100))
print("{0:0.2f}% nos dados de teste".format((len(X_teste)/len(df.index)) * 100))

"Naive Bayes"
modelo1 = GaussianNB()
modelo1.fit(X_treino, Y_treino.ravel())
"Verificando Dados de Treino"
nb_predict_train = modelo1.predict(X_treino)
print("Exatidão: {0:.4f}".format(metrics.accuracy_score(Y_treino, nb_predict_train)))
print()
"Verificando Dados de Teste"
nb_predict_test = modelo1.predict(X_teste)
print("Exatidão (Accuracy): {0:.4f}".format(metrics.accuracy_score(Y_teste, nb_predict_test)))
print()


"Random Forest"
modelo2 = RandomForestClassifier(random_state = 42)
modelo2.fit(X_treino, Y_treino.ravel())
"Verificando Dados de Treino"
rf_predict_train = modelo2.predict(X_treino)
print("Exatidão (Accuracy): {0:.4f}".format(metrics.accuracy_score(Y_treino, rf_predict_train)))
"Verificando Dados de Teste"
rf_predict_test = modelo2.predict(X_teste)
print("Exatidão (Accuracy): {0:.4f}".format(metrics.accuracy_score(Y_teste, rf_predict_test)))
print()


"Teste de Regressão Logistica"
modelo3 = LogisticRegression(C = 0.7, random_state = 42)
modelo3.fit(X_treino, Y_treino.ravel())
"Verificando Dados de Teste"
lr_predict_test = modelo2.predict(X_teste)
print("Exatidão (Accuracy): {0:.4f}".format(metrics.accuracy_score(Y_teste, lr_predict_test)))
print()

"Salvando o Modelo"
filename = 'modelo3_treinado.sav'    
pickle.dump(modelo3, open(filename, 'wb'))


"Teste" "OBS: Modificar os x teste"
loaded_model = pickle.load(open(filename, 'rb'))
resultado1 = loaded_model.predict(X_teste[15].reshape(1, -1))
resultado2 = loaded_model.predict(X_teste[18].reshape(1, -1))
print(resultado1)
print(resultado2)

















