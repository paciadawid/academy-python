from behave import given, when, then
from basics.classes import Student
from hamcrest import *


@given('I have a student "{name}" "{surname}" born in "{yob}"')
def step_impl(context, name, surname, yob):
    context.student = Student(name, surname, yob)


@then('my student in "{age}" years old')
def step_impl(context, age):
    assert context.student.get_age() == int(age)


@when('I change surname to "{surname}"')
def step_impl(context, surname):
    context.student.change_surname(surname)


@then('student\'s name is "{name}" "{surname}"')
def step_impl(context, name, surname):
    # assert context.student.print_full_name() == f"{name} {surname}"
    assert_that(context.student.name, equal_to(name))
    assert_that(context.student.surname, equal_to(surname))


@when('I add grade "{grade}"')
def step_impl(context, grade):
    context.student.add_grade(grade)


@then('average score is "{avg_score}"')
def step_impl(context, avg_score):
    assert_that(context.student.calculate_average(), equal_to(int(avg_score)))


@then('"{grade}" is in grade list')
def step_impl(context, grade):
    assert_that(context.student.grades, has_item(int(grade)))


@when("I add grades")
def step_impl(context):
    for row in context.table:
        context.student.add_grade(row["grade"])


@then('"{grades}" are in grade list')
def step_impl(context, grades):
    grades = list(map(int, grades.split(",")))
    assert_that(context.student.grades, equal_to(grades))
