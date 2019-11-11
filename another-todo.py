def notiz_input():
    input("\nEingabe hier: ")


def close():
    loop = False


Todo = []
print("\n"+"-"*28)
print("Welcome to the Generic Todo!")
print("-"*28+"\n")
loop = True


while(loop):
    print("1. Notiz erstellen\n2. Notiz anschauen\n3. Notiz löschen\n4. Programm beenden")
    if(notiz_input() == "4"):
        exit()
    

