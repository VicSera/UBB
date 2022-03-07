import { IonItem, IonLabel } from '@ionic/react';
import React from 'react';
import {ItemProps} from '../ItemProps';

interface DomainEntityCardProps {
    entity: ItemProps
}

const ItemCard: React.FC<DomainEntityCardProps> = ({entity}) => {
    return (
        <IonItem onClick={() => {}}>

        </IonItem>
    );
};

export default ItemCard;
