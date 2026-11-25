"""Descarga los datasets del taller desde la GitHub Release `data-v1` a `docs/workshop/data/`."""

from pathlib import Path
import urllib.request

BASE_URL = "https://github.com/IA-P1-BCN/juanCarlos-investigacion-clustering/releases/download/data-v1"
FILES = ("mushrooms.csv", "credit_card.csv")
DATA_DIR = Path(__file__).resolve().parent / "data"


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        dest = DATA_DIR / name
        if dest.exists() and dest.stat().st_size > 0:
            print(f"✓ Ya existe: {dest}")
            continue
        url = f"{BASE_URL}/{name}"
        print(f"↓ Descargando {name} desde GitHub Release data-v1...")
        urllib.request.urlretrieve(url, dest)
        print(f"✓ Guardado: {dest} ({dest.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
