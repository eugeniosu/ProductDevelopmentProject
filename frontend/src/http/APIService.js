/* eslint-disable */
import axios from 'axios';
const API_URL = process.env.API;

export class APIService{
    constructor(){

    }
    getFields() {
        const url = `${API_URL}/api/field/`;
        return axios.get(url).then(response => response.data);
    }
    getFieldsByURL(link){
        return axios.get(link).then(response => response.data);
    }
    getField(pk) {
        const url = `${API_URL}/api/field/${pk}/`;
        return axios.get(url).then(response => response.data);
    }
    deleteField(field){
        const url = `${API_URL}/api/field/${field.pk}/`;
        return axios.delete(url);
    }
    createField(field){
        const url = `${API_URL}/api/field/`;
        return axios.post(url,field);
    }
    updateField(field){
        const url = `${API_URL}/api/field/${field.pk}/`;
        return axios.put(url, field);
    }

    getRiskTypes() {
        const url = `${API_URL}/api/risktype/`;
        return axios.get(url).then(response => response.data);
    }
    getRiskTypesByURL(link){
        return axios.get(link).then(response => response.data);
    }
    getRiskType(pk) {
        const url = `${API_URL}/api/risktype/${pk}/`;
        return axios.get(url).then(response => response.data);
    }
    deleteRiskType(riskType){
        const url = `${API_URL}/api/risktype/${riskType.pk}/`;
        return axios.delete(url);
    }
    createRiskType(riskType){
        const url = `${API_URL}/api/risktype/`;
        return axios.post(url,riskType);
    }
    updateRiskType(riskType){
        const url = `${API_URL}/api/risktype/${riskType.pk}/`;
        return axios.put(url, riskType);
    }

    getRisks() {
        const url = `${API_URL}/api/risk/`;
        return axios.get(url).then(response => response.data);
    }
    getRisksByURL(link){
        return axios.get(link).then(response => response.data);
    }
    getRisk(pk) {
        const url = `${API_URL}/api/risk/${pk}/`;
        return axios.get(url).then(response => response.data);
    }
    deleteRisk(risk){
        const url = `${API_URL}/api/risk/${risk.pk}/`;
        return axios.delete(url);
    }
    createRisk(risk){
        const url = `${API_URL}/api/risk/`;
        return axios.post(url,risk);
    }
    updateRisk(risk){
        const url = `${API_URL}/api/risk/${risk.pk}/`;
        return axios.put(url, risk);
    }

    getFieldRisks() {
        const url = `${API_URL}/api/fieldrisk/`;
        return axios.get(url).then(response => response.data);
    }
    getFieldRisksByURL(link){
        return axios.get(link).then(response => response.data);
    }
    getFieldRisk(pk) {
        const url = `${API_URL}/api/fieldrisk/${pk}/`;
        return axios.get(url).then(response => response.data);
    }
    deleteFieldRisk(risk){
        const url = `${API_URL}/api/fieldrisk/${risk.pk}/`;
        return axios.delete(url);
    }
    createFieldRisk(risk){
        const url = `${API_URL}/api/fieldrisk/`;
        return axios.post(url,risk);
    }
    updateFieldRisk(risk){
        const url = `${API_URL}/api/fieldrisk/${risk.pk}/`;
        return axios.put(url, risk);
    }
}
