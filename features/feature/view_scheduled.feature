    Feature: View scheduled processes on the Schedules tab

      Scenario: View scheduled processes successfully
        Given user is logged in Integra
        When go to the Schedules tab
        And select a schedule of the list
        Then show the list of processes found in that schedule
