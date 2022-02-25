import PropTypes from 'prop-types';
import {useCallback, useContext, useEffect, useReducer} from 'react';
import * as React from 'react';
import {AuthContext} from '../auth/AuthProvider';
import {getLogger} from '../core';
import {newWebSocket} from '../core/websocket';
import {ITEM_OPERATION_FAILED, ITEM_OPERATION_STARTED, ITEM_SAVED, ITEMS_FETCHED} from './ItemActions';
import {addItem, changeQuantityApi, deleteItem, getItems, updateItem} from './ItemApi';
import {ItemProps} from './ItemProps';
import {initialState, reducer} from './ItemReducer';
import {ChangeQuantityFn, DeleteItemFn, ItemState, RefreshItemsFn, SaveItemFn} from './ItemState';

export const ItemContext = React.createContext<ItemState>(initialState);

const log = getLogger('DomainEntityProvider')

interface ItemProviderProps {
    children: PropTypes.ReactNodeLike;
}

export const ItemProvider: React.FC<ItemProviderProps> = ({children}) => {
    const [state, dispatch] = useReducer(reducer, initialState);
    const { token } = useContext(AuthContext);
    const { items, loading, failed } = state;

    useEffect(getItemsCallback, []);
    useEffect(wsEffect, [token]);

    const saveItem = useCallback<SaveItemFn>(saveItemCallback, []);
    const deleteItem = useCallback<DeleteItemFn>(removeItemCallback, []);
    const changeQuantity = useCallback<ChangeQuantityFn>(changeQuantityCallback, []);
    const value = { items, loading, failed, saveItem, deleteItem, changeQuantity };

    return (
        <ItemContext.Provider value={value}>
            {children}
        </ItemContext.Provider>
    );

    async function changeQuantityCallback(productId: number, item: ItemProps) {
        try {
            dispatch({type: ITEM_OPERATION_STARTED});
            await changeQuantityApi(productId, item);
            dispatch({type: ITEM_SAVED});
            getItemsCallback();
        } catch (error) {
            dispatch({type: ITEM_OPERATION_FAILED, payload: {error}});
            getItemsCallback();
        }
    }

    function getItemsCallback() {
        let canceled = false;
        fetchItems().then(() => log('Items fetched successfully'));

        async function fetchItems() {
            try {
                dispatch({type: ITEM_OPERATION_STARTED});
                let fetchedEntities = await getItems();

                if (!canceled)
                    dispatch({type: ITEMS_FETCHED, payload: {items: fetchedEntities}});
            } catch (error) {
                dispatch({type: ITEM_OPERATION_FAILED, payload: {error}});
            }
        }

        return () => {
            canceled = true;
        };
    }

    async function saveItemCallback(entity: ItemProps) {
        try {
            // dispatch({type: ITEM_OPERATION_STARTED});
            // let returnedEntity = await (entity.id ? updateItem(entity) : addItem(entity));
            // dispatch({type: ITEM_SAVED, payload: {item: returnedEntity}});
        } catch (error) {
            dispatch({type: ITEM_OPERATION_FAILED, payload: {error}});
        }
    }

    async function removeItemCallback(id: string) {
        try {
            dispatch({type: ITEM_OPERATION_STARTED});
            await deleteItem(id);
        } catch (error) {
            dispatch({type: ITEM_OPERATION_FAILED, payload: {error}});
        }
    }

    function wsEffect() {
    }
};
