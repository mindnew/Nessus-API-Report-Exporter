# Nessus-API-Report-Exporter
Simple python3 script to download reports from Nessus in csv or xml formats.

**How it works** <br/>
Run this .py file with python3:<br/>
<code>python Nessus-API-Report-Exporter.py</code> 
<br/>
<br/>
Then follow the instructions indicated in the script

<code>python Nessus-API-Report-Exporter.py
Enter Nessus IP address and port (example: 10.0.0.1:8834)
10.1.31.6:8834
Input Access key:
3578hbvcb56c731dfbv7318dbe40hf5fdfgcb7nkjlkkhjhdsf6745jo5bvlfv52
Input Secret key:
231567vb676877lmbvcxxnb60hjv44356bmll4352dbv0jhmvb5k69bf90fghfdf
Connected to 10.1.31.6:8834
id name
2 Trash
3 My Scans

--------------------
Enter folder id:
3
--------------------
id name
200 Scan1
231 Scan2
244 Scan3
266 Scan4
--------------------
Enter scan id (You can enter multiple scans. Example: 105,240,196).
231
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
File saved as: Scan2.csv
---DONE!---
</code> 
