import requests
import pytest

# Update your aba host ip here
aba_host = '10.244.23.10'

# Canonical REST API URL
ABA_URL = f"http://{aba_host}:8080/MicroStrategyLibrary/api"


@pytest.fixture()
def client():
    return RestRunner(root_url=ABA_URL,
                      username='administrator',
                      password='')


class RestRunner(object):
    AUTH_LDAP = 16
    AUTH_STANDARD = 1

    def __init__(self, root_url, username, password, mode=AUTH_STANDARD, locale=None):
        self.s = requests.session()
        self.root_url = root_url.rstrip('/')
        self.reason = ''
        self.resp = None
        self.username = username
        self.password = password
        self.authenticated = False
        self.mode = mode
        self.locale = locale

    def auth(self):
        json_body = {'username': self.username,
                     'password': self.password,
                     "loginMode": self.mode,
                     }
        if self.locale:
            json_body.update({'numberLocale': self.locale,
                              "displayLocale": self.locale,
                              "messagesLocale": self.locale,
                              "metadataLocale": self.locale,
                              "warehouseDataLocale": self.locale
                              })
        resp = self.s.post(self.root_url + '/auth/login',
                           json=json_body)
        if resp.ok:
            self.s.headers.update(
                {'X-MSTR-AuthToken': resp.headers['X-MSTR-AuthToken']})
            self.authenticated = True
            return resp
        else:
            raise RuntimeError(
                'Error when get authentication token, response: \n{}'.format(
                    resp.content))

    def run(self, method, path, project_id=None, **kwargs):
        method = method.upper()
        path = path if path.startswith("/") else "/" + path
        url = self.root_url + path
        req = requests.Request(method, url, **kwargs)
        if not self.authenticated:
            self.auth()
        if project_id:
            self.s.headers.update({'X-MSTR-ProjectID': project_id})
        prepped = self.s.prepare_request(req)
        resp = self.s.send(prepped)
        self.resp = resp
        if not resp.ok:
            print(
                'Get response code {}, response: \n{}'.format(resp.status_code,
                                                              resp.content))
        return resp

    def publish_cube(self, project_id, cube_id):
        return self.run(method='post', path='/cubes/{}/'.format(cube_id),
                        project_id=project_id)
