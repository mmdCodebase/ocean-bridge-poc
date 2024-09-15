import * as React from 'react';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ListSubheader from '@mui/material/ListSubheader';
import DashboardIcon from '@mui/icons-material/Dashboard';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import PeopleIcon from '@mui/icons-material/People';
import BarChartIcon from '@mui/icons-material/BarChart';
import LayersIcon from '@mui/icons-material/Layers';
import AssignmentIcon from '@mui/icons-material/Assignment';
import data from '../testdata/initialCall.json';  
import workflowStepsTest from '../testdata/WorkflowStepSimple.json'

export function WorkflowSteps(props) {
  const [workflowColumns, setWorkflowColumns ] = React.useState();
  const { workflowSteps, dataGrids, setDataGrids } = props;

  function workflowStepClicked(workflowStep) {
    console.log(workflowStep.DataGridID);
    setWorkflowColumns(workflowStep.WorkflowStepColumns);
    setDataGrids(workflowStep.DataGridID);
  }
      return (
      <React.Fragment>
        Workflow Steps
      {workflowStepsTest.map((workflowStep) => (
        <ListSubheader component="div">
          <ListItemButton key={workflowStep.WorkflowStepID} onClick={() => workflowStepClicked(workflowStep)}>
            <ListItemIcon>
              <PeopleIcon />
            </ListItemIcon>
            <ListItemText secondary={workflowStep.WorkflowStepName} />
          </ListItemButton>
        </ListSubheader>
      ))}
    </React.Fragment>
    )
  };