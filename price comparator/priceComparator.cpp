#include <iostream>

using namespace std;

int main() {

	system("python3 get_data_from_website.py");
	//system("sleep 0.5s");
	system("g++ process_data.cpp read.cpp -o processData");
	system("./processData");
	return 0;
}