-- Aufgabe 5
insert into tblbenutzer (BenutzerID, Nachname) values (8, 'Saueressig');
Query OK, 1 row affected (0.03 sec)
-- Aufgabe 6
insert into tblchips (ChipsID, ChipSerienNr, tblBenutzer_BenutzerID) values (16, '01104ACFBE12', 8);
Query OK, 1 row affected (0.03 sec)
-- Check
select * from tblchips;
+---------+--------------+------------------------+
| ChipsID | ChipSerienNr | tblBenutzer_BenutzerID |
+---------+--------------+------------------------+
|       2 | 01104A1CAAED |                      1 |
|       3 | 01104A6DBF89 |                      2 |
|       4 | 01104A3EE085 |                      3 |
|       5 | 010FA0DF2657 |                      4 |
|      12 | 01104A3EC4A1 |                      5 |
|      14 | 01104A41CBD1 |                      6 |
|      15 | 011049BF7790 |                      7 |
|      16 | 01104ACFBE12 |                      8 |
+---------+--------------+------------------------+
-- Aufgabe 7
insert into tblreader (ReaderID, Bezeichnung) values (5, 'Neuer Eingang');
Query OK, 1 row affected (0.04 sec)

-- Check
select * from tblreader;
+----------+----------------------+
| ReaderID | Bezeichnung          |
+----------+----------------------+
|        1 | Eingang Lager        |
|        2 | Eingang Werkstatt    |
|        3 | Eingang B├╝ro        |
|        4 | Zugang B├╝ro/Verkauf |
|        5 | Neuer Eingang        |
+----------+----------------------+
5 rows in set (0.00 sec)
-- Aufgabe 8
insert into tblberechtigung (tblChips_ChipsID, tblReader_ReaderID) values (16, 3);
Query OK, 1 row affected (0.40 sec)
-- Aufgabe 9
insert into tblberechtigung (tblChips_ChipsID, tblReader_ReaderID) values (2, 1);
Query OK, 1 row affected (0.01 sec)

insert into tblberechtigung (tblChips_ChipsID, tblReader_ReaderID) values (2, 2);
Query OK, 1 row affected (0.01 sec)

insert into tblberechtigung (tblChips_ChipsID, tblReader_ReaderID) values (2, 3);
Query OK, 1 row affected (0.00 sec)

insert into tblberechtigung (tblChips_ChipsID, tblReader_ReaderID) values (2, 4);
Query OK, 1 row affected (0.01 sec)
-- Aufgabe 10
-- BenutzerID-Check
select * from tblbenutzer;
+------------+------------+
| BenutzerID | Nachname   |
+------------+------------+
|          1 | Nettmann   |
|          2 | Schmidt    |
|          3 | Aydin      |
|          4 | Tabor      |
|          5 | Maier      |
|          6 | Praktikant |
|          7 | Gast       |
|          8 | Saueressig |
+------------+------------+
8 rows in set (0.00 sec)

-- Chip löschen
delete from tblchips where tblBenutzer_BenutzerID=4;
Query OK, 1 row affected (0.02 sec)
-- Benutzer löschen
delete from tblbenutzer where Nachname='Tabor';
Query OK, 1 row affected (0.01 sec)

-- Aufgabe 11
-- Namensänderung
update tblbenutzer set Nachname='Schmidt-Huber' where BenutzerID=2;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

-- Überprüfung
select * from tblbenutzer;
+------------+---------------+
| BenutzerID | Nachname      |
+------------+---------------+
|          1 | Nettmann      |
|          2 | Schmidt-Huber |
|          3 | Aydin         |
|          5 | Maier         |
|          6 | Praktikant    |
|          7 | Gast          |
|          8 | Saueressig    |
+------------+---------------+
7 rows in set (0.00 sec)
-- Aufgabe 12
-- Alle Zugangsberechtigungen fürs Lager löschen
delete from tblberechtigung where tblReader_ReaderID=1;
Query OK, 2 rows affected (0.03 sec)

-- Nettmann wieder dazufügen
insert into tblberechtigung(tblChips_ChipsID, tblReader_ReaderID) values (2, 1);
Query OK, 1 row affected (0.01 sec)