Feature: Logging to website

  @blocker
  Scenario: Successful login
    When I login using "seleniumremote@gmail.com"/"tester"
    Then I see error message

  @minor
  Scenario: Unsuccessful login
    When I login using "seleniumremote@gmail.com"/"testerrr"
    Then I see error message

  @minor
  Scenario: Fail flow
    When I login using "seleniumremote@gmail.com"/"testerrr"
    Then I'm logged in