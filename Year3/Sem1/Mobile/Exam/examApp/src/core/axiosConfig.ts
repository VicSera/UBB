import {UserProps} from '../auth/UserProps';
import {Logger, ResponseProps} from './index';
import {Storage} from "@capacitor/storage"

export const axiosConfig = async () => {
    return {
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${(await Storage.get({key: 'AUTH_TOKEN'})).value}`
        }
    }
};

export async function updateAuthToken(token: string) {
    await Storage.set({
        key: 'AUTH_TOKEN',
        value: token
    });
}

export const createWithLogs: (logger: Logger) => <T>(promise: Promise<ResponseProps<T>>, fnName: string) => Promise<T> =
    (logger) => (promise, fnName) => withLogs(logger, promise, fnName);

function withLogs<T>(log: Logger, promise: Promise<ResponseProps<T>>, fnName: string): Promise<T> {
    log(`${fnName} - started`);
    return promise
        .then(res => {
            log(`${fnName} - succeeded`);
            return Promise.resolve(res.data);
        })
        .catch(err => {
            log(`${fnName} - failed`);
            return Promise.reject(err);
        });
}

export async function getCachedUserAndToken(): Promise<UserAndToken | undefined> {
    const token = (await Storage.get({key: 'AUTH_TOKEN'})).value;
    if (token)
        return {token, user: extractUserFromToken(token)};
    else
        return undefined;
}

interface UserAndToken {
    user: UserProps;
    token: string;
}

function extractUserFromToken(token: string): UserProps {
    return JSON.parse(atob(token.split('.')[1])) as UserProps;
}
