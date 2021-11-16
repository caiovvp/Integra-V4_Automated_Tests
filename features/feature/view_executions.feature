    Feature: View executions of all processes

      Scenario: Log in Integra and go to Executions
        Given user is logged in Integra
        And go to the Executions tab

      Scenario: View executions of each process
        When select a process of the list
        Then show a list of all executions on that process

      Scenario: View all the integrations
        When go to all processes
        Then show the all the executions of all processes
        Scenario: Test if filter is working
          When choose a filter
          Then show only processes according with that filter
