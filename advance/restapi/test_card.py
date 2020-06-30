import pytest

project_id = '060ED74A48F4992BA084F7BF6C9A652A'  # MicroStrategy Tutorial project in T619
cube_id = 'A9BBD4F945361D6C56DDF1B9310EFF6E'
name_id_code_message = [
    ("1Attribute", "AA09FB6C4306490F9445DF9386538831", 200, ""),
    ("noPageBy", "D327F1D14C8C4C39F03DEE841188E657", 500, "Hyper card layout property is invalid"),
    ("pageBy", "F034931F43AFA4B8DD766BA88E03F795", 500, "Hyper card layout property is invalid"),
    ("retail-sample-data.xls", "A9BBD4F945361D6C56DDF1B9310EFF6E", 500, "Hyper card layout property is invalid"),
    ("blank card", "5D6395B14D6DE5A8524D1182FBA8340A", 404, "No records available after applying filter"),
    ("1Metric", "41D21C684AA7290EF41AEF81E6B7A9D2", 404, "No records available after applying filter"),
]


@pytest.fixture(autouse=True)
def republish_cube_on_demand(client):
    client.publish_cube(project_id, cube_id=cube_id)


@pytest.mark.parametrize(argnames="name, report_id, code, message", argvalues=name_id_code_message)
def test_get_report_instance_card(client, name, report_id, code, message):
    resp = client.run(method='post', path=f'/reports/{report_id}/instances',
                      project_id=project_id, json={})
    instance_id = resp.json()['instanceId']
    resp = client.run(method="put", path=f'/reports/{report_id}/instances/{instance_id}/card',
                      project_id=project_id)
    if code != 200:
        assert resp.status_code == code, resp.status_code
        assert resp.json()["message"] == message, resp.json()
    else:
        assert resp.ok


@pytest.mark.parametrize(argnames="name,report_id, code, message", argvalues=name_id_code_message)
def test_get_report_instance_card_v2(client, name, report_id, code, message):
    resp = client.run(method='post', path=f'/v2/reports/{report_id}/instances',
                      project_id=project_id, json={})
    instance_id = resp.json()['instanceId']
    resp = client.run(method="get", path=f'/reports/{report_id}/instances/{instance_id}/card',
                      project_id=project_id)
    if code != 200:
        assert resp.status_code == code, resp.status_code
        assert resp.json()["message"] == message, resp.json()
    else:
        assert resp.ok
