import math
import csv

def nol(f):
    """ノルムを計算する関数"""
    return math.sqrt(sum(x**2 for x in f))

def nai(f, g):
    """内積を計算する関数"""
    return sum(f[i] * g[i] for i in range(len(f)))

def sokan(f, g):
    """相関係数を計算する関数"""
    return nai(f, g) / (nol(f) * nol(g))

# メイン処理
if __name__ == "__main__":
    sogoSokan = []
    zikoSokan = []

    try:
        # ファイルオープン
        with open("WB09.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            # 有効桁数を設定

            # ここに相互相関関数を求めるソースを記述
            # 必要に応じてf, gの値を設定し、相関係数を計算
            # 例: writer.writerow([sokan(f, g)])

            # sin,cosの値を配列に格納
            degrees = [i for i in range(0, 360)]
            sin = [math.sin(math.radians(angle)) for angle in degrees]

            # τ(range)の範囲で相互相関係数を求める
            for t in range(-360,361):
                sinT = [math.sin(math.radians(angle + t)) for angle in degrees]
                cosT = [math.cos(math.radians(angle + t)) for angle in degrees] # τを足した状態で格納

                sogoSokan.append(round(sokan(sin, cosT), 3)) # 相互相関係数を求める
                zikoSokan.append(round(sokan(sin, sinT), 3)) # 自己相関係数を求める
            result = list(zip(list(range(-360, 361)),sogoSokan,zikoSokan))
            writer = csv.writer(csvfile)
            writer.writerows(result)


    except FileNotFoundError:
        print("ファイルがありません")
