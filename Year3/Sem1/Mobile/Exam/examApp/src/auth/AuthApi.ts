import axios from 'axios';
import {baseUrl, getLogger} from '../core';
import {axiosConfig, createWithLogs} from '../core/axiosConfig';
import {AuthProps} from './AuthProps';
import {UserProps} from './UserProps';

const authUrl = `http://${baseUrl}/auth`;

const log = getLogger('authApi');
const withLogs = createWithLogs(log);

export const login: (username: string, password: string) => Promise<AuthProps> = async (username, password) => {
    return withLogs(axios.post(`${authUrl}/login`, {username, password}, await axiosConfig()), 'login');
}

export const registerUser: (user: UserProps) => Promise<AuthProps> = async user => {
    return withLogs(axios.post(`${authUrl}/register`, user, await axiosConfig()), 'register');
}

