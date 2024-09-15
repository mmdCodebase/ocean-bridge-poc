import axios, { AxiosRequestConfig } from 'axios';
import {QueryClient} from "react-query";

/*** --- APP SETTINGS --- ***/
export const APP_NAME = 'ocean_bridge_poc';
export const BASE_API_URL = process.env.REACT_APP_BASE_API_URL
const apiUrls = [BASE_API_URL];
const headers = {
    'Access-Control-Allow-Origin': '*',
    'Origin': 'localhost',
    'Content-Type': 'application/json',
  }
export const apiClients = apiUrls.map((baseUrl) => axios.create({ baseURL: baseUrl, headers: headers}));  
axios.defaults.baseURL = BASE_API_URL;
axios.defaults.headers.common['Authorization'] = '1234'

/*** --- REACT QUERY SETTINGS --- ***/
export const queryClient = new QueryClient({
    defaultOptions: {
        queries: {
            refetchOnWindowFocus: false,
        }
    }
})