#!/usr/bin/env python3
import os
import json
from datetime import date

try:
    import yaml
except ImportError:
    raise SystemExit("pip install pyyaml")

COVERAGE_SCORE = {
    "none": 0,
    "partial": 40,
    "good": 70,
    "high": 90
}

def find_meta_files(root="mitre/techniques"):
    for root_dir, _, files in os.walk(root):
        if "meta.yml" in files:
            yield os.path.join(root_dir, "meta.yml")

def main():
    techniques = []

    for meta_path in find_meta_files():
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = yaml.safe_load(f)

        tid = meta.get("technique_id")
        name = meta.get("technique_name", "")
        coverage = meta.get("coverage_status", "none").lower()
        score = COVERAGE_SCORE.get(coverage, 10)

        if not tid:
            continue

        techniques.append({
            "techniqueID": tid,
            "techniqueName": name,
            "score": score,
            "comment": f"coverage={coverage}"
        })

    layer = {
        "name": "attack-hunting-lab – Coverage",
        "versions": {
            "layer": "4.5",
            "navigator": "4.9.0"
        },
        "domain": "enterprise-attack",
        "description": "Coverage generated from attack-hunting-lab meta.yml files",
        "filters": {
            "platforms": ["Windows"]
        },
        "sorting": 0,
        "layout": {
            "layout": "side",
            "showID": True,
            "showName": True
        },
        "hideDisabled": False,
        "techniques": techniques,
        "gradient": {
            "colors": ["#ffffff", "#ff9999", "#ffcc66", "#66ff66"],
            "minValue": 0,
            "maxValue": 100
        },
        "metadata": [
            {"name": "generated", "value": date.today().isoformat()}
        ]
    }

    os.makedirs("artifacts", exist_ok=True)
    out = "artifacts/mitre_navigator_layer.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(layer, f, indent=2)

    print(f"[OK] Navigator layer generated: {out}")
    print(f"[OK] Techniques included: {len(techniques)}")

if __name__ == "__main__":
    main()
