# Aplicativo de ML QA com Streamlit e Cypress

Bem-vindo ao ML QA App! Este projeto combina o poder do Aprendizado de Máquina com o Streamlit para criar uma interface interativa e o Cypress para testes automatizados.

## Aprendizado de Máquina com o Streamlit

### Instalação
````
pip install -r requirements.txt
````

# Treinando o Modelo
1 - Abra o terminal e navegue até o diretório do projeto.
2 - Execute o aplicativo Streamlit:

````
streamlit run app.py
````
3 - O ML QA App será aberto em seu navegador padrão.

# Uso
1 - O aplicativo permite treinar um modelo de regressão linear simples com dados fornecidos.
2 - Insira um valor para X para fazer previsões.

# Testes Automatizados com o Cypress
## Instalação:
````
cd cypress
npm i
````

## Executando os Testes:
1 - Inicie o aplicativo Streamlit (se ainda não estiver em execução).
2 - Em uma nova janela do terminal, navegue até o diretório cypress.
3 - Execute o Cypress:
````
npx cypress open
````
4 - O Cypress Test Runner será aberto. Clique no arquivo de teste (app.spec.js) para executar os testes.

### Cenários de Teste
* **deveria clicar uma vez:** Verifica o comportamento de clicar no botão de previsão uma vez.
* **deveria clicar duaz vezes:** Testa o botão para dois cliques consecutivos.
* **deveria clicar três vezes:** Garante que o botão funcione conforme esperado com três cliques consecutivos.

# Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações de pull.

# Licença
Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.