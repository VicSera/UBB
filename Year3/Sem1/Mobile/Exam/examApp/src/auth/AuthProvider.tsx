import PropTypes from 'prop-types';
import React, {useCallback, useEffect, useReducer} from 'react';
import {getLogger} from '../core';
import {getCachedUserAndToken, updateAuthToken} from '../core/axiosConfig';
import {LOGIN_FAILED, LOGIN_SUCCEEDED, LOGIN_TRIGGERED, LOGOUT} from './AuthActions';
import {login} from './AuthApi';
import {initialState, reducer} from './AuthReducer';
import {AuthState, LogoutFn, TriggerLoginFn} from './AuthState';

export const AuthContext = React.createContext<AuthState>(initialState)

const log = getLogger('AuthProvider');

interface AuthProviderProps {
    children: PropTypes.ReactNodeLike
}

export const AuthProvider: React.FC<AuthProviderProps> = ({children}) => {
    const [state, dispatch] = useReducer(reducer, initialState);
    const { user, token, loading } = state;

    useEffect(() => {
        getCachedUserAndToken().then(userAndToken => {
            if (userAndToken) {
                dispatch({type: LOGIN_SUCCEEDED, payload: {user: userAndToken.user, token: userAndToken.token}});
            }
        });
    }, []);

    const triggerLogin = useCallback<TriggerLoginFn>(triggerLoginCallback, []);
    const logout = useCallback<LogoutFn>(logoutCallback, []);
    const value = { user, token, loading, triggerLogin, logout };
    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    )

    async function triggerLoginCallback(username: string, password: string): Promise<boolean> {
        try {
            dispatch({type: LOGIN_TRIGGERED});
            const {user, token} = await login(username, password);
            await updateAuthToken(token);
            dispatch({type: LOGIN_SUCCEEDED, payload: {user, token}});
            return true;
        } catch (error) {
            dispatch({type: LOGIN_FAILED, payload: {error}});
            return false;
        }
    }

    async function logoutCallback() {
        dispatch({type: LOGOUT});
        await updateAuthToken('');
    }
}
