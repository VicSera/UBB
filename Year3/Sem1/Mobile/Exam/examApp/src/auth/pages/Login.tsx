import {IonButton, IonContent, IonInput, IonPage} from '@ionic/react';
import React, {useContext, useEffect, useState} from 'react';
import {RouteComponentProps} from 'react-router';
import {AuthContext} from '../AuthProvider';

interface LoginPageProps extends RouteComponentProps {
    homePage: string;
}

const Login: React.FC<LoginPageProps> = ({history, homePage}) => {
    const {triggerLogin, token} = useContext(AuthContext);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    useEffect(() => {
        if (token) {
            history.push(homePage)
        }
    }, [token, history, homePage])

    function login() {
        triggerLogin && triggerLogin(username, password).then(success => success && history.push(homePage));
    }

    return (
        <IonPage>
            <IonContent>
                <IonInput className='input' value={username} onIonChange={e => setUsername(e.detail.value || '')} />
                <IonInput type='password' className='input' value={password} onIonChange={e => setPassword(e.detail.value || '')} />
                <IonButton onClick={login}>Log in</IonButton>
            </IonContent>
        </IonPage>
    );
};

export default Login;
