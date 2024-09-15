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
import { WorkflowSteps } from './WorkflowSteps.tsx';  

export function WorkflowStepGroups(props) {
  const { workflowStepGroups, dataGrids, setDataGrids } = props;
    return (
      <React.Fragment>
      {workflowStepGroups && workflowStepGroups.map((workflowStepGroup) => (
        <>
        <ListItemButton key={workflowStepGroup.WorkflowStepGroupID}>
          <ListItemIcon>
            <ShoppingCartIcon />
          </ListItemIcon>
          <ListItemText primary={workflowStepGroup.WorkflowStepGroup_Name} />
        </ListItemButton>
        {workflowStepGroup.WorkflowSteps && <WorkflowSteps workflowSteps={workflowStepGroup.WorkflowSteps} dataGrids = {dataGrids} setDataGrids = {setDataGrids} />}
        </>
      ))}
    </React.Fragment>
    )
    };