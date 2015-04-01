#include <math.h>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#define _USE_MATH_DEFINES
using namespace std;
#define M_PI 3.1415926

class Matrice{
public:
	long double mat[101][101];
	int linii, coloane;

	Matrice(int i, int j){
		linii = i;
		coloane = j;
		for (i = 1; i <= linii; i++)
		for (j = 1; j <= coloane; j++)

			mat[i][j] = 0;
	}
	void Print();
	Matrice adauga(Matrice& x);
	Matrice inmulteste(Matrice& x);
	Matrice inmulteste(double x);
	Matrice scade(Matrice& x);
	void copiaza(Matrice& x);
	Matrice transpune();
	double norma();

};
void Matrice::copiaza(Matrice& x){
	linii = x.linii;
	coloane = x.coloane;
	for (int i = 1; i <= linii; i++)
	for (int j = 1; j <= coloane; j++)
		mat[i][j] = x.mat[i][j];
}

Matrice Matrice::adauga(Matrice& x){
	Matrice b(linii, coloane);
	if (linii == x.linii && coloane == x.coloane)
	{
		for (int i = 1; i <= linii; i++)
		for (int j = 1; j <= coloane; j++)
		{
			b.mat[i][j] = mat[i][j] + x.mat[i][j];
		}
	}
	return b;
}
Matrice Matrice::scade(Matrice& x){
	Matrice b(linii, coloane);
	if (linii == x.linii && coloane == x.coloane)
	{
		for (int i = 1; i <= linii; i++)
		for (int j = 1; j <= coloane; j++)
		{
			b.mat[i][j] = mat[i][j] - x.mat[i][j];
		}
	}
	return b;
}
Matrice Matrice::inmulteste(Matrice& x){
	Matrice b(linii, x.coloane);
	if (coloane == x.linii)
	{
		for (int i = 1; i <= linii; i++)
		for (int j = 1; j <= x.coloane; j++)
		{
			b.mat[i][j] = 0;
			for (int k = 1; k <= coloane; k++)
			{
				b.mat[i][j] += mat[i][k] * x.mat[k][j];
			}
		}
	}
	return b;
}
Matrice Matrice::inmulteste(double x){
	Matrice b(linii, coloane);
	for (int i = 1; i <= linii; i++)
	for (int j = 1; j <= coloane; j++)
	{

		b.mat[i][j] = mat[i][j] * x;
	}
	return b;
}
Matrice Matrice::transpune(){
	Matrice b(coloane, linii);
	for (int i = 1; i <= coloane; i++)
	for (int j = 1; j <= linii; j++)
	{
		b.mat[i][j] = mat[j][i];
	}
	return b;
}
double Matrice::norma(){
	double m = 0;
	for (int i = 1; i <= linii; i++)
	{
		double mi = 0;
		for (int j = 1; j <= coloane; j++)
		{
			mi += fabs(mat[j][i]);
		}
		if (mi > m) m = mi;
	}
	return m;
}



void Matrice::Print(){
	cout << setprecision(6);
	for (int i = 1; i <= linii; i++)
	{
		for (int j = 1; j <= coloane; j++)
			cout << left << setw(6) << mat[i][j] << " ";
		cout << "\n";
	}
}
int m = 10, p = 10;
double eps = 0.00000001;
Matrice A(m, m), b(m, 1), I(m, m);

void metodaJacobi(int p){
	int i, j;
	double t, mi, er, sigma0;
	int u0;
	mi = A.norma();
	t = 2 / mi;
	Matrice B(m, m), bs(m, 1), X(m, 1), Y(m, 1), X0(m, 1);
	for (int k = 1; k <= p; k++)
	{
		double sigma = t / (p + 1) * (double)k;
		Matrice As(m, m);
		As = A.inmulteste(sigma);
		B = I.scade(As);
		bs = b.inmulteste(sigma);
		int u = 0;
		for (i = 1; i <= m; i++)
			X.mat[i][1] = 0;
		do{
			u++;
			Y = B.inmulteste(X);
			Y = Y.adauga(bs);
			double sum = 0;
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
		//B.Print();
		//cout<<"\n";
	}
	cout << "\n ----------->>>>>>> Metoda Jacobi relaxata >>>>>>>>>>>>>> -------------- \n";
	cout << "\n ----------->>>>>>>   Parametrul optim de relaxare: " << sigma0 << "\n";
	cout << "\n ----------->>>>>>>   Nr pasi: " << u0 << "\n ----------->>>>>>>   Solutia X0: \n";

	X0.Print();
	cout << "\n ----------->>>>>>>   A * X0 \n";

	(A.inmulteste(X0)).Print();



}

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

int main()
{
	int  i, j;
	for (i = 1; i <= m; i++)
	for (j = 1; j <= m; j++){
		if (i == j) A.mat[i][j] = 2;
		else if (j == i + 1 || i == j + 1) A.mat[i][j] = 1;
		else A.mat[i][j] = 0;
	}

	for (i = 1; i <= m; i++)
		b.mat[i][1] = 1;
	for (i = 1; i <= m; i++)
	for (j = 1; j <= m; j++){
		if (i == j) I.mat[i][j] = 1;
		else I.mat[i][j] = 0;
	}
	//A.Print();
	cout << "\n";
	//metodaJacobi(p);
	//metodaGaussSeidel(p);
	//metodaGradientConjugat();
	ValoriProprii();

	return 0;
}
