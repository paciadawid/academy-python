Feature: Logging to website

  @blocker
  Scenario: Successful login
    When I login using "seleniumremote@gmail.com"/"tester"
    Then I'm logged in

  @minor
  Scenario: Unsuccessful login
    When I login using "seleniumremote@gmail.com"/"testerrr"
    Then I see error message
