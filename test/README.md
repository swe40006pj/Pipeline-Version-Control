# Flask Unit Converter — Test Branch

This branch stores all testing logic for the Flask Unit Converter project.

## Folder Structure
- `tests/` — pytest test files, organized by feature
- `conftest.py` — Flask test client fixture
- `pytest.ini` — pytest configuration
- `requirements.txt` — dependencies for testing

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run all tests:
   ```bash
   pytest
3. To test only one feature
   ```
   pytest -k "length"

## Notes

This branch should not contain .github/workflows/.
It is imported by develop workflows for both PR testing and regression testing.

   