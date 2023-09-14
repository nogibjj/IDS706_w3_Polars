"""
Main cli or app entry point
"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import polars as pl


def generate_iris_polars():
    iris = load_iris()
    data_iris = pl.DataFrame(iris.data, schema=iris.feature_names)
    target = pl.DataFrame(iris.target, schema=["target"])
    df = data_iris.hstack(target)
    df.write_csv("./Iris.csv")


def load_iris_polars(path):
    iris_data = pl.read_csv(path)
    return iris_data


def desc_iris(data_iris):
    print(data_iris.describe())
    return data_iris.describe()


def visual_iris(data_iris):
    sepal_length = data_iris["sepal length (cm)"]
    sepal_width = data_iris["sepal width (cm)"]
    target = data_iris["target"]
    sepal_length_list = sepal_length.to_list()
    sepal_width_list = sepal_width.to_list()
    target_list = target.to_list()

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(
        sepal_length_list,
        sepal_width_list,
        c=target_list,
        cmap="viridis",
    )
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.title("Scatter Plot of Sepal Length vs. Sepal Width")
    plt.colorbar(scatter, label="Iris Species")
    plt.show()
    plt.savefig("iris_scatter_plot.png")

    plt.figure(figsize=(8, 6))
    _ = plt.boxplot(
        [sepal_length_list, sepal_width_list], labels=["Sepal Length", "Sepal Width"]
    )
    plt.xlabel("Features")
    plt.ylabel("Values")
    plt.title("Box Plot of Sepal Length and Sepal Width")
    plt.savefig("iris_box_plot.png")
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.hist(
        [sepal_length_list, sepal_width_list],
        bins=10,
        edgecolor="black",
        label=["Sepal Length", "Sepal Width"],
    )
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram of Sepal Length and Sepal Width")
    plt.legend()
    plt.savefig("iris_histogram.png")
    plt.show()


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    generate_iris_polars()
    cur_path = "./Iris.csv"
    data = load_iris_polars(cur_path)
    desc_iris(data)
    visual_iris(data)
