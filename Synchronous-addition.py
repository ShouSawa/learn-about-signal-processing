import numpy as np
import pandas as pd

def main():
    sampling_points = 128 #サンプリング点
    n_value = [10,100,1000,10000] #同期加算の回数


    #信号Sの作成
    A = 1 #振幅
    f = 1 #周波数
    t = np.linspace(0,1,sampling_points,True)
    S = A*np.sin(2*np.pi*f*t)

    ave = 0 #平均
    s = 1 #標準偏差
    all_SOn = []
    all_N_prime = []

    for n in n_value:
        sumS = np.zeros(sampling_points) #同期加算用の配列

        for j in range(n):
            N = np.random.normal(ave,s,sampling_points) #正規乱数の作成
            SIn = np.add(S,N) #合成信号SInの作成
            sumS = np.add(sumS,SIn) #同期加算する

        SOn = sumS / n #出力信号SOnの作成z
        all_SOn.append(SOn) 
        N_prime = sum(np.abs(np.subtract(S,SOn))) #合成信号Sと出力信号SOnとの差の絶対値の総和
        all_N_prime.append(N_prime)
    
    all_SOn.insert(0,S)
    n_value.insert(0,'S')

    # 配列を転置
    all_SOn_T = np.array(all_SOn).T.tolist() 
    all_N_prime_T = np.array(all_N_prime).T.tolist() 
    print(all_SOn_T)
    print(all_N_prime)

    # グラフ1の作成
    abscissa = [i for i in range(0, sampling_points)] # 横軸のサンプリング点
    df1 = pd.DataFrame(data=np.round(all_SOn_T, decimals=3), index=abscissa, columns=n_value) # dataframeの作成

    # グラフ2の作成
    n_value.remove('S')
    df2 = pd.DataFrame(data=np.round(all_N_prime_T, decimals=3), index=n_value, columns=["減衰後の雑音N'n"]) # dataframeの作成

    # Excelへの書き込み
    with pd.ExcelWriter('./wb05.xlsx') as writer:
        df1.to_excel(writer, sheet_name='sheet1')
        df2.to_excel(writer, sheet_name='sheet2')


if __name__ == "__main__":
    main()
