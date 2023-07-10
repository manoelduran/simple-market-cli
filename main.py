from typing import List, Dict
from time import sleep
from models.product import Product
from utils.helper import formatCoin

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('===================================')
    print('======================= Bem-vindo(a) ===========')
    print('======================= Manubas Store ===========')
    print('===================================')

    print('Selecione uma opção abaixo:')
    print('1 - Register Product:')
    print('2 - List Product:')
    print('3 - Buy Product:')
    print('4 - Show Cart:')
    print('5 - Confirm Order:')
    print('6 - Cancel:')

    option: int = int(input())
    if option == 1:
        register()
    elif option == 2:
        list()
    elif option == 3:
        buy()
    elif option == 4:
        showCart()
    elif option == 5:
        confirmOrder()
    elif option == 6:
        print('Welcome back!')
        sleep(2)
        exit(0)
    else:
        print('Invalid Option! Try another.')
        sleep(1)
        menu()


def register() -> None:
    print('Register Product')
    print('======================')

    name: str = input('Type the product name here:')
    price: float = float(input('Type the product price here:'))
    product: Product = Product(name, price)
    products.append(product)


    print(f'The {product.name} has been registered!')
    sleep(2)
    menu()


def list() -> None:
    if len(products) > 0:
        print('Products:')
        print('======================')
        for product in products:
            print(product)
            print('======================')
            sleep(1)
    else:
        print('No exists products in product list!')

    sleep(2)
    menu()


def buy() -> None:
    if len(products) > 0:
        print('Type the product code that you want to add in your cart:')
        print('===============================================================')
        print('Available products:')
        for product in products:
            print(product)
            print('===============================================================')
            sleep(1)
        code: int = int(input())
        product: Product = getProductByCode(code)
        print('===============================================================')
        if (product):
            if len(cart) > 0:
                existsInCart: bool = False
                for item in cart:
                    quantity: int = item.get(product)
                    if quantity:
                        item[product] = quantity + 1
                        print(
                            f'The product {product.name} now has {quantity + 1} units')
                        existsInCart = True
                        sleep(2)
                        menu()
                if not existsInCart:
                    dicionaryProduct = {product: 1}
                    cart.append(dicionaryProduct)
                    print(
                        f'The product {product.name} has been added to your cart!')
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                cart.append(item)
                print(f'Product {product.name} has been added to your cart!')
                sleep(2)
                menu()
        else:
            print('Product with code: {code} not found!')
            sleep(2)
            menu()
    else:
        print('No exists products in product list!')
    sleep(2)
    menu()


def showCart() -> None:
    if len(cart) > 0:
        print(f'Products in cart')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print(f'========================')
                
                sleep(1)
    else:
        print(f'Do not exsits products in your cart!')
    sleep(2)
    menu()

def confirmOrder() -> None:
    if len(cart) > 0:
        total: float = 0
        print('Products in cart:')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                total += data[0].price * data[1]
                print('====================')
                sleep(1)
        print(f'Your invoice is: {formatCoin(total)}')
        print(f'Welcome Back!')
        cart.clear()
        sleep(5)
    else:
        print('No exists products in cart!')

    sleep(2)
    menu()


def getProductByCode(code: int) -> Product:
    foundProduct: Product = None
    for product in products:
        if product.code == code:
            foundProduct = product
    return foundProduct


if __name__ == '__main__':
    main()
