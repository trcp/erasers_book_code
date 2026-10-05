# 本書のサンプルコード

「これを読めばあなたもロボットを動かせるようになる！〜ロボット初学者のための Linux・コマンドライン・ROS 入門〜」（eR@sers）に出てくるプログラムをまとめたリポジトリです。

- 本書のサンプルコード：https://github.com/trcp/erasers_book_code

## ディレクトリの構成

| ディレクトリ | 内容 | 対応する章 |
| --- | --- | --- |
| `python/what_is_python/` | C 言語と Python の比較 | 第16章 |
| `python/python_env/` | はじめてのスクリプト | 第17章 |
| `python/python_basics/` | Python の基本 | 第18章 |
| `python/python_class/` | クラスとモジュール（`module_example/` はモジュールの例、`exercise_debug_*.py` は誤りを直す練習問題で、そのままでは正しく動かない） | 第19章 |
| `python/answers/` | 第18章・第19章の練習問題の解答例（`ex18_2_1.py` は練習問題 18.2 (1)） | 付録C |
| `shellscript/` | シェルスクリプト（`setup_dev.sh` は第10章の実践、`env/` は第9章の環境変数の例） | 第9章・第10章 |
| `cmake_hello/` | C 言語のプログラムを CMake でビルドする例 | 第11章 |
| `docker/` | Dockerfile・compose.yaml・Dev Containers の例 | 第15章 |
| `docker_ros/` | Docker で ROS 2 の開発環境を作る例 | 補章1 |
| `ros2_ws/` | ROS 2 のワークスペース | 第23章〜第30章、補章2・3 |

`python/` のファイル名の先頭の番号は、本文に出てくる順番です。
番号の後ろの名前は、本文のリストのキャプションに書かれたファイル名と同じです（例：本文の `none.py` は `python/python_basics/10_none.py`）。

## Python のプログラム

第18章・第19章のプログラムは、第17章で作る `~/py_practice` にコピーして、`python3 ファイル名` で実行します。
`07_import_as.py` は NumPy を使うので、第17章の仮想環境を有効にしてから実行してください。

## ROS 2 のワークスペース（`ros2_ws/`）

`ros2_ws/src/` には、次の 3 つのパッケージがあります。

| パッケージ | 内容 | 対応する章 |
| --- | --- | --- |
| `my_package` | Python のノード・launch ファイル（Python と XML）・設定ファイル・URDF | 第24章〜第30章、補章3 |
| `my_interfaces` | 自分で定義したメッセージ型とサービスの型 | 第24章 |
| `my_cpp_package` | C++ のノード | 補章2 |

Ubuntu 24.04 と ROS 2 Jazzy で、次のようにビルドします。

```bash
git clone https://github.com/trcp/erasers_book_code.git
cd erasers_book_code/ros2_ws
source /opt/ros/jazzy/setup.bash
rosdep install -i --from-path src --rosdistro jazzy -y
colcon build --symlink-install
source install/local_setup.bash
ros2 run my_package talker
```

本の手順どおりに `~/ros2_ws` を使う場合は、`src/` の中のパッケージを `~/ros2_ws/src/` にコピーしてからビルドしてください。

## 本との関係

ここにあるファイルは、本の原稿（`book/samples/` と本文）から書き出したものです。
本の原稿を直したときは、こちらも合わせて直してください。
