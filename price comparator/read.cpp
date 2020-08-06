#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include "read.hpp"
using namespace std;

ifstream f("products");
ifstream g("prices");

vector<string> read_products() {
	vector<string> products;
	//string product;
	char dummy[1501];
	while(f.getline(dummy, 1500)) {
		//cout << dummy << '\n';
		string product(dummy);
		//cout << product << '\n';
		products.push_back(product);
	}
	return products;
}

vector<string> read_prices() {
	vector<string> prices;
	char dummy[1501];
	while(g.getline(dummy, 1500)) {
		string price(dummy);
		prices.push_back(price);
	}
	return prices;
}

bool price_compare(string s1, string s2) {
	//only for prices vector
	int len1 = 0;
	int len2 = 0;
	
	while(s1[len1] <= '9' && s1[len1] >= '0') {
		++len1;
	}

	while(s2[len2] <= '9' && s2[len2] >= '0') {
		++len2;
	}

	if(len1 == len2) {
		for(int i = 0; i < s1.length(); ++i) {
			if(s1[i] != s2[i]) {
				return s1[i] < s2[i];
			}
		}
	}
	
	return len1 < len2;
}

bool compare_with_switch(string s1, string s2) {
	if(s1.compare(s2) > 0) {
		return 0;
	}
	return 1;
}

void sort_vector(vector<string>& vect) {
	//sorts product and price vector
	if(vect[0][0] <= '9' && vect[0][0] >= '0') {
		sort(vect.begin(), vect.end(), price_compare);
	}
	else
		sort(vect.begin(), vect.end(), compare_with_switch);
}

void print_vector(vector<string> vect) {
	//prints a vector
	for(int i = 0; i < vect.size(); ++i) {
		cout << vect[i] << '\n';
	}
}

void print_map(vector<string> vect, unordered_map<string, string> map) {
	for(int i = 0; i < vect.size(); ++i) {
		cout << map[vect[i]] << '\n';
		cout << vect[i] << '\n';
	}
}