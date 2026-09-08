# WW2 Ships Cleaner

A small Python project for cleaning and exploring a World War II ships dataset using **Pandas**.

## Purpose

Made for my personal interest in WW2 naval history and to practice **Pandas and data cleaning** using a real-world dataset.

## Tech

* Python
* Pandas

## Structure

```text
WW2 Ships Cleaner/
├── data/
│   ├── raw/
│   │   └── ships.csv
│   └── processed/
│       └── ships_clean.csv
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

## Dataset

Source: Kaggle
License: CC0 1.0 Universal
