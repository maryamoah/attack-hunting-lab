# attack-hunting-lab

![Status](https://img.shields.io/badge/status-active-success)
![Platform](https://img.shields.io/badge/platform-Windows%20AD-blue)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-red)
![License](https://img.shields.io/badge/license-MIT-green)
![CI](https://github.com/maryamoah/attack-hunting-lab/actions/workflows/validate.yml/badge.svg)

> **Most detections alert. This repository teaches how to hunt.**

`attack-hunting-lab` is a practical, MITRE ATT&CK–aligned threat hunting repository built around **real SOC workflows**.  
It focuses on *how analysts think*: forming hypotheses, validating telemetry, tuning noise, and measuring coverage.

Initial scope targets **Windows Active Directory environments**, with clean separation for future Linux and cloud expansion.

---

## 🔍 What this repository is (and isn’t)

### ✅ This *is*
- A **threat hunting lab**, not just detection rules
- Explicitly aligned to **MITRE ATT&CK (Enterprise)**
- Built around **analyst reasoning** (hypothesis → hunt → validation → outcome)
- Detection logic expressed in **Sigma** for portability
- Coverage that is **measurable and visualised**

### ❌ This is *not*
- A noisy alert dump
- Vendor-locked detection content
- A “set and forget” rules repository

---

## 🎯 Scope and assumptions

| Area | Focus |
|----|----|
| Platform | Windows Active Directory |
| Framework | MITRE ATT&CK (Enterprise) |
| Detection logic | Sigma |
| Hunting & operations | Wazuh |
| Validation | Manual + lab-based testing |

The scope is **intentional**:  
one platform → one telemetry model → meaningful hunts.

---

## 🧭 How to use this repository

1. Pick a **MITRE technique**
2. Read the **hunt hypothesis**
3. Verify **required telemetry** exists
4. Execute the hunt and record outcomes
5. Promote to detection once noise is understood

This keeps detection engineering grounded in evidence.

---

## 🧠 Repository structure

```
attack-hunting-lab/
├── mitre/
│   └── techniques/
│       └── <TECHNIQUE>_<NAME>/
│           ├── meta.yml              # Scope & coverage
│           ├── hunts/                # Hypotheses & steps
│           ├── detections/
│           │   └── sigma/            # Portable detections
│           └── validation/           # How to test safely
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

Coverage improves as hunts mature into validated detections.

---

## 🗺️ MITRE ATT&CK coverage map

Coverage is tracked via an **auto-generated MITRE Navigator layer**.

**File:**
```
artifacts/mitre_navigator_layer.json
```

### View the layer
1. Open https://mitre-attack.github.io/attack-navigator/
2. Click **Open Existing Layer**
3. Upload `mitre_navigator_layer.json`

Colour intensity reflects **coverage maturity**, not ambition.

---

## ⚙️ Getting started

Validate repository structure:
```bash
python scripts/validate_repo.py
```

Generate MITRE Navigator layer:
```bash
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
- Linux and cloud scopes (separate branches)

---

## 🤝 Contributions

This repository is intentionally opinionated.

Contributions should:
- Align with MITRE ATT&CK
- Include a hunt hypothesis
- Document required telemetry
- Be reproducible

---

## 📜 License
MIT License

---

*Built from real SOC investigations and blue-team operations.*
