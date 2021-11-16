    Feature: Create user inside Integra

        Scenario: Go to the add new user page
          Given user is logged in Integra
          And enter the users page
          And click on the add new user button

        Scenario: Type existent username
          When type an username that is already registered
          Then show message saying
          """
            {
              "message": "Existe um usuário com este username",
              "web_ele": "/html/body/main/form/div[4]/div/div[2]"
            }
          """

        Scenario: Type existent email
          When type an email that is already registered
          Then show message saying
          """
            {
              "message": "Existe um usuário com este email",
              "web_ele": "/html/body/main/form/div[4]/div/div[2]"
            }
          """

        Scenario: User successfully created
          When type all valid infos
          Then show message saying
          """
            {
              "message": "Usuário adicionado com sucesso!",
              "web_ele": "/html/body/div/div/div/div/h4"
            }
          """
          And find new user in users page

        Scenario: Delete new user
          Given enter the users page
          Then find new user in users page
          And delete new user successfully
