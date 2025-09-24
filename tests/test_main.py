import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient


def test_health_endpoint_sync(client: TestClient) -> None:
    """Test the /health endpoint returns the expected response (sync)."""
    response = client.get("/health")
    assert response.status_code == 200
    # Fix: Health endpoint returns a tuple, not a JSON object
    assert response.json() == ["OK", 200]


@pytest.mark.asyncio
async def test_health_endpoint_async(async_client: AsyncClient) -> None:
    """Test the /health endpoint returns the expected response (async)."""
    response = await async_client.get("/health")
    assert response.status_code == 200
    assert response.json() == ["OK", 200]


@pytest.mark.asyncio
async def test_docs_endpoint_in_debug(async_client: AsyncClient) -> None:
    """Test that docs are available in debug mode."""
    response = await async_client.get("/docs")
    assert response.status_code == 200
    assert "swagger" in response.text.lower()


def test_app_metadata(client: TestClient) -> None:
    """Test that the app has correct metadata."""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    openapi_data = response.json()
    assert openapi_data["info"]["title"] == "Personal Blog API"
    assert openapi_data["info"]["version"] == "1.0.0"
