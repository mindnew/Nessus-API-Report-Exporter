# Nessus-API-Report-Exporter
Simple python3 script to download reports from Nessus in csv or xml formats.

**How it works** <br/>
Run this .py file with python3:<br/>
<code>python Nessus-API-Report-Exporter.py</code> 
<br/>
<br/>
Then follow the instructions indicated in the script:<br/>
$ python Nessus-API-Report-Exporter.py
```
id name
2 Trash
3 My Scans
5 Discovery
9 regular scan
--------------------
Enter folder id:
3
--------------------
id name
216 10.227.97.65_ASTRA
191 Alpha_tst
173 AZON
175 Logistika_AlfaGO
--------------------
Enter scan id (You can enter multiple scans. Example: 105,240,196).
173
Choose the report format (1-2):
1. CSV
2. Nessus
1
{"token":"ce2d5454077808c03a10bea77ceb384baa3a5410882ca5d00b33da3d01207c37","file":1911844196}
--------------------
Wait untill the report will be prepared
{"status":"loading"}
{"status":"ready"}
--------------------
Checking export status: {"status":"ready"}
--------------------
File saved as: AZON_08-05-2023.csv
---DONE!---
```
