# import pytest

# @pytest.mark.feature("speed")
# def test_speed_mps_to_kmh(client):
#     res = client.get("/api/convert?category=speed&from=mps&to=kmh&value=1")
#     assert res.status_code == 200
#     assert res.get_json()["result"] == 3.6

# @pytest.mark.feature("speed")
# def test_speed_mph_to_mps(client):
#     res = client.get("/api/convert?category=speed&from=mph&to=mps&value=60")
#     assert res.status_code == 200
#     assert res.get_json()["result"] == 26.8224

# @pytest.mark.feature("speed")
# def test_speed_knot_to_kmh(client):
#     res = client.get("/api/convert?category=speed&from=knot&to=kmh&value=10")
#     assert res.status_code == 200
#     assert res.get_json()["result"] == 18.52

# # if the unit does not exist in this category, should return error code 400
# @pytest.mark.feature("speed")
# def test_invalid_speed_unit(client):
#     res = client.get("/api/convert?category=speed&from=mps&to=foo&value=10")
#     assert res.status_code == 400