/* File: 05_getTempHumid_HTS221.cpp
 * Author: Philippe Latu
 * Source: https://github.com/platu/libsensehat-cpp
 *
 * This example program collects measures from the HTS221 Humidity sensor.
 * This sensor provides temperature measurement in degrees Celsius and relative
 * humidity measurement.
 *
 * Function prototypes:
 * 
 * double senseGetTemperatureFromHumidity();
 *   ^- temperature
 *
 * double senseGetHumidity();
 *   ^- humidity
 *
 * The program simply calls the two functions
 */

#include <iostream>
#include <thread>
#include <chrono>
#include <iomanip>
#include <sensehat.h>

using namespace std;

void GetData() {

	double HumidTemp, PressureTemp, Humid, Pressure;
	
	while (true)
	{
		cout << "-------------------------------" << endl
			<< "Sense Hat initialization Ok." << endl;
		senseClear();

		HumidTemp = senseGetTemperatureFromHumidity();
		cout << fixed << setprecision(2) << "Temp (from humidity) = " << HumidTemp << "°C" << endl;

		Humid = senseGetHumidity();
		cout << fixed << setprecision(0) << "Humidity = " << Humid << "% rH" << endl;

		PressureTemp = senseGetTemperatureFromPressure();
		cout << fixed << setprecision(2) << "Temp (from pressure) = " << PressureTemp << "°C" << endl;

		Pressure = senseGetPressure();
		cout << fixed << setprecision(0) << "Pressure = " << Pressure << "hPa" << endl;

		std::this_thread::sleep_for(10s);
	}
}

int main() {

	if(senseInit()) {
		std::thread first(GetData);
		first.join();
	}

	senseShutdown();

	return EXIT_SUCCESS;
}