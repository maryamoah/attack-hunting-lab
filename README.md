# attack-hunting-lab

![Status](https://img.shields.io/badge/status-active-success)
![Platform](https://img.shields.io/badge/platform-Windows%20AD-blue)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-red)
![License](https://img.shields.io/badge/license-MIT-green)
![CI](https://github.com/maryamoah/attack-hunting-lab/actions/workflows/validate.yml/badge.svg)

> A practical **MITRE ATT&CK–aligned threat hunting lab** focused on real SOC workflows — not theory.

This repository documents **how to hunt adversary behaviour** using structured hypotheses, portable detections, and measurable coverage, with an initial focus on **Windows Active Directory environments**.

---

## 🔍 What this repo is (and isn’t)

### ✅ This is
- A **threat-hunting lab**, not just detection rules
- MITRE ATT&CK–aligned by design
- Built around **analyst thinking** (hypothesis → hunt → validation → outcome)
- Tool-agnostic at the detection layer (Sigma as source of truth)

### ❌ This is not
- A dump of noisy alerts
- Vendor-locked detections
- A “set and forget” rules repo

---

## 🎯 Current scope

| Area | Focus |
|----|----|
| Platform | Windows Active Directory |
| Framework | MITRE ATT&CK (Enterprise) |
| Detection logic | Sigma |
| Hunting & operations | Wazuh |
| Validation | Manual + lab-based testing |

---

## 🧠 Repository structure

```
attack-hunting-lab/
├── mitre/
│   └── techniques/
│       └── <TECHNIQUE>_<NAME>/
│           ├── meta.yml
│           ├── hunts/
│           ├── detections/
│           │   └── sigma/
│           └── validation/
├── scripts/
│   ├── validate_repo.py
│   └── build_navigator_layer.py
├── tooling/
│   └── wazuh/
│       └── mapping.md
├── artifacts/
│   └── mitre_navigator_layer.json
└── README.md
```

---

## 🧪 Implemented techniques

| Technique | Name | Coverage |
|---------|------|---------|
| T1059.001 | PowerShell | Partial |
| T1021.001 | Remote Desktop Protocol (RDP) | Partial |

---

## 🗺️ MITRE ATT&CK coverage map

Navigator layer is auto-generated from metadata.

**File:**  
```
artifacts/mitre_navigator_layer.json
```

### How to view
1. Open https://mitre-attack.github.io/attack-navigator/
2. Click **Open Existing Layer**
3. Upload `mitre_navigator_layer.json`

---

## ⚙️ Getting started

```bash
python scripts/validate_repo.py
python scripts/build_navigator_layer.py
```

---

## 📌 Design principles

- One technique, one platform, one telemetry model
- Hunts before alerts
- Detections must be explainable
- Validation is mandatory
- Coverage must be measurable

---

## 🔮 Roadmap

- Password spraying (T1110)
- WMI lateral movement (T1047)
- Disable security tools (T1562.001)
- Improved RDP baselining
- Linux & cloud scopes (separate branches)

---

## 🤝 Contributions

This repo is opinionated by design.  
Contributions should align with MITRE ATT&CK and include a hunt hypothesis and validation steps.

---

## 📜 License
MIT License
