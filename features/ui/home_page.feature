Feature: Home Page

    Scenario Outline: Check redirect
        Given I go to homepage 
        When I click <header>
        Then I check message after redirection
        
        Examples: 
            | header |
            | Elements |
            | Forms |
            | Alerts, Frame & Windows |
            | Widgets |
            | Interactions |
            | Book Store Application |
            