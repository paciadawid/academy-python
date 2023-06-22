Feature: Student


  Scenario: Check age
    Given I have a student "Tester" "Testowy" born in "1999"
    Then my student in "24" years old

  Scenario: Changing surname of student
    Given I have a student "Tester" "Testowy" born in "1999"
    When I change surname to "Nietestowy"
    Then student's name is "Tester" "Nietestowy"

  Scenario: Student with grade 5
    Given I have a student "Tester" "Testowy" born in "1999"
    When I add grade "5"
    Then average score is "5"
    And "5" is in grade list

  Scenario: Student with multiple grades
    Given I have a student "Tester" "Testowy" born in "1999"
    When I add grades
      | grade |
      | 4     |
      | 5     |
      | 5     |
    Then average score is "5"
    And "4,5,5" are in grade list