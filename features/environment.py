


def before_scenario(context, scenario):
    context.test = "Test"
    print(scenario.status)
