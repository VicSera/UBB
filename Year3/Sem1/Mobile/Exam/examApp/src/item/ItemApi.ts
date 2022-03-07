import {Storage} from '@capacitor/storage';
import axios from 'axios';
import {baseUrl, getLogger} from '../core';
import {axiosConfig, createWithLogs} from '../core/axiosConfig';
import {ItemProps} from './ItemProps';

const url = `http://${baseUrl}/item`;

const log = getLogger('itemApi');
const withLogs = createWithLogs(log);

export const changeQuantityApi: (productId: number, item: ItemProps) => Promise<any> = async (productId, item) => {
    return withLogs(axios.put(`${url}/${productId.toString()}`, item), 'changeQuantity')
}

export const getItems: () => Promise<ItemProps[]> = async () => {
    return withLogs(axios.get(url, await axiosConfig()), 'getItems');
}

export const addItem: (entity: ItemProps) => Promise<ItemProps> = async entity => {
    return withLogs(axios.post(url, entity, await axiosConfig()), 'addEntity');
}

export const updateItem: (entity: ItemProps) => Promise<ItemProps> = async entity => {
    return withLogs(axios.put(url, entity, await axiosConfig()), 'updateEntity');
}

export const deleteItem: (id: string | number) => Promise<ItemProps> = async id => {
    return withLogs(axios.delete(`${url}/${id.toString()}`, await axiosConfig()), 'deleteEntity')
}
