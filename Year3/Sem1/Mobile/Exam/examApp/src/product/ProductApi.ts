import axios from 'axios';
import {baseUrl, getLogger} from '../core';
import {axiosConfig, createWithLogs} from '../core/axiosConfig';
import {ProductProps} from './ProductProps';

const url = `http://${baseUrl}/product`;

const log = getLogger('entityApi');
const withLogs = createWithLogs(log);

export const getProducts: () => Promise<ProductProps[]> = async () => {
    return withLogs(axios.get(url, await axiosConfig()), 'getProducts');
}

export const addProduct: (entity: ProductProps) => Promise<ProductProps> = async entity => {
    return withLogs(axios.post(url, entity, await axiosConfig()), 'addEntity');
}

export const updateProduct: (entity: ProductProps) => Promise<ProductProps> = async entity => {
    return withLogs(axios.put(url, entity, await axiosConfig()), 'updateEntity');
}

export const deleteProduct: (id: string | number) => Promise<ProductProps> = async id => {
    return withLogs(axios.delete(`${url}/${id.toString()}`, await axiosConfig()), 'deleteEntity')
}
