import pytest

@pytest.mark.feature("length")
def test_length_m_to_cm(client):
    res = client.get("/api/convert?category=length&from=m&to=cm&value=1")
    assert res.status_code == 200
    assert res.get_json()["result"] == 100.0

@pytest.mark.feature("length")
def test_length_ft_to_m(client):
    res = client.get("/api/convert?category=length&from=ft&to=m&value=3.28084")
    assert res.status_code == 200
    data = res.get_json()
    assert abs(data["result"] - 1.0) < 1e-6
