 Feature: Change account password

    Background:
    Given user is on login page
    And click on the change password button
      Scenario: Account email exists
        When type a valid email on the email box
        And click on the request new password button
        Then show message saying
        """
          {
            "message": "Código enviado. Verifique seu e-mail",
            "web_ele": "/html/body/div[1]/div/div[1]/div/form/div[1]"
          }
        """

      Scenario: Account email doesnt exist
        When type an invalid email on the email box
        And click on the request new password button
        Then show message saying
        """
          {
            "message": "Não há nenhum usuário com esse email",
            "web_ele": "/html/body/div[1]/div/div[1]/div/form/div[1]"
          }
        """
