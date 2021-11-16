 Feature: Delete user

    Scenario: Create new user to be deleted
      Given user is logged in Integra
      And enter the users page
      And click on the add new user button
      When type all valid infos
      Then show message saying
        """
          {
            "message": "Usuário adicionado com sucesso",
            "web_ele": "/html/body/div[1]/div/div/div/h4"
          }
        """

    Scenario: Delete new user successfully
      Then find new user in users page
      And delete new user successfully

    Scenario: Log in with deleted user
      When try to log in with deleted user
      Then show message saying
      """
        {
          "message": "Nome de usuário ou senha incorretos",
          "web_ele": "/html/body/div/div/div[1]/div/form/div[2]"
        }
      """

