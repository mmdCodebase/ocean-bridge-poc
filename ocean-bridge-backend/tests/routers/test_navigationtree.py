import pytest
from httpx import Response

from app.models.tree import WorkflowTrees


workflow_id = ["9e40de8b-7a4e-11ee-9aff-00505686a13d"]

@pytest.mark.anyio
@pytest.mark.parametrize("workflow_id", workflow_id)
async def test_get_navigationtree(async_client, workflow_id):
    response: Response = await async_client.get(
        f"/V1/navigationtree/{workflow_id}",
        headers={"Authorization": "test_api_key"}
    )

    assert response.status_code == 200
    assert "set-cookie" in response.headers

    data = WorkflowTrees.parse_obj(response.json())
    assert isinstance(data, WorkflowTrees)
