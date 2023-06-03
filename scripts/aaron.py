import os

for i in range(1, 125):
    os.system(f"curl -X POST http://localhost:5000/{i}/spend_points/500")
