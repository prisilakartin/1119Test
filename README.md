# 1119Test

A data science project scaffold following the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) conventions.

## Project structure

```
├── data/
│   ├── external/       # Data from third-party sources
│   ├── interim/        # Intermediate transformed data
│   ├── processed/      # Final, analysis-ready datasets
│   └── raw/            # Immutable original data
├── models/             # Trained and serialized models
├── notebooks/          # Exploratory analysis (number notebooks in order)
├── references/         # Data dictionaries and project references
├── reports/
│   └── figures/        # Generated charts and figures
├── src/project_name/
│   ├── data/           # Data loading and validation
│   ├── features/       # Feature engineering
│   ├── modeling/       # Training and prediction
│   └── visualization/  # Plotting helpers
├── tests/              # Automated tests
├── config/             # Project configuration
├── params.yaml         # Experiment parameters
├── pyproject.toml      # Python project metadata and dependencies
└── Makefile            # Common development commands
```

## Getting started

1. Create and activate a virtual environment.
2. Install the project: `pip install -e ".[dev]"`
3. Put original datasets in `data/raw/`. Keep raw data unchanged.
4. Add notebooks to `notebooks/` using names such as `01-exploration.ipynb`.
5. Implement reusable code in `src/project_name/` and tests in `tests/`.

## Reproducibility

- Keep random seeds and experiment settings in `params.yaml`.
- Do not commit private, sensitive, or large datasets; use an appropriate data store.
- Record data sources and definitions in `references/`.
- Save generated plots in `reports/figures/`.

## Development

Run tests with `pytest` and lint with `ruff check .`.
