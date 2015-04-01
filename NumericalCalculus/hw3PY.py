from gmpy2 import mpfr
from math import sqrt
from math import pi

def newEmptyMatrix(rows,columns):
    newMatrix = []
    for i in range(0,rows):
        newRow = []
        for j in range(0,columns):
            newRow.append(0)
        newMatrix.append(newRow)
    return newMatrix

class Matrix:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.matrix = newEmptyMatrix(rows,columns)

    def displayMatrix(self):
        LENGTH = self.getLength()
        for k in range(0,LENGTH+self.columns):
            print("=",end='')
        print("")
        for i in range(0,self.rows):
            for j in range(0,self.columns):
                print(str(self.matrix[i][j])+" ",end='')
            print("")
        for k in range(0,LENGTH+self.columns):
            print("=",end='')
        print("")
    def Add(x):
        b = Matrix(self.rows,self.columns)
        if self.rows == x.rows and self.rows == x.columns:
            for i in range(1,self.rows):
                for j in range(1,self.columns):
                    b.matrix[i][j] = self.matrix[i][j] + x.matrix[i][j]
        return b
    def multiplyMatrix(x):
    	b = Matrix(self.rows,self.columns)
    	if self.columns == x.rows:
    		for i in range(1,self.rows):
        		for j in range(1,x.columns):
        			b.matrix[i][j] = 0;
        			for k in range(1,self.columns):
        				b.matrix[i][j] += self.matrix[i][k] * x.matrix[k][j]

    	return b
    def multiplyScalar(x):
        b = Matrix(self.rows,self.columns)
        for i in range(1,self.rows):
            for j in range(1,x.columns):
                b.matrix[i][j] = self.matrix[i][j] * x
        return b
    def Substract(x):
    	b = Matrix(self.rows,self.columns)
    	if self.rows == x.rows and self.columns == x.columns:
    		for i in range(1,self.rows):
        		for j in range(1,self.columns):
        			b.matrix[i][j] = self.matrix[i][j] - x.matrix[i][j]
    	return b
    def Transpose():
        b = Matrix(self.rows,self.columns)
        for i in range(1,self.columns):
            for j in range(1,self.rows):
                b.matrix[i][j] = self.matrix[j][i];
        return b;
    def norma():
    	m = 0
    	for i in range(0,self.rows):
            mi = 0
            for j in range(1,self.columns):
                mi += abs(self.matrix[j][i]);
            if mi > m:
                m = mi
    	return m

'''
Variables
'''
m = 10
p = 10
eps = 10**(-10)
A = Matrix(m,m)
b = Matrix(m,1)
I = Matrix(m,m)

'''
Methods
'''
def JacobiMethod(p):
    i = 0
    j = 0
    t = mpfr(0)
    mi = mpfr(0)
    er = mpfr(0)
    sigma0 = mpfr(0)
    u0 = 0
    mi = A.norma()
    t = mpfr(2 / mi)

    B = Matrix(m,m)
    bs = Matrix(m,1)
    X = Matrix(m, 1)
    Y = Matrix(m, 1)
    X0 = Matrix(m, 1)

    for k in range(1,p+1): #Might be p
        sigma = t / (p + 1) * mpfr(k)
        As = Matrix(m,m)
        As = A.multiplyScalar(sigma);
        B = I.Substract(As);
        bs = b.multiplyScalar(sigma);
        u = 0;
        for i in range(1,m+1): #Might be m
            X.matrix[i][1] = 0;
        condition = True
        while condition:
            u += 1
            Y = B.multiplyMatrix(X)
            Y = Y.Add(bs)
            sum = mpfr(0)
            for i in range(1,m+1): #Might be m
                for j in range(1,m+1): #Might be m
                    sum += A.matrix[i][j] * (Y.matrix[j][1] - X.matrix[j][1])*(Y.matrix[i][1] - X.matrix[i][1])
            er = sqrt(sum)
            X = Y

            condition = (er > eps)

        if k == 1:
            u0 = u
            X0 = X
            sigma0 = sigma
        elif u < u0:
            u0 = u
            X0 = X
            sigma0 = sigma
    print("\n ====================> Relaxed Jacobi Method <==================== \n")
    print("\n ===> Parametrul optim de relaxare:", sigma0)
    print("Solution:")
    X0.displayMatrix();
    print("\n ===> A * X0 - Test:")
    (A.multiplyMatrix(X0)).displayMatrix()
