import truss
from pathlib import Path
import requests

tr = truss.load("./falcon_7b_truss")
command = tr.docker_build_setup(build_dir=Path("./falcon_7b_truss"))
print(command)