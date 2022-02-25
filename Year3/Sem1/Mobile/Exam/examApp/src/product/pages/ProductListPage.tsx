import {
    IonButton,
    IonContent,
    IonFab,
    IonFabButton,
    IonHeader,
    IonIcon, IonInput,
    IonList,
    IonLoading,
    IonPage,
    IonSearchbar,
    IonTitle,
    IonToolbar
} from '@ionic/react';
import {add} from 'ionicons/icons';
import React, {useContext, useEffect, useState} from 'react';
import {RouteComponentProps} from 'react-router';
import {changeQuantityApi} from '../../item/ItemApi';
import {ItemContext} from '../../item/ItemProvider';
import {ProductProps} from '../ProductProps';
import {ProductContext} from '../ProductProvider';
import ProductCard from './ProductCard';

export interface ProductWithQuantity {
    product: ProductProps;
    quantity: number;
}

const ProductsPage: React.FC<RouteComponentProps> = ({history}) => {
    const {products, loading} = useContext(ProductContext);
    const {items, changeQuantity} = useContext(ItemContext);
    const [selectedProductId, setSelectedProductId] = useState<number | undefined>(undefined);
    const [inputQuantity, setInputQuantity] = useState<string>("");

    const [productsWithQuantity, setProductsWithQuantity] = useState<ProductWithQuantity[]>([]);

    useEffect(() => {
        const tmp: ProductWithQuantity[] = []
        items && products && products.forEach(product => {
            const quantity = items.filter(item => item.productId === product.id)
                 .map(item => item.quantity)
                .reduce((a, b) => a + b, 0);

            const res: ProductWithQuantity = {
                product,
                quantity
            };

            tmp.push(res);
        });

        setProductsWithQuantity(tmp);
    }, [products, items])

    const addQuantity = () => {
        const quantity = parseInt(inputQuantity)

        if (quantity) {
            console.log(quantity);

            const item = items.find(i => i.productId === selectedProductId);
            if (item && selectedProductId)
                changeQuantity && changeQuantity(selectedProductId, { ...item, quantity: item.quantity + quantity });
        }
    }

    return (
        <IonPage>
            <IonHeader>
                <IonToolbar>
                    <IonTitle>Products</IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent fullscreen>
                <IonLoading isOpen={loading} message="Fetching entities..."/>
                <IonInput type="number" placeholder="quantity" onIonChange={event => setInputQuantity(event.detail.value!)}/>
                <IonButton onClick={addQuantity}>Add</IonButton>
                {productsWithQuantity && (
                    <IonList>
                        {productsWithQuantity.map(
                            pq => pq.product.id &&
                                  <ProductCard key={pq.product.id}
                                               entity={pq}
                                               selected={pq.product.id === selectedProductId}
                                               onClick={() => {
                                                   setSelectedProductId(pq.product.id);
                                                   console.log("selected " + pq.product.id);
                                               }}/>
                        )}
                    </IonList>
                )}
            </IonContent>
        </IonPage>
    );
};

export default ProductsPage;
