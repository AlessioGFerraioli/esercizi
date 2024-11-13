def decoratore(funzione):
    def wrapper():
        print("Prima")
        funzione()
        print("Dopo")
    return wrapper

@decoratore
def saluta():
    print("ciao")

saluta()