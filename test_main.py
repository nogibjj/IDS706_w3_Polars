"""
Test goes here, for four functions

"""

from main import *
import os


def test_generate_iris_polars():
    generate_iris_polars()
    assert os.path.exists("./Iris.csv"), "Iris.csv file not found"


def test_load_iris_polars():
    iris_data = load_iris_polars("./Iris.csv")
    assert isinstance(iris_data, pl.DataFrame), "Data loaded is not a Polars DataFrame"
    assert len(iris_data) == 150, "Loaded data has the wrong number of rows"


def test_desc_iris():
    sample_data = pl.DataFrame(
        {
            "sepal length (cm)": [5.1, 4.9, 4.7],
            "sepal width (cm)": [3.5, 3.0, 3.2],
            "petal length (cm)": [1.4, 1.3, 1.5],
            "petal width (cm)": [0.2, 0.4, 0.3],
            "target": [0, 1, 2],
        }
    )
    description = desc_iris(sample_data)
    assert isinstance(
        description, pl.DataFrame
    ), "Data is not in the format of a Polars DataFrame"
    assert len(description) >= 8, "Missing key summary in the data"


def test_visual_iris():
    sample_data = pl.DataFrame(
        {
            "sepal length (cm)": [5.1, 4.9, 4.7],
            "sepal width (cm)": [3.5, 3.0, 3.2],
            "target": [0, 1, 2],
        }
    )
    visual_iris(sample_data)
    assert os.path.exists("iris_scatter_plot.png"), "Scatter plot image file not found"
    assert os.path.exists("iris_box_plot.png"), "Box plot image file not found"
    assert os.path.exists("iris_histogram.png"), "Histogram image file not found"
