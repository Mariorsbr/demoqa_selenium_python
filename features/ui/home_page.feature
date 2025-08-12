Feature: Home Page

    Scenario: Check redirect
        Given I go to homepage 
        When I click Alerts, Frame & Windows
        Then I check message after redirection
        

            