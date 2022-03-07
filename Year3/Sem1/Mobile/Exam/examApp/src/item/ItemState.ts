import {ItemProps} from './ItemProps';

export type SaveItemFn = (props: ItemProps) => Promise<any>;
export type DeleteItemFn = (id: string) => Promise<any>;
export type RefreshItemsFn = () => Promise<any>;
export type ChangeQuantityFn = (productId: number, item: ItemProps) => Promise<any>;

export interface ItemState {
    items: ItemProps[];
    loading: boolean;
    failed: boolean;
    saveItem?: SaveItemFn;
    deleteItem?: DeleteItemFn;
    changeQuantity?: ChangeQuantityFn;
}
