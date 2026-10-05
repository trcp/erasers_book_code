# 元にするイメージ（ROS 2 Jazzy の公式イメージ）
FROM ros:jazzy

# 追加のパッケージをインストールする
RUN apt-get update && apt-get install -y \
    ros-jazzy-turtlesim \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリ（ROS 2 のワークスペース）
WORKDIR /root/ros2_ws

# コンテナを起動したときに実行するコマンド
CMD ["bash"]
