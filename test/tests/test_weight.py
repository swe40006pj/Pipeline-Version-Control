import pytest

@pytest.mark.feature("weight")
def test_weight_kg_to_lb(client):
    res = client.get("/api/convert?category=weight&from=kg&to=lb&value=1")
    assert res.status_code == 200
    data = res.get_json()
    assert abs(data["result"] - 2.20462) < 1e-3

# if the convert does not exist, should return error code 400
@pytest.mark.feature("weight")
def test_weight_invalid_unit(client):
    res = client.get("/api/convert?category=weight&from=g&to=stone&value=1")
    assert res.status_code == 400
