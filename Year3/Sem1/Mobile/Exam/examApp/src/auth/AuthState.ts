import {UserProps} from './UserProps';

export type TriggerLoginFn = (username: string, password: string) => Promise<boolean>;
export type LogoutFn = () => void;

export interface AuthState {
    loading: boolean;
    user?: UserProps;
    token?: string;
    triggerLogin?: TriggerLoginFn;
    logout?: LogoutFn;
}
