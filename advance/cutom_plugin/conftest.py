import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    slacker_mark = item.get_closest_marker('slacker')
    if slacker_mark:
        if rep.when == "call" and rep.failed:
            print('Post message at slack channel: {} and mention: {} about '
                  'this test case: {} failure successfully!'.format('GTA', slacker_mark.kwargs.get('mail'), item.name))
