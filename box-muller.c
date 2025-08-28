/* Box-Muller�@�ɂ�鐳�K�����v���O���� */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14159

double RAND(void);
double BOXMULLER(void);

int main(int argc, char* argv[])
{
        FILE *fp;

        int n;                      /* �f�[�^�̐� */
        int i;                      /* �J��Ԃ��ϐ� */
        double ran;

        double sum = 0.0;
        double ave;

        srand((unsigned int)time(NULL)); // ���ݎ����̏��ŏ�����
        
        if (NULL == (fp = fopen("rand.csv", "w")))
        {
                printf("file open error!!");
                exit(1);
        }

        printf("\n�f�[�^�̐������Ă��������B n=");
        scanf("%d", &n);

        /* �����̕\�� */
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

        printf("\n�G���̕��� %10.6lf / %d,%10.6lf\n", sum, n, sum / (double)n);
        
        fclose(fp);
        getchar();
        getchar();

        return 0;
}

/* 0�ȏ�1�����̈�l�����𔭐�������֐� */

double RAND(void)
{
        double x = rand();

        x = (x + 0.000001) / (RAND_MAX + 0.1);

        return x;
}

/* ���K�����𔭐�������֐�(Box-Muller�@) */

double BOXMULLER(void)
{
        double mu = 0;       /* ���σ� */
        double sigma = 1;    /* ���U��^2 */

        return (sqrt(sigma) * sqrt(-2 * log(RAND())) * sin(2 * PI * RAND()) + mu);
}
