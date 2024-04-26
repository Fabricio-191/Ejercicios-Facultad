#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <malloc.h>
#include <limits>
#include <cmath>
#include <map>
using namespace std;

const int N = 10;
const float Infinity = numeric_limits<int>::max();

class City {
	public:
		double x;
		double y;

		City(double ax, double ay) {
			this->x = ax;
			this->y = ay;
		}

		float distanceTo(City city) {
			return sqrt(
				pow(this->x - city.x, 2) +
				pow(this->y - city.y, 2)
			);
		}

		bool operator < (City city) const {
			return this->x < city.x && this->y < city.y;
		}

		bool operator == (City city) const {
			return this->x == city.x && this->y == city.y;
		}
};

class Path {
	public:
		City* cities;
		int citiesQty;
		float distance;

		Path(City* cities, int citiesQty, float distance){
			this->cities = cities;
			this->citiesQty = citiesQty;
			this->distance = distance;
		}

		bool hasCity(City city) {
			for(int i = 0; i < this->citiesQty; i++){
				if(city == this->cities[i]) return true;
			}

			return false;
		}

		Path operator + (City city){
			City* newCities = (City*) malloc(sizeof(City) * (this->citiesQty + 1));
			for(int i = 0; i < this->citiesQty; i++){
				newCities[i] = this->cities[i];
			}
			newCities[this->citiesQty] = city;

			City lastCity =  this->cities[this->citiesQty - 1];
			float newDistance = this->distance + lastCity.distanceTo(city);

			return Path(newCities, this->citiesQty + 1, newDistance);
		}

		void print(){
			printf("Distance: %.2f   Cities: [ ", this->distance);
			for(int i = 0; i < this->citiesQty - 1; i++){
				printf("(%.0f, %.0f), ", this->cities[i].x, this->cities[i].y);
			}
			printf("(%.0f, %.0f) ]\n", this->cities[this->citiesQty - 1].x, this->cities[this->citiesQty - 1].y);
		}
};

class TravellingSalesman {
	public:
		City* cities;
		City* start;
		Path* solution;
		float lessDistance;

		TravellingSalesman(City* cities){
			this->cities = cities;
		};

		Path resolve(City start) {
			Path startPath = Path({ &start }, 1, 0);
			this->start = &start;
			this->lessDistance = Infinity;

			this->process(startPath);

			return *this->solution;
		}

		void process(Path path){
			if(path.citiesQty == N){
				path = path + *this->start;

				if (path.distance < this->lessDistance){
					this->solution = &path;
					this->lessDistance = path.distance;
				}
			}else if(path.distance < this->lessDistance){
				for(int i = 0; i < N; i++){
					City city = this->cities[i];

					if(!path.hasCity(city)){
						this->process(path + city);
					}
				}
			}
		}

		void baseCase(){
			Path path = Path({ this->start }, 1, 0);

			for(int i = 0; i < N - 1; i++){
				City closestCity = this->cities[0];
				float closestDistance = Infinity;

				for(int j = 0; j < N; j++){
					City city = this->cities[j];

					if(!path.hasCity(city)){
						float distance = path.cities[path.citiesQty - 1].distanceTo(city);

						if(distance < closestDistance){
							closestDistance = distance;
							closestCity = city;
						}
					}
				}

				path = path + closestCity;
			}

			path = path + *this->start;
			this->solution = &path;
			printf("Caso base: \n");
			this->solution->print();
		}
};

City* generateCities(){
	srand(time(NULL));
	City* cities = (City*) malloc(sizeof(City) * N);

	for(int i = 0; i < N; i++){
		cities[i] = City(
			(double)(rand() % 100),
			(double)(rand() % 100)
		);
	}

	return cities;
}

int main(){
	City* cities = generateCities();
	TravellingSalesman salesman = TravellingSalesman(cities);

	Path solution = salesman.resolve(cities[0]);
	printf("Mejor solucion: \n");
	solution.print();

	return 0;
}