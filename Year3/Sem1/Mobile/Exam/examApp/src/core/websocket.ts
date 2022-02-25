import {ItemProps} from '../item/ItemProps';
import {ProductProps} from '../product/ProductProps';
import {baseUrl, getLogger} from './index';

const log = getLogger("Websocket logger");

interface MessageData {
    event: string;
    payload: {
        entity: ItemProps | ProductProps;
    };
}

export const newWebSocket = (token: string | undefined, onMessage: (data: MessageData) => void, url: string = baseUrl) => {
    const ws = new WebSocket(`ws://${url}`)
    ws.onopen = () => {
        log('web socket onopen');
        ws.send(JSON.stringify({
           type: 'authorization',
           payload: { token }
       }));
    };
    ws.onclose = () => {
        log('web socket onclose');
    };
    ws.onerror = error => {
        log('web socket onerror', error);
    };
    ws.onmessage = messageEvent => {
        log('web socket onmessage');
        onMessage(JSON.parse(messageEvent.data));
    };

    return () => {
        ws.close();
    }
}
