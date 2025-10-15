import pytest

@pytest.mark.feature("area")
def test_area_m2_to_ft2(client):
    res = client.get("/api/convert?category=area&from=m2&to=ft2&value=1")
    assert res.status_code == 200
    data = res.get_json()
    assert abs(data["result"] - 10.7639) < 0.01
