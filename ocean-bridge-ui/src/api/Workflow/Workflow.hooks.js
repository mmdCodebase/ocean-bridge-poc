import { useQuery, useMutation } from "react-query";
import WorkflowAPI from "./Workflow.api";

export function useGetWorkflow(query){
    return useQuery(["fetchWorkflow", query], WorkflowAPI.getWorkflowData);
}

export function useGetWorkflowSteps(query){
    return useQuery(["fetchWorkflowSteps", query], WorkflowAPI.getWorkflowStepData);
}

export function useGetDataGrid(query){
    return useQuery(["fetchDataGrid", query], WorkflowAPI.getDataGrid);
}

export function useGetDataGridData(query){
    return useQuery(["fetchDataGridData", query], WorkflowAPI.getDataGridData);
}

export function useUpdateDataGridData(query){
    return useMutation(["updateDataGridData", query], WorkflowAPI.updateDataGridData);
}