#define VERSION "1.0"

#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

int main(int argc, char **argv){
	
	if (argc < 3){
		cout<<"Infomedia "<<VERSION<<" - Para uso junto con Mediainfo.\n";
		cout<<"Error, faltan datos. Uso:\ninfomedia archivo campo\n";
		return 1;
	}
	ifstream entrada(argv[1]);
	if (!entrada.good()){
		cout<<"Error al abrir el archivo.\n";
		return 1;
	}
	string s;
	while (getline(entrada, s)){
		if (s.find(argv[2]) != string::npos){
			string res = s.substr(s.find(": ")+2, s.length());
			cout<<res<<endl;
			break;
		}
	}
	return 0;
}
