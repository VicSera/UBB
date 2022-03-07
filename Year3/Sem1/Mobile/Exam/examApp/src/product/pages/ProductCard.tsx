import { IonItem, IonLabel } from '@ionic/react';
import React from 'react';
import {ProductWithQuantity} from './ProductListPage';

interface ProductCardProps {
    entity: ProductWithQuantity,
    onClick: (productId: number) => void,
    selected: boolean
}

const ProductCard: React.FC<ProductCardProps> = ({entity, onClick, selected}) => {
    const getClass = () => {
        if (selected)
            return "item md item-fill-none in-list item-label selected-product"
        else return "item md item-fill-none in-list item-label";
    }

    return (
        <IonItem onClick={() => onClick(entity.product.id)} class={getClass()}>
            <IonLabel>{entity.product.name} - {entity.quantity}</IonLabel>
        </IonItem>
    );
};

export default ProductCard;
