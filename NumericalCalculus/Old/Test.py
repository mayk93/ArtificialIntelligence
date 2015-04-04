import gmpy2
from gmpy2 import mpz,mpq,mpfr,mpc

Scale = 1

def main():
    n = 5
    p = 7;

    L = initializeMatrix(n+1)
    U = initializeMatrix(n+1)
    Q = initializeMatrix(n+1)
    R = initializeMatrix(n+1)

    x = initializeVector(n+1)
    b = initializeVector(n+1)

    LU(n,L,U,x,b,p)
'''
    print(Cholesky(n, L, x, b, p))

    print(QR(n, Q, R, x, b, p))
'''

def initializeMatrix(n):
    matrix = []
    for i in range(0,n):
        row = []
        for j in range(0,n):
            row.append(mpfr(0))
        matrix.append(row)
    return matrix

def initializeVector(n):
    vector = []
    for i in range(0,n):
        vector.append(mpfr(0))
    return vector

def CheckSolution(x,n,A,b):
    print("Checking:")
    for i in range(1,n+1):
        s = mpfr(0)
        for j in range(1,n+1):
            s =  s + A[i][j]*x[j]
        s = substraction(s,b[i])
        print(i,"->",s)
    print("Done.")

def Factorial(n):
    f = mpfr(1)
    for i in range(2,n+1):
        f = f*mpfr(i)
    return f

def Combinations(n,k):
    return Factorial(n)/(Factorial(n-k)*Factorial(k))

def CreateMatrix(n,p):
    A = initializeMatrix(n+1)
    b = initializeVector(n+1)
    l = mpfr(1)
    for i in range(1,n+1):
        for j in range(1,n+1):
            A[i][j] = Combinations(p+j-1,i-1)
    AT = TransposeMatrix(A,n)
    for i in range(1,n+1):
        b[i] = mpfr(0)
        for j in range(1,n+1):
            b[i] = b[i] + A[i][j]
    return (A,b)

def TransposeMatrix(A,n):
    AT = initializeMatrix(n+1)
    for i in range(1,n+1):
        for j in range(0,n+1):
            AT[i][j] = A[j][i]
    return AT

def MultiplyMatrix(A,B,n):
    C = initializeMatrix(n+1)
    for i in range(1,n+1):
        for j in range(1,n+1):
            sum = mpfr(0)
            for k in range(1,n+1):
                sum = sum + A[i][k] * B[k][j]
                C[i][j] = sum
    return C

def LU(n,L,U,x,b,p):
    print(">0")
    C = initializeMatrix(n+1)
    y = initializeVector(n+1)
    (C,b) = CreateMatrix(n,p) #Check C to be properly made
    CT = TransposeMatrix(C,n)
    A = MultiplyMatrix(CT,C,n)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i < j:
                L[i][j] = mpfr(0)
            if i > j:
                U[i][j] = mpfr(0)
            if i == j:
                U[i][j] = mpfr(1)
    for i in range(1,n+1):
        L[i][1] = A[i][1]
        U[1][j] = A[1][j] / L[1][1]
    for k in range(2,n+1):
        for i in range(k,n+1):
            sum1 = mpfr(0)
            for t in range(1,k):
                sum1 = sum1+L[i][t]*U[t][k]
            L[i][k] = A[i][k]-sum1
            sum2 = mpfr(0)
            for t in range(1,k):
                sum2 = sum2+L[k][t]*U[t][i]
            U[k][i] = A[k][i] - sum2 / L[k][k]
    y[1] = b[1]/L[1][1]
    for i in range(2,n+1):
        sum = mpfr(0)
        for k in range(1,i):
            sum = sum + L[i][k]*y[k]
        y[i] = (b[i]-sum)/L[i][i]
    x[n]=y[n]
    for i in range(n-1,0,-1):
        sum = mpfr(0)
        for k in range(i+1,n+1):
            sum = sum+U[i][k]*x[k]
        x[i] = y[i]-sum
    '''
    '''
    matrixPrint(L,"L")
    matrixPrint(U,"U")
    matrixPrint(A,"A")
    matrixPrint(MultiplyMatrix(L,U,n),"Multiply")
    CheckSolution(x,n,A,b)
