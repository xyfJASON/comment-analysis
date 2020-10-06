#include<cstdlib>
#include<cstdio>
#include<string>

#ifdef WIN32
#include<direct.h>
#else
#include<unistd.h>
#endif

int main(){
	char buf[250];
	chdir(getcwd(buf, sizeof buf));
	// system("ls");
	system("python begin.py");
	system("python classifier.py");
}