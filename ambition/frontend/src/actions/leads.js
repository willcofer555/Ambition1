import axios from 'axios';
import { GET_LEADS } from './types';

//Get leads 

export const getLeads = () => dispatch => {
    axios
    .get("/api/amb_app/")
    .then(res => {
        dispatch({
            type: GET_LEADS,
            payload: res.data
        });
    }).catch(err => console.log(err));
    
        
};