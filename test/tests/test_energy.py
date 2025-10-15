import pytest

@pytest.mark.feature("energy")
def test_energy_kcal_to_kj(client):
    res = client.get("/api/convert?category=energy&from=kcal&to=kJ&value=1")
    assert res.status_code == 200
    data = res.get_json()
    assert abs(data["result"] - 4.184) < 1e-6
