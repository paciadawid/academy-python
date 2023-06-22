Feature: Dummy feature

  @positive @premium
  Scenario: Positive scenario flow
    Given I start test
    Then I see success

  Scenario: Negative scenario flow
    Given I start test
    Then I see fail

  Scenario: Table flow
    Given I start test
    When I add values
      | value |
      | 2     |
      | 2     |
      | 3     |
    Then my result is "7"


  Scenario Outline: Calculator with examples
    Given I start test
    When I add "<x>" and "<y>"
    Then my result is "<result>"

    Examples:
      | x  | y   | result |
      | 1  | 1   | 2      |
      | 0  | 1   | 1      |
      | 11 | 111 | 122    |
