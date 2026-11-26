"""Render persisted project records to a standalone, offline HTML map."""
import argparse
import json
import os
import re
import tempfile
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

FIT = ("Nie wymaga", "Trochę", "Bardzo", "Brak danych")
MONEY = ("Tak", "Nie", "Brak danych")


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def require_text(row, keys):
    for key in keys.split():
        if not isinstance(row.get(key), str) or not row[key].strip():
            raise ValueError(f"brak pola tekstowego: {key}")


def load_record(path):
    row = read(path)
    require_text(row, "name type status fit money amount facts checked dateKind")
    if row["fit"] not in FIT or row["money"] not in MONEY:
        raise ValueError("nieznana wartość fit lub money")
    for field in ["checked", "date"]:
        value = row.get(field)
        if field == "date" and value is None:
            continue
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError(f"{field}: oczekiwano RRRR-MM-DD")
        date.fromisoformat(value)
    if not isinstance(row.get("links"), list) or not row["links"]:
        raise ValueError("brak źródeł")
    for url in row["links"]:
        parsed = urlsplit(url)
        if parsed.scheme not in ("http", "https") or not parsed.hostname:
            raise ValueError("niepoprawny URL źródła")
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state", type=Path)
    parser.add_argument("output", type=Path, nargs="?")
    args = parser.parse_args()
    meta = read(args.state / "project.json")
    require_text(meta, "project period")
    # Only public report fields enter the shareable file.
    data = {key: meta[key] for key in ("project", "period")}
    data["coverage"] = meta.get("coverage", "")
    rows = []
    for path in sorted((args.state / "records").glob("*.json")):
        try:
            row = load_record(path)
        except (ValueError, TypeError, AttributeError) as exc:
            raise SystemExit(f"{path}: {exc}") from exc
        if args.output is None:
            print(path.stem, row["checked"], row.get("date") or "—", row["status"], row["name"], sep=" | ")
        rows.append({k: row[k] for k in "name type status fit money amount facts checked date dateKind links barrier".split() if k in row})
    if args.output is None:
        return
    data["rows"] = rows
    template = (Path(__file__).resolve().parents[1] / "assets/map.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("<", r"\u003c")
    output = args.output.resolve()
    if output.suffix.lower() != ".html":
        parser.error("plik wynikowy musi mieć rozszerzenie .html")
    with tempfile.NamedTemporaryFile(dir=output.parent, mode="w", encoding="utf-8", delete=False) as temp:
        temp.write(template.replace("__MAP_DATA__", payload))
    os.replace(temp.name, output)
    print(f"{len(rows)} → {output}")


if __name__ == "__main__":
    main()
