import pytest

@pytest.mark.feature("volume")
def test_volume_l_to_ml(client):
    res = client.get("/api/convert?category=volume&from=L&to=ml&value=1")
    assert res.status_code == 200
    data = res.get_json()
    assert abs(data["result"] - 1000.0) < 1e-6

@pytest.mark.feature("volume")
def test_volume_invalid(client):
    res = client.get("/api/convert?category=volume&from=ml&to=kg&value=1")
    assert res.status_code == 400
