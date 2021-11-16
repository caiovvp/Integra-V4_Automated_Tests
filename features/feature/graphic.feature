    Feature: Show graphics and info as the dashboard loads

      Scenario: Show all information and Graphic accordingly
        Given user is logged in Integra
        Then show integrations information of the /html/body/main/div[1]
        Then show integrations information of the /html/body/main/div[3]
        And show integrations graphic

      Scenario: Show graphic according to the filter applied
        #Needs to add validation to the "period" filter on the graphic
        Scenario: Change graphic according to the time filter
          When time filter is chosen
          Then show integrations graphic
        Scenario: Change graphic according to the integration filter
          When integration filter is chosen
          Then show integrations graphic