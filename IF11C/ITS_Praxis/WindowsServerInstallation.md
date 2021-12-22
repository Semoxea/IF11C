---
layout: default
title: "ITS-Praxis - Client-Server-Installation"
permalink: /ITSPraxis/CSI
---

## LS 1.2 Windows Server Installation

## Verlaufsprotokoll der Installation der virtuellen Maschinen am 12.10.21 von Sandra Saueressig auf 00054572

### Windows Server

#### HyperV Einstellungen

* Pfad der VM auf Host: C:\Documents\VMs\Machines\ITS-HyperV\Serverman\Serverman
* Größe der Festplatte: 30GB
* Größe des Arbeitsspeichers: 4GB
* Anzahl Prozessoren/Kerne: 1/1
* Netzwerkkarte: Bridged
* BS-Version: Windows Server 2019 Standard
* Servername: Serverman
* Anmeldename: Admin
* Passwort: Admin12345
* Firewalls deaktiviert
* IPv6 deaktiviert
* Updates verschoben
* IP-Adresse: 192.168.2.29
* Subnetzmaske: 255.255.255.0
* DNS-Server: 127.0.0.1

### Windows Clientwoman

#### HyperV Einstellungen

* Pfad der VM auf Host: C:\Berufsschule\IF11C\ITS\VMs\Clientwoman
* Größe der Festplatte: 20GB
* Größe des Arbeitsspeichers: 2GB
* Anzahl Prozessoren/Kerne: 1/1
* Netzwerkkarte: Bridged
* BS-Version: Windows 10 Education N
* Servername: Clientwoman
* Anmeldename: Admin
* Passwort: Admin12345
* Firewalls deaktiviert
* IPv6 deaktiviert
* Updates verschoben
* IP-Adresse: 192.168.2.22
* Subnetzmaske: 255.255.255.0
* DNS-Server: 192.168.2.29

### Windows Clientman

#### HyperV Einstellungen

* Pfad der VM auf Host: C:\ProgramData\Microsoft\Windows\Hyper-V
* Größe der Festplatte: 20GB
* Größe des Arbeitsspeichers: 2GB
* Anzahl Prozessoren/Kerne: 1/1
* Netzwerkkarte: Bridged
* BS-Version: Windows 10 Education N
* Servername: Clientman
* Anmeldename: Admin
* Passwort: Admin12345
* Firewalls deaktiviert
* IPv6 deaktiviert
* Updates verschoben
* IP-Adresse: 192.168.2.20
* Subnetzmaske: 255.255.255.0
* DNS-Server: 192.168.2.29

## Doku KW41

Berechtigungsplanung
![Berechtigungen](./images/Berechtigungen.png)
Domänengruppen
![DomaenenGruppen](./images/DomaenenGruppen.png)
Ordnerstruktur
![Ordnerstruktur](./images/Ordnerstruktur.png)

## Doku KW45

* Server und Client zu Ende konfiguriert
* DNS-Server auf Client auf Server-IP eingestellt
* Virtueller Switch den VMs zugewiesen
* Netzwerkplan erstellt
* Gruppen/Benutzer im AD angelegt

### Virtueller Netzwerkplan

|Computername|IP-Adresse|Schüler|Rolle|
|--|--|--|--|
|NETTMANN-PC01|192.168.2.22|Sandra|Client|
|NETTMANN-PC02|192.168.2.20|Kevin|Client|
|NETTSERVER|192.168.2.29|Lijon|Server|

![Netzwerkplan](./images/Networkplan.png)

### Gruppen- & Benutzeranlage im AD

|Gruppe|Anmeldenamen|Kennwort|
|--|--|--|
|Geschäftsleitung|hans-juergen.nettmann|hjn123|
|Verkaufsleitung|thomas.denkert|Thomas123|
|Verkauf|klaus.binderlein|Klaus123|
|Verkauf|beate.koches|Beate123|
|Sekretariat|melike.dosya|Melike123|
|Sekretariat|monika.heckamir|Monika123|
|Ausbildung|ines.ottmann|Ines123|
|Ausbildung|peter.donat|Peter123|
|Annahme|enrico.volante|Enrico123|
|Werkstatt|enrico.volante|Enrico123|
|Personalverwaltung|hans-juergen.nettmann|hjn123|
|Buchhaltung|melike.dosya|Melike123|

## Doku KW 50

* Neuer Client (Clientman) in Domäne aufgenommen
* Home-Laufwerk für Domänenbenutzer konfiguriert
* Netzwerkplan überarbeitet
* NTFS-Rechte/Zugriff auf Netzlaufwerk konfiguriert

### Home-Netzlaufwerk

|Aufgabe|Umsetzung/Hinweise|
|--|--|
|Zugriffsberechtigte Personen oder Gruppe konfigurieren|Jeder User nur auf seine Inhalte|
|Ordner anlegen und im Netzwerk freigeben|H:\\nettserver\Home|
|NTFS-Rechte vergeben|User: Lesen & Schreiben<br>Admin: Vollzugriff|
|Test mit verschiedenen Nutzern| erfolgreich|

### Weitere Netzlaufwerke

#### Ordner für den Verkauf

|Aufgabe|Umsetzung/Hinweise|
|--|--|
|Zugriffsberechtigte Personen oder Gruppe konfigurieren|Thomas Denkert, Klaus Binderlein, Beate Koches|
|Ordner anlegen und im Netzwerk freigeben|V:\\nettserver\Verkauf|
|NTFS-Rechte vergeben|Lesen & Schreiben für alle Benutzer und Domain-Admin|
|Test mit verschiedenen Nutzern|Binderlein & Denkert erfolgreich|

#### Public: Austauschlaufwerk

|Aufgabe|Umsetzung/Hinweise|
|--|--|
|Zugriffsberechtigte Personen oder Gruppe konfigurieren|Alle Domainmembers|
|Ordner anlegen und im Netzwerk freigeben|P:\\nettserver\Public|
|NTFS-Rechte vergeben|Domainmembers: Lesen & Schreiben<br>Administrator: Vollzugriff|
|Test mit verschiedenen Nutzern| Binderlein & Denkert erfolgreich|

#### Admin-Laufwerk

|Aufgabe|Umsetzung/Hinweise|
|--|--|
|Zugriffsberechtigte Personen oder Gruppe konfigurieren|Administrator, Hans-Juergen Nettmann|
|Ordner anlegen und im Netzwerk freigeben|Z:\\nettserver\Admin|
|NTFS-Rechte vergeben|HJ-Nettmanm: Lesen<br>Administrator: Vollzugriff|
|Test mit verschiedenen Nutzern| KW50: nicht erfolgreich|

#### Weitere Laufwerke

|Benutzer|Laufwerk|A-Laufwerk|L-Laufwerk|
|--|--|--|--|
|Verkaufsleitung|Anleitungen für Neuzugänge, Verwaltungsdaten der Geschäftsleitung|Lesen + Schreiben|Lesen + Schreiben|
|Geschäftsleitung|Verwaltungsdaten der Geschäftsleitung|Gar nichts|Vollzugriff|

### Doku KW 51

* Gruppenrichtlinien wurden hinzugefügt -> Jeder bekommt Eigene Dateien in Home kopiert
* Public-Freigabe für jeden
* Drucker wurde eingebunden

##### Note to self

Adaptereinstellungen umstellen auf DHCP für ITS, auf statisch 192.168.2.22 für ITT
