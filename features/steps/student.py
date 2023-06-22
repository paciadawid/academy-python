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
