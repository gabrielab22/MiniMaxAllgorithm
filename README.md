Minimax algoritam

Napraviti implementaciju minmax algoritma za igru podizanja štapića. Pravila igre (koju igraju 2 igrača) su sljedeća:

•	Na podu se nalazi 11 štapića.
•	Svaki igrač može podignuti 1 ili 2 štapića.
•	Igrači se mijenjaju sve dok na podu postoji barem jedan štapić
•	Igrač koji podigne zadnja 2 štapića pobjeđuje.
•	Igrač koji pokuša podignuti 2 štapića dok se na podu nalazi samo 1 štapić gubi igru.
•	Prethodna dva pravila efektivno kažu da igra završava (i igrač na redu gubi) ako je na podu manje od 2 štapića (1 ili 0).

Algoritam treba preuzeti ulogu drugog igrača tj. računala i igrati protiv osobe koja će svoje korake unositi preko konzole. Uz implementaciju minmax algoritma potrebno je osmisliti i implementirati klasu koja će predstavljati stanje igre te koristiti tu klasu kao dio minmax implementacije. Pomoćna klasa treba pratiti sve relevantne segmente igre kao što su:
•	Trenutni igrač
•	Broj štapića na podu
