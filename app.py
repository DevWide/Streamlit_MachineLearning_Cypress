import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Função para treinar o modelo
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Função principal do aplicativo Streamlit
def main():
    st.title('ML QA App')

    # Carregue os dados (substitua pelo seu conjunto de dados)
    data = {'X': [1, 2, 3, 4, 5], 'y': [2, 4, 5, 4, 5]}
    df = pd.DataFrame(data)

    # Crie o modelo
    st.header('Treinamento do Modelo')
    X_train = df[['X']]
    y_train = df['y']
    model = train_model(X_train, y_train)

    # Interface para inserir dados de entrada
    st.header('Previsão')
    new_data = st.number_input('Insira um valor para X:', min_value=0)
    prediction = model.predict([[new_data]])

    # Exiba a previsão
    st.write('A previsão é:', prediction[0])

if __name__ == '__main__':
    main()
