export const getLogger: (tag: string) => (...args: any) => void =
    tag => (...args) => console.log(tag, ...args);

export type Logger = (...args: any) => void;

export const baseUrl = 'localhost:3000';

export interface ActionProps {
    type: string,
    payload?: any
}

export interface ResponseProps<T> {
    data: T;
}
