for sensor in camera lidar imu; do
    echo "checking $sensor ..."
done

# ワイルドカードで、CSV ファイルを 1 つずつ処理する
for f in *.csv; do
    echo "$f: $(wc -l < "$f") lines"
done

# ブレース展開で 1〜3 の数字を使う
for i in {1..3}; do
    echo "trial $i"
done