'''
    public void LU(int n, BigDecimal[][] L, BigDecimal[][] U, BigDecimal[] x, BigDecimal[] b, int p) {




        CheckSolution(x,n,A,b);
    }

    public void Cholesky(int n, BigDecimal[][] L, BigDecimal[] x, BigDecimal[] b, int p) {
        BigDecimal[][] C = new BigDecimal[n + 1][n + 1];
        BigDecimal[] y = new BigDecimal[n + 1];
        CreateMatrix(n, C, b, p);
        BigDecimal[][] CT = TransposeMatrix(C, n);
        BigDecimal[][] A = MultiplyMatrix(CT, C, n);
        for (int j = 1; j <= n; j++) {
            BigDecimal s = new BigDecimal("0");
            for (int k = 1; k < j; k++) {
                s = s.add(L[j][k].multiply(L[j][k]));
            }

            L[j][j] = BigMath.sqrt(A[j][j].subtract(s), Scale);

            for (int i = j + 1; i <= n; i++) {
                BigDecimal s2 = new BigDecimal("0");
                for (int k = 1; k < j; k++) {
                    s2 = s2.add(L[i][k].multiply(L[j][k]));
                }
                L[i][j] = (A[i][j].subtract(s2)).divide(L[j][j], Scale, RoundingMode.HALF_UP);
            }
        }
        y[1] = b[1].divide(L[1][1], Scale, RoundingMode.HALF_UP);
        for (int i = 2; i <= n; i++) {
            BigDecimal sum = BigDecimal.valueOf(0.0);
            for (int k = 1; k <= i - 1; k++)
                sum = sum.add(L[i][k].multiply(y[k]));
            y[i] = (b[i].subtract(sum)).divide(L[i][i], Scale, RoundingMode.HALF_UP);
        }
        x[n] = y[n].divide(L[n][n], Scale, RoundingMode.HALF_UP);
        for (int i = n - 1; i > 0; i--) {
            BigDecimal sum = BigDecimal.valueOf(0.0);
            for (int k = i + 1; k <= n; k++)
                sum = sum.add(L[k][i].multiply(x[k]));
            x[i] = (y[i].subtract(sum)).divide(L[i][i], Scale, RoundingMode.HALF_UP);
        }
        CheckSolution(x,n,A,b);
    }

    public void QR(int n, BigDecimal[][] Q, BigDecimal[][] R, BigDecimal[] x, BigDecimal[] b, int p) {
        BigDecimal[][] C = new BigDecimal[n + 1][n + 1];
        BigDecimal[] y = new BigDecimal[n + 1];
        CreateMatrix(n, C, b, p);
        BigDecimal[][] CT = TransposeMatrix(C, n);
        BigDecimal[][] A = MultiplyMatrix(CT, C, n);
        BigDecimal sumi = BigDecimal.valueOf(0.0);
        for (int i = 1; i <= n; i++)
            sumi = sumi.add(A[i][1].multiply(A[i][1]));
        R[1][1] = BigMath.sqrt(sumi, Scale);
        for (int i = 1; i <= n; i++)
            Q[i][1] = A[i][1].divide(R[1][1], Scale, RoundingMode.HALF_UP);
        for (int k = 2; k <= n; k++) {
            for (int j = 1; j <= k - 1; j++) {
                BigDecimal sum = BigDecimal.valueOf(0.0);
                for (int i = 1; i <= n; i++)
                    sum = sum.add(A[i][k].multiply(Q[i][j]));
                R[j][k] = sum;
            }
            BigDecimal sum1 = BigDecimal.valueOf(0.0);
            for (int i = 1; i <= n; i++)
                sum1 = sum1.add(A[i][k].multiply(A[i][k]));
            BigDecimal sum2 = BigDecimal.valueOf(0.0);
            for (int i = 1; i <= k - 1; i++)
                sum2 = sum2.add(R[i][k].multiply(R[i][k]));

            R[k][k] = BigMath.sqrt(sum1.subtract(sum2), Scale);
            for (int i = 1; i <= n; i++) {
                BigDecimal sump = BigDecimal.valueOf(0.0);
                for (int t = 1; t <= k - 1; t++)
                    sump = sump.add(R[t][k].multiply(Q[i][t]));
                Q[i][k] = (A[i][k].subtract(sump)).divide(R[k][k], Scale, RoundingMode.HALF_UP);
            }
        }
        for (int i = 1; i <= n; i++) {
            BigDecimal sumj = BigDecimal.valueOf(0.0);
            for (int j = 1; j <= n; j++)
                sumj = sumj.add(Q[j][i].multiply(b[j]));
            y[i] = sumj;
        }
        x[n] = y[n].divide(R[n][n], Scale, RoundingMode.HALF_UP);
        for (int i = n - 1; i > 0; i--) {
            BigDecimal sum = new BigDecimal(0);
            for (int j = i + 1; j <= n; j++) {
                sum = sum.add(R[i][j].multiply(x[j]));
            }
            x[i] = (y[i].subtract(sum)).divide(R[i][i], Scale, RoundingMode.HALF_UP);
        }
        CheckSolution(x,n,A,b);
    }
'''

def matrixPrint(matrix,name):
    print(name)
    for row in matrix:
        print(row)

def substraction(a,b):
    return a-b

if __name__ == "__main__":
    main()
