# WW2 Ships Cleaner

A small data project for cleaning, exploring, and analyzing a World War II ships dataset using **Pandas and Power BI**.

## Purpose

Made for my personal interest in WW2 naval history and to practice **data cleaning, exploration, and visualization** using a real-world dataset.

## Tech

* Python
* Pandas
* Power BI

## Structure

```text
WW2 Ships Cleaner/

├── data/
│   ├── raw/
│   │   └── ships.csv
│   └── processed/
│       └── ships_clean.csv
│
├── powerbi/
│   └── WW2_Ships_Dashboard.pbix
│
├── cleaner.py
├── requirements.txt
└── README.md
```

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python cleaner.py
```

The raw dataset is kept unchanged in `data/raw/`, while the cleaned dataset is saved in `data/processed/`.

The processed dataset was then used in **Power BI** to explore and analyze WW2 naval data through interactive visualizations.

## Dataset

Source: Kaggle

License: CC0 1.0 Universal
