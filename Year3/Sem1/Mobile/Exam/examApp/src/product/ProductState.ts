import {ProductProps} from './ProductProps';

export type SaveProductFn = (props: ProductProps) => Promise<any>;
export type DeleteProductFn = (id: string) => Promise<any>;

export interface ProductState {
    products: ProductProps[];
    loading: boolean;
    failed: boolean;
    saveProduct?: SaveProductFn;
    deleteProduct?: DeleteProductFn;
}
