from pathlib import Path
from datetime import date

# Base structure
base = Path("AI-ML-Works")

dirs = [
    base / "Week-01-Python-Data-Foundations" / "Day-1-Python-Refresher",
    base / "Week-01-Python-Data-Foundations" / "Day-2-NumPy-Deep-Dive",
    base / "Week-01-Python-Data-Foundations" / "Day-3-Pandas-ML-I",
    base / "Week-02-Math-for-ML" / "Day-1-Linear-Algebra",
    base / "Week-02-Math-for-ML" / "Day-2-Calculus-Gradients",
    base / "daily-logs",
]

# Create all directories (parents + no error if exists)
for d in dirs:
    d.mkdir(parents=True, exist_ok=True)  # uses Path.mkdir with parents/exist_ok pattern [web:12][web:17]

# Create today’s daily log file
today_str = date.today().isoformat()  # e.g. 2025-12-17 [web:18]
log_file = base / "daily-logs" / f"{today_str}.md"
log_file.touch(exist_ok=True)  # create file if it doesn't exist [web:18]
