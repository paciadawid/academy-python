from hamcrest import *
from behave import given, when, then


@when('I login using "{email}"/"{password}"')
def step_impl(context, email, password):
    context.login_page.login_with_email(email, password)


@then("I'm logged in")
def step_impl(context):
    context.login_page.check_if_logged_in()


@then("I see error message")
def step_impl(context):
    context.login_page.check_error_message()
