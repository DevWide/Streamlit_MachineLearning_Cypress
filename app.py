import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def main():
    st.title('ML QA App')

    data = {'X': [1, 2, 3, 4, 5], 'y': [2, 4, 5, 4, 5]}
    df = pd.DataFrame(data)

    st.header('Treinamento do Modelo')
    X_train = df[['X']]
    y_train = df['y']
    model = train_model(X_train, y_train)

    st.header('Previsão')
    new_data = st.number_input('Insira um valor para o campo abaixo:', min_value=0)
    prediction = model.predict([[new_data]])

    st.write('A previsão é:', prediction[0])

if __name__ == '__main__':
    main()
