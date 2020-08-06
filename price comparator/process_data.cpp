#include "read.hpp"

int main() {
	vector<string> products;
	products = read_products();
	vector<string> prices;
	prices = read_prices();
	//sort_vector(products);
	//sort_vector(prices);
	//print_vector(products);
	//print_vector(prices);

	//sort_vector ordoneaza vectorii separat. Trebuie ordonati atasati
	// unul de altul

	unordered_map<string, string> products_map;
	unordered_map<string, string> prices_map;
	for(int i = 0; i < products.size(); ++i) {
		products_map[products[i]] = prices[i]; 
	}
	for(int i = 0; i < products.size(); ++i) {
		prices_map[prices[i]] = products[i]; 
	}

	//print_vector(products);
	//print_vector(prices);
	sort_vector(prices);
	//cout << "\n\n";
	//print_vector(prices);

	print_map(prices, prices_map);
	//cout << map[products[21]];

	return 0;
}