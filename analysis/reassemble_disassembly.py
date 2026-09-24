#!/usr/bin/env python3
from pathlib import Path
import gzip
import hashlib

HERE = Path(__file__).resolve().parent
parts = [
    HERE / "macho-disassembly.txt.gz.part01",
    HERE / "macho-disassembly.txt.gz.part02",
    HERE / "macho-disassembly.txt.gz.part03",
]
gz_path = HERE / "macho-disassembly.txt.gz"
txt_path = HERE / "macho-disassembly.txt"

with gz_path.open("wb") as out:
    for part in parts:
        out.write(part.read_bytes())

with gzip.open(gz_path, "rb") as src, txt_path.open("wb") as out:
    out.write(src.read())

for path in (gz_path, txt_path):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print(f"{digest}  {path.name}")
