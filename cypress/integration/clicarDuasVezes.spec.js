describe('ML QA App', function () {
    it('Carrega o aplicativo', function () {
      cy.visit('http://localhost:8501');  // Certifique-se de ajustar a URL conforme necessário
  
      // Adicione comandos do Cypress para interagir com o aplicativo
      // Por exemplo, você pode verificar se o título do aplicativo está correto
      cy.contains('ML QA App').should('exist');
    });
  
    it('Realiza uma previsão', function () {
      cy.visit('http://localhost:8501');  // Certifique-se de ajustar a URL conforme necessário

      for (let i = 0; i < 2; i++) {
        cy.get('#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-91z34k.egzxvld4 > div:nth-child(1) > div > div:nth-child(4) > div > div.css-1rvyln1.e1jwn65y3 > div.css-76z9jo.e1jwn65y2 > button.step-up.css-1r8izn3.e1jwn65y1').click();
        cy.contains('A previsão é:').should('exist');
        }     
    });
  });
  