'''
void metodaGaussSeidel(int p){
	int i, j;
	double er, sigma0;
	int u0;
	double t, mi;
	mi = A.norma();
	t = 2.0 / mi;
	Matrice B(m, m), X(m, 1), Y(m, 1), X0(m, 1);
	for (int k = 1; k <= p; k++)
	{
		double sigma = (2.0 / (p + 1))* (double)k;
		//double sigma = t / (p + 1) * (double)k;
		Matrice As(m, m);

		As = A.inmulteste(sigma);
		B = I.scade(As);
		int u = 0;
		for (i = 1; i <= m; i++)
		{
			X.mat[i][1] = 0;
			Y.mat[i][1] = 0;
		}
		do{
			u++;

			for (i = 1; i <= m; i++)
			{
				double sum1 = 0.0, sum2 = 0.0;
				for (j = 1; j < i; j++)
					sum1 += B.mat[i][j] * Y.mat[j][1];
				for (j = i; j <= m; j++)
					sum2 += B.mat[i][j] * X.mat[j][1];
				Y.mat[i][1] = sum1 + sum2 + b.mat[i][1] * sigma;
			}
			double sum = 0.0;
			for (i = 1; i <= m; i++)
			for (j = 1; j <= m; j++)
			{
				sum += A.mat[i][j] * (Y.mat[j][1] - X.mat[j][1])*(Y.mat[i][1] - X.mat[i][1]);
			}
			er = sqrt(sum);
			X = Y;

		} while (er > eps);
		if (k == 1) { u0 = u; X0 = X; sigma0 = sigma; }
		else if (u < u0) { u0 = u; X0 = X; sigma0 = sigma; }
	}
	cout << "\n ----------->>>>>>>   Metoda Gauss Seidel relaxata >>>>>>>>>>>>>> -------------- \n";
	cout << "\n ----------->>>>>>>   Parametrul optim de relaxare: " << sigma0 << "\n";
	cout << "\n ----------->>>>>>>   Nr pasi: " << u0 << "\n ----------->>>>>>>   Solutia X0: \n";

	X0.Print();
	cout << "\n ----------->>>>>>>   A * X0 \n";

	(A.inmulteste(X0)).Print();

}

void ValoriProprii(){
	int i, j;
	double er, c, s;
	Matrice X(m, m), Y(m, m);
	X = A;
	int u = 0;
	do{

		u++;
		int p = 1, q = 2;
		double maxi = X.mat[p][q];
		for (i = 1; i <= m; i++)
		for (j = i + 1; j <= m; j++)
		if (fabs(X.mat[i][j]) > maxi){
			maxi = fabs(X.mat[i][j]);
			p = i; q = j;
		}
		double fi;
		if (X.mat[p][p] == X.mat[q][q])
		{
			fi = M_PI / 4;
		}
		else {
			fi = 0.5 * atan(2 * X.mat[p][q] / (X.mat[p][p] - X.mat[q][q]));
		}
		s = sin(fi); c = cos(fi);
		Matrice T(m, m), Tt(m, m);
		T = I;
		T.mat[p][p] = c;
		T.mat[q][q] = c;
		T.mat[p][q] = (-1) * s;
		T.mat[q][p] = s;
		Tt = T.transpune();
		Y = Tt.inmulteste(X);
		Y = Y.inmulteste(T);
		X = Y;
		er = 0.0;
		for (i = 1; i <= m; i++)
		for (j = 1; j <= m; j++)
		{
			if (i != j) er += X.mat[i][j] * X.mat[i][j];
		}
		er = sqrt(er);
	} while (er > eps);
	Matrice Z(m, 1);
	for (i = 1; i <= m; i++){
		Z.mat[i][1] = X.mat[i][i];
	}
	cout << "\n <<<<<<<<<<<<<<<<< Valori Proprii >>>>>>>>>>>>>>>>> \n";
	Z.Print();


}
void metodaGradientConjugat(){
	int i, j;
	Matrice X(m, 1), Y(m, 1), r(m, 1), aux(m, 1), v(m, 1);
	for (i = 1; i <= m; i++)
		X.mat[i][1] = 1;
	aux = A.inmulteste(X);
	r = b.scade(aux);
	v = r;
	for (i = 1; i <= m; i++)
	{
		//double sigma = (2.0 / p)* (double)k;
		double sum1 = 0;
		for (j = 1; j <= m; j++)
			sum1 += r.mat[j][1] * r.mat[j][1];
		Matrice av(m, 1);
		av = A.inmulteste(v);
		double sum2 = 0;
		for (j = 1; j <= m; j++)
			sum2 += av.mat[j][1] * v.mat[j][1];

		double  ai = 0;
		ai = sum1 / sum2;
		aux = v.inmulteste(ai);
		aux = aux.adauga(X);
		Y = aux;
		aux = A.inmulteste(Y);
		r = b.scade(aux);
		double sum3 = 0, ci;
		for (j = 1; j <= m; j++)
			sum3 += r.mat[j][1] * r.mat[j][1];
		ci = sum3 / sum1;
		aux = v.inmulteste(ci);
		aux = r.adauga(aux);
		v = aux;
		X = Y;



	}
	cout << "\n ----------->>>>>>>   Metoda Gradient >>>>>>>>>>>>>> -------------- \n";

	X.Print();
	cout << "\n ----------->>>>>>>   A * X0 \n";

	(A.inmulteste(X)).Print();




}
'''
def main():
    i = 0
    j = 0
    for i in range(1,m+1): #Might be m
    	for j in range(1,m+1): #Might be m
            if i == j:
                A.matrix[i][j] = 2
            elif j == i + 1 or i == j + 1:
                A.matrix[i][j] = 1
            else:
                A.matrix[i][j] = 0
    for i in range(1,m+1): #Might be m
        b.matrix[i][1] = 1
    for i in range(1,m+1): #Might be m
    	for j in range(1,m+1): #Might be m
            if (i == j):
                I.matrix[i][j] = 1
            else:
                I.matrix[i][j] = 0
    JacobiMethod(p)
	#//metodaGaussSeidel(p);
	#//metodaGradientConjugat();

main()
