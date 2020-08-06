#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

vector<string> read_products();
vector<string> read_prices();
void sort_vector(vector<string>& );
void print_vector(vector<string> );
void print_map(vector<string> , unordered_map<string, string> );