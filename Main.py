from Diagramm import show_chart

while True:
    print("1) Einnahme hinzufügen")
    print("2) Ausgabe hinzufügen")
    print("3) Statistik anzeigen")
    print("4) Diagramm anzeigen")
    print("5) Beenden")
    choice = input("Wählen Sie eine Option: ")
    if choice == "1":
        eingabe = int(input("Geben Sie den Betrag der Einnahme ein: "))
        pass
    elif choice == "2":
        ausgabe = int(input("Geben Sie den Betrag der Ausgabe ein: "))
        pass
    elif choice == "3":
        print("Statistik wird angezeigt.")
        print("Einnahmen: ", eingabe)
        print("Ausgaben: ", ausgabe)
        print("Saldo: ", eingabe - ausgabe)
        pass
    elif choice == "4":
        print("Diagramm wird angezeigt.")
        show_chart()
    elif choice == "5":
        print("Programm wird beendet.")
        break
    else:
        print("Ungültige Option. Bitte wählen Sie erneut.")
   