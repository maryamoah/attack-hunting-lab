#!/usr/bin/env python3
import os, sys
try:
    import yaml
except ImportError:
    raise SystemExit("pip install pyyaml")

REQUIRED = ["technique_id","technique_name","tactic","platforms","coverage_status","last_reviewed"]

def main():
    ok = True
    for root, _, files in os.walk("mitre/techniques"):
        if "meta.yml" in files:
            p = os.path.join(root, "meta.yml")
            meta = yaml.safe_load(open(p, encoding="utf-8")) or {}
            missing = [k for k in REQUIRED if k not in meta]
            if missing:
                ok = False
                print(f"[FAIL] {p} missing {missing}")
    if ok:
        print("[OK] Repo structure valid")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(main())
