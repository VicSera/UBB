import {ActionProps} from '../core';
import {PRODUCT_OPERATION_FAILED, PRODUCT_OPERATION_STARTED, PRODUCT_SAVED, PRODUCT_DELETED, PRODUCTS_FETCHED} from './ProductActions';
import {ProductState} from './ProductState';

export const initialState: ProductState = {
    products: [],
    failed: false,
    loading: false
};

export const reducer: (state: ProductState, action: ActionProps) => ProductState = (state, {type, payload}) => {
    switch (type) {
        case PRODUCT_OPERATION_STARTED:
            return {...state, loading: true, failed: false};
        case PRODUCTS_FETCHED:
            return {...state, loading: false, products: payload.products};
        case PRODUCT_SAVED: {
            const products = [...state.products];
            const user = payload.product;
            const index = products.findIndex(it => it.id === user.id);
            if (index === -1) {
                products.splice(0, 0, user);
            } else {
                products[index] = user;
            }
            return { ...state, users: products, loading: false };
        }
        case PRODUCT_DELETED: {
            const products = [...state.products];
            const product = payload.product;
            const index = products.findIndex(it => it?.id === product.id);
            if (index !== -1) {
                products.splice(index, 1);
            }
            return { ...state, products, loading: false };
        }

        case PRODUCT_OPERATION_FAILED:
            return {...state, loading: false, failed: true};
        default:
            return state;
    }
};
