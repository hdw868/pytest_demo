from pytest_bdd import given, when, then, scenario


@scenario(
    'outline.feature',
    'Outlined given, when, then',
    example_converters=dict(start=int, eat=float, left=str)
)
def test_outlined():
    pass


@given('there are <start> cucumbers')
def start_cucumbers(start):
    assert isinstance(start, int)
    return dict(start=start)


@when('I eat <eat> cucumbers')
def eat_cucumbers(start_cucumbers, eat):
    assert isinstance(eat, float)
    start_cucumbers['eat'] = eat


@then('I should have <left> cucumbers')
def should_have_left_cucumbers(start_cucumbers, start, eat, left):
    assert isinstance(left, str)
    assert start - eat == int(left)
    assert start_cucumbers['start'] == start
    assert start_cucumbers['eat'] == eat