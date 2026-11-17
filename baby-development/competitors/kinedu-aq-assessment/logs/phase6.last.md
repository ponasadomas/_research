COMPLETED: 2,064/2,064 assessment requests, all HTTP 200.  
Covered ages 0–48 and all 196 age-area sweeps.  
Collected 2,033 ascending rows and 31 descending controls.  
Proxy country NL; sequential requests; 2.0-second sleeps.  
Saved [area-table.csv](area-table.csv) and [AREA-TABLE.md](AREA-TABLE.md).  
Found 36 decreases across 33 age-area pairs; exact K values documented.  
Order controls matched all 24 exposed numeric pairs; 7 pairs remained hidden.  
Repeated area/count checks: 5,462 comparisons, zero conflicts.  
19 age-area sweeps never exposed numeric months; omissions preserved.  
Added [collector](scripts/collect_area_table.py) and [builder](scripts/build_area_table.py).  
[Validation](logs/phase6-validation.json) passed hashes, payloads, headers and pacing checks.  
Recipe: select age and served area IDs, count Yes answers, then look up K.