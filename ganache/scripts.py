from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('http://localhost:7545'))

def get_account_balance():
    address = input("Introduce la dirección de la cuenta para consultar su balance: ")
    if w3.is_address(address):
        balance = w3.eth.get_balance(address)
        print(f"Balance de la cuenta {address}: {w3.from_wei(balance, 'ether')} ETH")
    else:
        print("Dirección no válida.")

def get_latest_block_number():
    block_number = w3.eth.block_number
    print(f"El número del último bloque es: {block_number}")

def get_account_transactions():
    address = input("Introduce la dirección de la cuenta para consultar sus transacciones: ")
    if w3.is_address(address):
        block_number = w3.eth.block_number
        for i in range(block_number):
            block = w3.eth.get_block(i, full_transactions=True)
            for tx in block['transactions']:
                if tx['from'] == address or tx['to'] == address:
                    print(tx)
    else:
        print("Dirección no válida.")

def get_account_nonce():
    address = input("Introduce la dirección de la cuenta para consultar su nonce: ")
    if w3.is_address(address):
        nonce = w3.eth.get_transaction_count(address)
        print(f"Nonce de la cuenta {address}: {nonce}")
    else:
        print("Dirección no válida.")

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Consultar el balance de una dirección")
        print("2. Obtener el número del último bloque minado")
        print("3. Ver transacciones de una cuenta")
        print("4. Consultar el nonce de una cuenta")
        print("5. Salir")

        choice = input("\nElige una opción: ")

        if choice == "1":
            get_account_balance()
        elif choice == "2":
            get_latest_block_number()
        elif choice == "3":
            get_account_transactions()
        elif choice == "4":
            get_account_nonce()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
