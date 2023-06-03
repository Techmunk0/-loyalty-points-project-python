import os

for i in range(1, 125):
    os.system(f"curl -X POST http://localhost:5000/{i}")
    os.system(f"curl -X POST http://localhost:5000/{i}/add_points/100")
    os.system(f"curl -X POST http://localhost:5000/{i}/add_points/100")
    os.system(f"curl -X POST http://localhost:5000/{i}/add_points/100")
    os.system(f"curl -X POST http://localhost:5000/{i}/add_points/100")
    os.system(f"curl -X POST http://localhost:5000/{i}/add_points/100")
