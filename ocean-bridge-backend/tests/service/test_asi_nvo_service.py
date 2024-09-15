import pytest

from app.service import asi_nvo

from app.models.tree import WorkflowTrees
from app.models.data import Data
from app.models.layout.layout import Layout


workflow_id = ["9e40de8b-7a4e-11ee-9aff-00505686a13d"]
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
@pytest.mark.parametrize("workflow_id", workflow_id)
async def test_navigation_tree(async_client, workflow_id):
    response = asi_nvo.get_navigation_tree(workflow_id=workflow_id)

    if response is not None:
        navigation_tree = WorkflowTrees.parse_obj(response['tree'])

        assert isinstance(navigation_tree, WorkflowTrees)
        assert hasattr(navigation_tree, "tree")
        assert isinstance(navigation_tree.tree, list)
    else:
        raise ValueError("Workflow tree data is None in the response.")


@pytest.mark.anyio
@pytest.mark.parametrize("workflow_step_id", workflow_step_id)
async def test_layout(async_client, workflow_step_id):
    response = asi_nvo.get_layout(workflow_step_id=workflow_step_id, key_value='')

    if response is not None:
        layout = Layout.parse_obj(response['layout'])

        assert isinstance(layout, Layout)
        assert hasattr(layout, "div_list")
        assert isinstance(layout.div_list, list)
        assert hasattr(layout, "data_grids")
        assert isinstance(layout.data_grids, list)
        assert hasattr(layout, "fields")
        assert isinstance(layout.fields, list)
    else:
        raise ValueError("Layout data is None in the response.")


@pytest.mark.anyio
@pytest.mark.parametrize("workflow_step_id", workflow_step_id)
async def test_datagrid_data(async_client, workflow_step_id):
    response = asi_nvo.get_datagrid_data(
        workflow_step_id=workflow_step_id,
        form_id='',
        datagrid_id='',
        key_id='',
        fetch_type='PageDataWithDataGridData'
    )

    if response is not None:
        datagrid_data = Data.parse_obj(response['datagrid'])

        assert isinstance(datagrid_data, Data)
        assert hasattr(datagrid_data, "fields")
        assert isinstance(datagrid_data.fields, list)
        assert hasattr(datagrid_data, "data_grids")
        assert isinstance(datagrid_data.data_grids, list)
    else:
        raise ValueError("Datagrid data is None in the response.")
