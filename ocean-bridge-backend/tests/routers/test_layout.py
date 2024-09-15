import pytest
from httpx import Response

from app.models.layout.layout import Layout


workflow_step_id = [
    "69fc26ea-60db-4bbe-8cef-bc1058c2ce57",
    "3f4f0137-d0af-4b68-8ddb-cdae51a704d6",
    "1626af61-eb16-4058-bb05-d449b2b3acc7",
    "cd462a3c-d474-498a-bdb3-d849ffe5865",
    "62e68aa9-d95a-411a-a4fb-90168b77a438",
    "435b288b-456f-4c12-b72a-0ccf842cc3fd",
    "e299365a-f960-495f-a980-5ab41a97e229",
    "e5813c78-da5a-435a-9563-17e72b4efac4",
]

@pytest.mark.anyio
@pytest.mark.parametrize("workflow_step_id", workflow_step_id)
async def test_get_layout(async_client, workflow_step_id):
    response: Response = await async_client.post(
        f"/V1/layout",
        headers={"Authorization": "test_api_key"},
        json={"workflow_step_id": workflow_step_id}
    )

    assert response.status_code == 200
    assert "set-cookie" in response.headers

    data = Layout.parse_obj(response.json())
    assert isinstance(data, Layout)
