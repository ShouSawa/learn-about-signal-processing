import random
import math
import csv
import time

PI = 3.14159

def box_muller():
    # 平均0、分散1の正規分布
    mu = 0
    sigma = 1
    r = math.sqrt(-2 * math.log(random.random())) * math.sin(2 * PI * random.random())
    return sigma * r + mu

def generate_uniform():
    # -3から3までの範囲の一様乱数
    return random.uniform(-3, 3)

def main():
    n = 10000  # 乱数生成のデータ数を1万個に設定

    count_normal = [0] * 120  # 正規乱数のカウント用リスト
    count_uniform = [0] * 120  # 一様乱数のカウント用リスト

    # 出力ファイルを開く
    with open("rand_histogram.csv", mode="w", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(["Index", "Normal_Random", "Uniform_Random"])

        # 乱数生成とヒストグラムデータ集計
        for i in range(n):
            # 正規乱数の生成
            normal_rand = box_muller()
            normal_index = int((normal_rand / 0.05) + 60)
            if 0 <= normal_index < 120:
                count_normal[normal_index] += 1
            
            # 一様乱数の生成
            uniform_rand = generate_uniform()
            uniform_index = int((uniform_rand / 0.05) + 60)
            if 0 <= uniform_index < 120:
                count_uniform[uniform_index] += 1

            # ファイルへの書き込み
            writer.writerow([i, f"{normal_rand:.6f}", f"{uniform_rand:.6f}"])

    # ヒストグラムデータの出力
    with open("histogram_data.csv", mode="w", newline="") as hist_fp:
        hist_writer = csv.writer(hist_fp)
        hist_writer.writerow(["Range", "Normal_Count", "Uniform_Count"])

        for i in range(120):
            range_value = (i - 60) * 0.05
            hist_writer.writerow([range_value, count_normal[i], count_uniform[i]])

    print("ヒストグラムデータが'rand_histogram.csv'と'histogram_data.csv'に出力されました。")

if __name__ == "__main__":
    random.seed(int(time.time()))
    main()
