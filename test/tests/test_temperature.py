import pytest

@pytest.mark.feature("temperature")
def test_temperature_c_to_f(client):
    res = client.get("/api/convert?category=temperature&from=C&to=F&value=0")
    assert res.status_code == 200
    assert res.get_json()["result"] == 32.0

@pytest.mark.feature("temperature")
def test_temperature_f_to_c(client):
    res = client.get("/api/convert?category=temperature&from=F&to=C&value=212")
    assert res.status_code == 200
    assert res.get_json()["result"] == 100.0

# if the convert does not exist, should return error code 400
@pytest.mark.feature("temperature")
def test_invalid_temperature_unit(client):
    res = client.get("/api/convert?category=temperature&from=K&to=C&value=100")
    assert res.status_code == 400
