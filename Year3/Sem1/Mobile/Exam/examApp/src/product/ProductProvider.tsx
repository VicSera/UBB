import PropTypes from 'prop-types';
import {useCallback, useContext, useEffect, useReducer} from 'react';
import * as React from 'react';
import {AuthContext} from '../auth/AuthProvider';
import {getLogger} from '../core';
import {newWebSocket} from '../core/websocket';
import {PRODUCT_OPERATION_FAILED, PRODUCT_OPERATION_STARTED, PRODUCT_SAVED, PRODUCTS_FETCHED} from './ProductActions';
import {addProduct, deleteProduct, getProducts, updateProduct} from './ProductApi';
import {ProductProps} from './ProductProps';
import {initialState, reducer} from './ProductReducer';
import {DeleteProductFn, ProductState, SaveProductFn} from './ProductState';


export const ProductContext = React.createContext<ProductState>(initialState);

const log = getLogger('ProductProvider')

interface ProductProviderProps {
    children: PropTypes.ReactNodeLike;
}

export const ProductProvider: React.FC<ProductProviderProps> = ({children}) => {
    const [state, dispatch] = useReducer(reducer, initialState);
    const { token } = useContext(AuthContext);
    const { products, loading, failed } = state;

    useEffect(initializeEntities, []);

    const saveProduct = useCallback<SaveProductFn>(saveProductCallback, []);
    const deleteProduct = useCallback<DeleteProductFn>(removeProductCallback, []);
    const value = { products, loading, failed, saveProduct, deleteProduct };
    return (
        <ProductContext.Provider value={value}>
            {children}
        </ProductContext.Provider>
    );

    function initializeEntities() {
        let canceled = false;
        fetchEntities().then(() => log('Users fetched successfully'));

        return () => {
            canceled = true;
        };

        async function fetchEntities() {
            try {
                dispatch({type: PRODUCT_OPERATION_STARTED});
                let fetchedProducts = await getProducts();

                if (!canceled) {
                    dispatch({type: PRODUCTS_FETCHED, payload: {products: fetchedProducts}});
                }
            } catch (error) {
                dispatch({type: PRODUCT_OPERATION_FAILED, payload: {error}});
            }
        }
    }

    async function saveProductCallback(entity: ProductProps) {
        try {
            dispatch({type: PRODUCT_OPERATION_STARTED});
            let returnedProduct = await (entity.id ? updateProduct(entity) : addProduct(entity));
            dispatch({type: PRODUCT_SAVED, payload: {product: returnedProduct}});
        } catch (error) {
            dispatch({type: PRODUCT_OPERATION_FAILED, payload: {error}});
        }
    }

    async function removeProductCallback(id: string) {
        try {
            dispatch({type: PRODUCT_OPERATION_STARTED});
            await deleteProduct(id);
        } catch (error) {
            dispatch({type: PRODUCT_OPERATION_FAILED, payload: {error}});
        }
    }
};
