import { ConstructionOutlined } from "@mui/icons-material";
import axios from "axios";

export default class WorkflowAPI {
    static async getWorkflowData({queryKey}) {
        //eslint-disable-next-line
        const workflowId = '9e40de8b-7a4e-11ee-9aff-00505686a13d'
            try {
                let res = await axios.get(`/V1/navigationtree/${workflowId}`);
                return res.data
            } catch (e) {
                console.error('Could not get workflow data: ', e.message);
                return undefined;
            }
    }

    static async getWorkflowStepData({queryKey}) {
        //eslint-disable-next-line
        const workflowstep_Id = '12345'
            try {
                let res = await axios.get(`/workflows/workflowstep/${workflowstep_Id}`);
                return res.data
            } catch (e) {
                console.error('Could not get workflow data: ', e.message);
                return undefined;
            }
    }

    static async getDataGrid({queryKey}) {
        //eslint-disable-next-line
        const datagrid_Id = '12345'
            try {
                let res = await axios.get(`/workflows/datagrid/${datagrid_Id}`);
                return res.data
            } catch (e) {
                console.error('Could not get workflow data: ', e.message);
                return undefined;
            }
    }

    static async getDataGridData({queryKey}) {
        //eslint-disable-next-line
        const datagrid_Id = '12345'
            try {
                let res = await axios.get(`/workflows/datagrid/${datagrid_Id}/data`);
                return res.data
            } catch (e) {
                console.error('Could not get workflow data: ', e.message);
                return undefined;
            }
    }

    static async updateDataGridData(queryKey) {
        //eslint-disable-next-line
        const action_id = queryKey[0]
        const requestBody = {
            "dataGridId": '',
            "dataGroupColumnID": queryKey[0],
            "primaryKey" : queryKey[1],
            "oldValue": queryKey[2],
            "newValue": queryKey[3],
        }
            try {
                let res = await axios.post(`/workflows/actions/${action_id}`, requestBody);
                return res.data
            } catch (e) {
                console.error('Could not get workflow data: ', e.message);
                return undefined;
            }
    }
}