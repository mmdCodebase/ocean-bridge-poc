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
import { WorkflowStepGroups } from './WorkflowStepGroups.tsx';
import List from '@mui/material/List';
import { useGetWorkflowSteps } from '../api/Workflow/Workflow.hooks';

export default function Workflows(props) {
  const {data, dataGrids, setDataGrids } = props;
  const [workflowStepId, setWorkflowStepId] = React.useState('')

  const { isLoading, data: workflowStepsData, refetch } = useGetWorkflowSteps(workflowStepId);

  function handleWorkflowStepClick(WorkflowStepID) {
    setWorkflowStepId(WorkflowStepID)
    refetch();
    setDataGrids(workflowStepsData);
  };

  return (
    <List component="nav">
    {data && dataGrids && setDataGrids && data.map((workflow) => (
      <>
      <ListItemButton key={workflow.WorkflowStepID} onClick={() => handleWorkflowStepClick(workflow.WorkflowStepID)}>
        <ListItemIcon>
          <DashboardIcon />
        </ListItemIcon>
        <ListItemText primary={workflow.WorkflowStepName} />
      </ListItemButton>
      <ListSubheader component="div" inset>
        Workflow Step Groups
        <WorkflowStepGroups workflowStepGroups = {workflow.WorkflowStepGroups}  dataGrids = {dataGrids} setDataGrids = {setDataGrids} ></WorkflowStepGroups>
      </ListSubheader>
      </>
    ))}
  </List>
  )
};

export const secondaryListItems = (
  <React.Fragment>
      <ListSubheader component="div">
        Workflow Steps
      </ListSubheader>
      <ListItemButton>
        <ListItemIcon>
          <AssignmentIcon />
        </ListItemIcon>
        <ListItemText primary="Current month" />
      </ListItemButton>
  </React.Fragment>
);



