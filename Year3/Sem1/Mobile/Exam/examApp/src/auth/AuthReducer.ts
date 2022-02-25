import {ActionProps} from '../core';
import {LOGIN_FAILED, LOGIN_SUCCEEDED, LOGIN_TRIGGERED, LOGOUT} from './AuthActions';
import {AuthState} from './AuthState';

export const initialState: AuthState = {
    loading: false
}

export const reducer: (state: AuthState, action: ActionProps) => AuthState = (state, {type, payload}) => {
    switch(type) {
        case LOGIN_TRIGGERED:
            return {...state, loading: true};
        case LOGIN_SUCCEEDED:
            return {...state, user: payload.user, token: payload.token, loading: false};
        case LOGIN_FAILED:
            return {...state, user: undefined, token: undefined, loading: false};
        case LOGOUT:
            return {...state, user: undefined, token: undefined, loading: false};
        default:
            return state;
    }
}
