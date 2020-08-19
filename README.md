# leapyear-api

Dieses Repository enthält die Demo und Konfigurationen für
TekTon auf OpenShift 4.

Die Demo beinhaltet einen Flask-Server Dienst, der zu einer
Jahreszahl über die API ausgibt, ob es sich um ein Schaltjahr
handelt oder nicht.

Das Verzeichnis `pipeline/` beinhaltet Template-Dateien und
das Script zum Einrichten der Demo in einem OpenShift Cluster.

Im Verzeichnis `k8s/` bedindet sich die Resource-Definition
für die Anwendung.

Die eigentliche Anwendung befindet sich im Hauptverzeichnis.


