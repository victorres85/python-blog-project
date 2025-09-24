# Blog API

A modern, AI-enhanced personal blog API built with FastAPI.

## Tests

This project uses pytest with async support and coverage reporting.

### Running Tests

```bash
# Run all tests
uv run pytest

# Run tests with coverage (minimum 80% required)
uv run pytest --cov=app

# Run tests with detailed coverage report
uv run pytest --cov=app --cov-report=term-missing

# Generate HTML coverage report
uv run pytest --cov=app --cov-report=html
# Open htmlcov/index.html in your browser

# Run specific test file
uv run pytest tests/test_main.py

# Run tests with verbose output
uv run pytest -v
```

### Test Structure

- `tests/conftest.py` - Test fixtures and configuration
- `tests/test_main.py` - Main application tests
- Coverage reports are generated in `htmlcov/` directory
- Minimum coverage threshold: 80%
