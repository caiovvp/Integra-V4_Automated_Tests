  Feature: Change Account Password being logged in

    Scenario: Go to the user profile
      Given user is logged in Integra
      And enter the user profile

    Scenario: Password shorter than 8 characters
      When type invalid password
        """
          {"password": "senha"}
        """
      Then show message saying
        """
          {
            "message": "A senha deve conter pelo menos 8 caracteres",
            "web_ele": "/html/body/main/form/div[3]/div/div[2]"
          }
        """

    Scenario: Password without numbers
      When type invalid password
        """
          {"password": "senhalonga"}
        """
      Then show message saying
        """
          {
            "message": "A senha deve conter pelo menos um número",
            "web_ele": "/html/body/main/form/div[3]/div/div[2]"
          }
        """

    Scenario: Password without capital letters
      When type invalid password
        """
          {"password": "senha123"}
        """
      Then show message saying
        """
          {
            "message": "A senha deve conter pelo menos um caractere maiúsculo",
            "web_ele": "/html/body/main/form/div[3]/div/div[2]"
          }
        """

    Scenario: Password without special character
      When type invalid password
        """
          {"password": "Senha123"}
        """
      Then show message saying
        """
          {
            "message": "A senha deve conter pelo menos um caractere especial",
            "web_ele": "/html/body/main/form/div[3]/div/div[2]"
          }
        """

    Scenario: Passwords don't match
      When type different passwords
        """
          {"password": "Senha@123"}
        """
      Then show message saying
        """
          {
            "message": "As senhas devem ser iguais",
            "web_ele": "/html/body/main/form/div[3]/div/div[2]"
          }
        """

    Scenario: Change password successfully
      When type correct password
        """
          {"password": "Senha@123"}
        """
      Then show message saying
        """
          {
            "message": "Senha alterada com sucesso!",
            "web_ele": "/html/body/div/div/div/div/h4"
          }
        """
      And log out of Integra

    Scenario: Log in with new password
      When try to log in with the new password
        """
          {
            "user": "integra_tester",
            "password": ["WrongPassword@123", "Senha@123"]
          }
        """
      Then the dashboard page should open
