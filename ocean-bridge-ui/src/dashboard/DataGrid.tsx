import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridValueGetterParams } from '@mui/x-data-grid';
import Link from "@mui/material/Link";
import { Button, ButtonGroup } from '@mui/material';
import ColumnData from '../testdata/DataGrid.json'
import { ContactSupportOutlined, Cookie } from '@mui/icons-material';
import { useGetDataGrid, useGetDataGridData, useUpdateDataGridData } from '../api/Workflow/Workflow.hooks';

//dataGrid.DataGrid_ToolbarItems.map((DataGrid_ToolbarItem) => {}

function getType(column)
{
  if (column.columnType ==='number')
  {
    return 'number'
  }
  if (column.columnType ==='date')
  {
    return 'date'
  }
  if (column.columnType ==='datetime')
  {
    return 'dateTime'
  }
  if (column.columnType ==='boolean')
  {
    return 'boolean'
  }
  if (column.columnType ==='actions')
  {
    return 'actions'
  }
  if (column.editor ==='DropDownList' || column.columnType === 'DropDownList' )
  {
    return 'singleSelect'
  }
  else 
  {
    return 'string'
  }
  
}

function getValueGetter(type)
{
  if (type == 'date')
  {
    return ({ value }) => value && new Date(value)
  }
}

function getValueOptions(type) {
  if (type == 'singleSelect')
  {
    return ['abc', 'def', 'hij']
  }
}


function createColumns(columnsData) {
  const newColumns: GridColDef[] = []
  columnsData.columns.map((column) => (newColumns.push(
    {
      field: column.field,
      headerName: column.title,
      width: column.width * 1.25,
      editable: column.iseditable,
      type: getType(column),
      valueGetter: getValueGetter(getType(column)),
      valueOptions: getValueOptions(getType(column))

    }
    )))

  return newColumns;
  
}

function createColumnVisibilityModel(columnsData) {
  const columnVisibilityModel = {};

  columnsData.columns.forEach((column) => {
    columnVisibilityModel[column.field] = column.isvisible === 1 ? true : false;
  });

  return columnVisibilityModel;
}

export default function WorkflowStepColumns(props) {
  const { dataGridId } = props;

  const [columns, setColumns] = React.useState<GridColDef[]>([]);
  const [data, setData] = React.useState('');
  const [dataToUpdate, setDataToUpdate] = React.useState({});
  const [newDataValue, setNewDataValue] = React.useState('');
  const [columnVisibilityModel, setColumnVisibilityModel] = React.useState({});

  const { isLoading: dataGridLoading, data: columnsData, refetch } = useGetDataGrid(dataGridId)
  const { isLoading: dataGridDataLoading, data: dataGridData} = useGetDataGridData(dataGridId)
  const mutationUpdateDataGridData = useUpdateDataGridData([dataToUpdate[1], dataToUpdate[0], dataToUpdate[2], dataToUpdate[3]]);


  React.useEffect(() => {

    if (columnsData)
    {
      setColumns(createColumns(columnsData));
      setData(dataGridData)  
      setColumnVisibilityModel(createColumnVisibilityModel(columnsData));
    }
  },[columnsData, dataGridId])

  const handleRowUpdate = (updatedRow) => {
     columns.map((column) => {
      if (updatedRow[`${column.field}_OriginalColumnValue`] !== updatedRow[column.field] && updatedRow[`${column.field}_OriginalColumnValue`] !== '~')
      {
        const newValue = updatedRow[column.field];
        const originalColumnValue = updatedRow[`${column.field}_OriginalColumnValue`];
        const dataGroupColumnId = updatedRow[`${column.field}_DataGroupColumnID`];
        mutationUpdateDataGridData.mutate([dataGroupColumnId, updatedRow.OrderID, originalColumnValue, newValue])
        return dataGridData
      }
     }
     )
    }

  const handleEditCellChange = (params) => {
    const { id, field, value } = params;
    if (value === undefined || value === '') {
      // If the newly edited value is null, set it back to the original value
      const updatedData = data.map((row) =>
        row.OrderID === id ? { ...row, [field]: params.props.value } : row
      );
      setData(updatedData);
    } else {
      // Update the data with the new value
      const updatedData = data.map((row) => {

        if (row.OrderID === id)
        {
          return { ...row, [field]: value }
        }
        else 
        {
          return row
        }
      });
      setData(updatedData);
      //mutationUpdateDataGridData.mutate([params.row.customer_po]);
    }
  };
  let rows = []

  if (dataGridId) {
    return (
    <Box sx={{ height: 400, width: '100%' }}>
      <DataGrid
        columnVisibilityModel={columnVisibilityModel}
        onCellEditStop={handleEditCellChange}
        processRowUpdate={(updatedRow, originalRow) => 
          handleRowUpdate(updatedRow)
        }
        onProcessRowUpdateError={()=> console.log('failed')}
        getRowId={(row) => row.OrderID}
        rows={data}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 5,
            },
          },
        }
      }
        pageSizeOptions={[5]}
        checkboxSelection
        disableRowSelectionOnClick
      />
    </Box>
  );
}
}