Feature: Student


  Scenario: Check age
    Given I have a student "Tester" "Testowy" born in "1999"
    Then my student in "24" years old

  Scenario: Changing surname of student
    Given I have a student "Tester" "Testowy" born in "1999"
    When I change surname to "Nietestowy"
    Then student's name is "Tester" "Nietestowy"
