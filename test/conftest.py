import os
import sys
import pytest
# app will be above
# add upper directory to the python searching dir
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app   

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
