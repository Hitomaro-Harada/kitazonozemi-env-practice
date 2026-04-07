from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris


def main() -> None:
    # 画像の保存先フォルダを用意する
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    # scikit-learn に入っている Iris データセットを読み込む
    iris = load_iris()

    # 扱いやすいように pandas の DataFrame に変換する
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    # 数値ラベルを species 名に変換して列として追加する
    df["species"] = [iris.target_names[i] for i in iris.target]

    # species ごとの平均値を表示する
    print("=== Iris dataset summary ===")
    print(df.groupby("species").mean())

    # 散布図を作る
    plt.figure(figsize=(8, 6))

    # species ごとに色分けして点を打つ
    for species in iris.target_names:
        subset = df[df["species"] == species]
        plt.scatter(
            subset["sepal length (cm)"],
            subset["petal length (cm)"],
            label=species,
            alpha=0.7,
        )

    # グラフのタイトルや軸ラベルを設定する
    plt.title("Iris: sepal length vs petal length")
    plt.xlabel("sepal length (cm)")
    plt.ylabel("petal length (cm)")
    plt.legend()
    plt.tight_layout()

    # 作成した画像を outputs フォルダに保存する
    plt.savefig(output_dir / "iris_scatter.png")
    print("\nSaved figure to outputs/iris_scatter.png")


if __name__ == "__main__":
    main()
