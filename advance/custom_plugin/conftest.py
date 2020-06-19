import pytest
import requests

import os


def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 0:
        msg = "Congratulations! You test has completed, the result is *Pass*!"
    elif exitstatus == 1:
        msg = "Hmm..You test has completed, but the result is *Fail*! "
    else:
        msg = "Ops! something wrong happens during the test, and the test is not completed!"
    requests.post(os.getenv('SLACK_WEBHOOK_URL'), json={'text': msg})
