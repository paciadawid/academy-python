from behave import given, when, then

@given(u'I start test')
def step_impl(context):
    print(context.test)


@then(u'I see success')
def step_impl(context):
    assert True


@then("I see fail")
def step_impl(context):
    assert False


@when("I add values")
def step_impl(context):
    result = 0
    table = context.table
    for value in table.rows:
        result += int(value.cells[0])
    context.result = result


@then('my result is "{result}"')
def step_impl(context, result):
    assert int(result) == context.result, f"expected result: {result}, actual result {context.result}"


@when('I add "{x}" and "{y}"')
def step_impl(context, x, y):
    context.result = int(x) + int(y)
