[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/0xhzx/IDS706-w1_Mini_Project/actions/workflows/cicd.yml)
# Template for Python projects 

## IDS-706 2023 fall Week 2 Mini-project_Pandas_Script
Requirements
- Python script using Polars for descriptive statistics
- Read a dataset (CSV or Excel)
- Generate summary statistics (mean, median, standard deviation)
- Create at least one data visualization


# Target
Analyze the iris features and summary them in both form and plots, using Polars (the latest version) instead of Pandas!

# Dataset
Iris dataset from sklearn

# CI/CD
- Including `make install`, `make lint`, `make test`, `make format` and `make deploy`
- `make lint` uses pylint with configuration in `.pylintrc`
- Unit test cover 100%

# Result screenshot

## CI/CD process
![Alt text](image-1.png)

## Summary statistics 
![Summary](image.png)

## Data Visualization

### Scatter plot
![scatter_plot](iris_scatter_plot.png)
### Box plot
![box_plot](iris_box_plot.png)
### Histogram plot
![histogram_plot](iris_histogram.png)
