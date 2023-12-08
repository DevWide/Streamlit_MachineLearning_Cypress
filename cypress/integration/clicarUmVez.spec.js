describe('ML QA App', function () {
    it('Carrega o aplicativo', function () {
      cy.visit('http://localhost:8501');        
      cy.contains('ML QA App').should('exist');
    });
  
    it('Realiza uma previsão', function () {
      cy.visit('http://localhost:8501');  
      cy.get('#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-91z34k.egzxvld4 > div:nth-child(1) > div > div:nth-child(4) > div > div.css-1rvyln1.e1jwn65y3 > div.css-76z9jo.e1jwn65y2 > button.step-up.css-1r8izn3.e1jwn65y1').click();
      cy.contains('A previsão é:').should('exist');      

    });
  });
  