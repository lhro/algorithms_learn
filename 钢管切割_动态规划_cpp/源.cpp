#include<iostream>
#include<vector>
using namespace std;
class RodCut {
	vector<int> p{ 0,1,5,8,9,10,17,17,20,24,30 };//�۸��
	vector<int> r;//����¼
	vector<int> o;//���Ų�����¼��
	int counter;//����������¼������Ľ�����
	int cut(int n) {//�ݹ�����
		if (r[n] >= 0)
			return r[n];
		counter++;
		int q = -1;
		if (n == 0) {
			q = 0;
			counter--;//0�������ܴ���
		}
		else {
			for (int i = 1; i <= n && i <= 10; i++) {
				int temp = p[i] + cut(n - i);
				if (q < temp) {
					q = temp;
					o[n] = i;
				}
			}
		}
		r[n] = q;
		return q;
	}
	int cut(int n, int) {//�Ե�����
		r[0] = 0;
		for (int i = 1; i <= n; i++) {
			counter++;
			for (int j = 1; j <= i && j<=10; j++) {
				int temp = p[j] + r[i - j];
				if (r[i] < temp) {
					r[i] = temp;
					o[i] = j;
				}
			}
		}
		return 0;
	}
	void init(int n) {
		counter = 0;
		r.clear();
		o.clear();
		for (int i = 0; i <= n; i++) {
			r.push_back(-1);
		}
		for (int i = 0; i <= n; i++) {
			o.push_back(0);
		}

	}
	void print_operate(int n) {
		while (n != 0) {
			cout << o[n] << "\t";
			n -= o[n];
		}
	}
public:
	void run(int n) {
		init(n);
		cut(n,0);
		cout << "Maximum profit:" << r[n] << endl;
		cout << "Length of Sub-rod:" << endl;
		print_operate(n);
		cout << endl;

	}
};

int main() {
	RodCut r;
	int i;
	cout << "Total length:" << endl;
	cin >> i;
	if (i < 0) {
		cout << "Bad length!" << endl;
		return 0;
	}
	r.run(i);

}