/* Box-Muller法による正規乱数プログラム */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14159

double RAND(void);
double BOXMULLER(void);

int main(int argc, char* argv[])
{
        FILE *fp;

        int n;                      /* データの数 */
        int i;                      /* 繰り返し変数 */
        double ran;

        double sum = 0.0;
        double ave;

        srand((unsigned int)time(NULL)); // 現在時刻の情報で初期化
        
        if (NULL == (fp = fopen("rand.csv", "w")))
        {
                printf("file open error!!");
                exit(1);
        }

        printf("\nデータの数を入れてください。 n=");
        scanf("%d", &n);

        /* 乱数の表示 */
        for (i = 0; i < n; i++)
        {
                if ((i % 5) == 0)
                        printf("\n");
                else
                        printf("\t");

                ran = BOXMULLER();

                printf("%3d>%10.6lf", i, ran);

                fprintf(fp, "%3d,%10.6lf\n", i, ran);
                sum = sum + fabs(ran);
        }

        printf("\n雑音の平均 %10.6lf / %d,%10.6lf\n", sum, n, sum / (double)n);
        
        fclose(fp);
        getchar();
        getchar();

        return 0;
}

/* 0以上1未満の一様乱数を発生させる関数 */

double RAND(void)
{
        double x = rand();

        x = (x + 0.000001) / (RAND_MAX + 0.1);

        return x;
}

/* 正規乱数を発生させる関数(Box-Muller法) */

double BOXMULLER(void)
{
        double mu = 0;       /* 平均μ */
        double sigma = 1;    /* 分散σ^2 */

        return (sqrt(sigma) * sqrt(-2 * log(RAND())) * sin(2 * PI * RAND()) + mu);
}
