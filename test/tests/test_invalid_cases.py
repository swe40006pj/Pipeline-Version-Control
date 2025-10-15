import pytest

@pytest.mark.feature("error")
def test_missing_value_error(client):
    res = client.get("/api/convert?category=length&from=m&to=cm")
    assert res.status_code == 400

@pytest.mark.feature("error")
def test_unknown_category_error(client):
    res = client.get("/api/convert?category=unknown&from=m&to=cm&value=1")
    assert res.status_code == 400

@pytest.mark.feature("error")
def test_invalid_unit_for_category_error(client):
    res = client.get("/api/convert?category=weight&from=m&to=cm&value=1")
    assert res.status_code == 400
