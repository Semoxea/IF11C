list = [0,0,0,0,0,0,0,0,0,0]


while True:
    i = 0
    while i<=9:
        match list[i]:
            case 0: print("Parkplatz", i+1, "ist frei.")
            case 1: print("Parkplatz", i+1, "ist belegt.")
            case 2: print("Parkplatz", i+1, "ist reserviert.")
        i=i+1
    iParkplatzNr = int(input("Geben Sie die Parkplatznummer des Parkplatzes an dessen Status sie ändern möchten.\n"))
    while True:
        if iParkplatzNr<=len(list):
            break
        else:
            print("Eine falsche Eingabe wurde getätigt. Bitte versuchen Sie es erneut.")
    iStatus = int(input("Geben Sie den gewünschten Status des Parkplatzes an. 0 = frei, 1 = belegt, 2 = reserviert\n"))
    while True:
        match iStatus:
            case 0: print("Parkplatz", iParkplatzNr, "ist jetzt frei.\n\n")
            case 1: print("Parkplatz", iParkplatzNr, "ist jetzt belegt.\n\n")
            case 2: print("Parkplatz", iParkplatzNr, "ist jetzt reserviert.\n\n")
        if iStatus != 0 and iStatus != 1 and iStatus != 2:
            print("Eine falsche Eingabe wurde getätigt. Bitte versuchen Sie es erneut.")
        else:
            list[iParkplatzNr-1] = iStatus
            break
    
