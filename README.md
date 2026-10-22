# 🌐 Global Lethal Autonomous Weapons Systems (LAWS) Open Dataset

[![Sync & Report](https://github.com/a-vip/laws-open-dataset/actions/workflows/dataset-sync-and-report.yml/badge.svg)](https://github.com/a-vip/laws-open-dataset/actions/workflows/dataset-sync-and-report.yml)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.placeholder.svg)](https://zenodo.org)
[![Author: Avi Perera](https://img.shields.io/badge/Author-Avi_Perera-blue.svg)](https://aviperera.com)

An open, programmatic dataset indexing technical specifications, operational deployments, and International Humanitarian Law (IHL) compliance evaluations for **Lethal Autonomous Weapons Systems (LAWS)**, loitering munitions, quadruped UGVs, and algorithmic targeting architectures.

Curated and maintained by **[Avi Perera](https://aviperera.com)** — AI Governance Researcher, LAWS Expert, and Founder of [SovDash](https://sovdash.com).

---

## 📊 Dataset Access

The dataset is programmatically refreshed weekly and distributed in both JSON and CSV formats under [`data/`](data/):

| Format | File Path | Records | Direct Download |
| :--- | :--- | :---: | :--- |
| **JSON** | [`data/laws_systems.json`](data/laws_systems.json) | `100+` | [Download JSON](https://raw.githubusercontent.com/a-vip/laws-open-dataset/main/data/laws_systems.json) |
| **CSV** | [`data/laws_systems.csv`](data/laws_systems.csv) | `100+` | [Download CSV](https://raw.githubusercontent.com/a-vip/laws-open-dataset/main/data/laws_systems.csv) |

### Schema Fields
- `id`: Unique identifier
- `system_name`: Official platform designation (e.g. *V-BAT MQ-35*, *Switchblade 600*)
- `system_type`: Tactical classification (*Loitering Munition*, *UAS*, *UGV*, *Combat Humanoid*, *Targeting AI*)
- `manufacturer_developer`: Defense contractor or research institute
- `country_of_origin`: Sovereign state of manufacture
- `autonomy_assessment`: Meaningful Human Control (MHC) & targeting autonomy profile
- `canonical_dossier_url`: Full verified research dossier at **[aviperera.com](https://aviperera.com)**

---

## 📚 Academic & Policy Citation

To cite this dataset in research papers, policy briefs, or UN working documents, use the `CITATION.cff` metadata:

```bibtex
@dataset{perera2026laws_dataset,
  author    = {Perera, Avi},
  title     = {Global Lethal Autonomous Weapons Systems (LAWS) & Military AI Specifications Dataset},
  year      = {2026},
  publisher = {Zenodo},
  url       = {https://aviperera.com},
  note      = {Data-as-Code repository: https://github.com/a-vip/laws-open-dataset}
}
```

---

## ⚡ Autonomous Reporting Engine

This repository runs a scheduled [GitHub Action](.github/workflows/dataset-sync-and-report.yml) every Sunday to synchronize newly verified defense dossiers from **[aviperera.com](https://aviperera.com)** and dispatch an executive intelligence brief to `workwithavip@gmail.com`.

---

## 📄 License

Dataset licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
Code under MIT License.
