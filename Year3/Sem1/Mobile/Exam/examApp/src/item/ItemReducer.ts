import {ActionProps} from '../core';
import {ITEM_DELETED, ITEM_OPERATION_FAILED, ITEM_OPERATION_STARTED, ITEM_SAVED, ITEMS_FETCHED} from './ItemActions';
import {ItemState} from './ItemState';

export const initialState: ItemState = {
    items: [],
    failed: false,
    loading: false
};

export const reducer: (state: ItemState, action: ActionProps) => ItemState = (state, {type, payload}) => {
    switch (type) {
        case ITEM_OPERATION_STARTED:
            return {...state, loading: true, failed: false};
        case ITEMS_FETCHED:
            return {...state, loading: false, items: payload.items};

        case ITEM_SAVED: {
            return state;
            // const items = [...state.items];
            // const user = payload.item;
            // const index = items.findIndex(it => it.id === user.id);
            // if (index === -1) {
            //     items.splice(0, 0, user);
            // } else {
            //     items[index] = user;
            // }
            // return { ...state, users: items, loading: false };
        }
        case ITEM_DELETED: {
            return state;
            // const items = [...state.items];
            // const item = payload.item;
            // const index = items.findIndex(it => it?.id === item.id);
            // if (index !== -1) {
            //     items.splice(index, 1);
            // }
            // return { ...state, items, loading: false };
        }

        case ITEM_OPERATION_FAILED:
            return {...state, loading: false, failed: true};
        default:
            return state;
    }
};
