Für jede Landschaft enthält die entsprechende Textdatei
  * in der ersten Zeile ihre vertikale Länge als Anzahl von Kachelreihen von oben nach unten und
  * in der zweiten Zeile ihre horizontale Breite als Anzahl von Kachelspalten von links nach rechts.

Für das Beispiel einer unvollständigen Landschaft auf dem Aufgabenblatt ist also die Länge "2" in der ersten Zeile und die Breite "2" in der zweiten Zeile der Textdatei. Danach folgt stets eine Leerzeile.

Die weiteren Zeilen der Textdatei enthalten die Landschaft als eine Karte von Kacheln. Je zwei aufeinander folgende Zeilen der Textdatei enthalten horizontal nebeneinander liegende Kacheln, gefolgt von jeweils einer die Kacheln vertikal trennenden Leerzeile oder dem Dateiende. Da jede Kachel aus 2x2 Quadraten besteht, umfasst die Landschaftskarte insgesamt doppelt so viele Quadrate in der Länge und Breite als Kacheln.

Jedes der vier Quadrate einer Kachel wird durch eines der Zeichen "0", "1" oder *" dargestellt. "0" steht für ein Quadrat mit Wasser und "1"  für ein Quadrat mit Land an den jeweiligen Außenseiten der Kachel. "*" repräsentiert je eines von vier Quadraten einer Kachel mit noch unbekannter Landschaft.

Innerhalb einer Textzeile folgt auf jedes Zeichen für ein Quadrat ein trennendes Leerzeichen. Die beiden horizontal benachbarten Quadrate zweier nebeneinander liegenden Kacheln sind jeweils durch drei Leerzeichen voneinander getrennt.

Als alternative Eingabedateien (zum Beispiel für die Blockly-Umgebung) stehen die obigen Textdateien auch in kompakter Form ohne Leerzeichen und Leerzeilen zur Verfügung.
