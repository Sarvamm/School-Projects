/* Q1. Determine if a year is a leap year. 
 
Branch/Semester: CSE/I                                                         
Date of submission:14-10-2024 
Question: Write a C++ program that checks if a given year is a leap year. A year is a 
leap year if it is divisible by 4 but not divisible by 100, except when it is divisible by 
400. 
 
 
Example Input: 2024 
Output: 
2024 is a leap year.*/

// #include<iostream>
// using namespace std;

// bool isLeapYear(int year) {
//     if (year % 400 == 0)
//         return true;
//     else if (year % 100 == 0)
//         return false;
//     else if (year % 4 == 0)
//         return true;
//     else
//         return false;
// }

// int main() {
//     int year;
//     cout << "Enter a year: ";
//     cin >> year;
//     if (isLeapYear(year)){
//         cout << year << " is a leap year.";
//     }
//     else {
//         cout << year << " is not a leap year.";
//     }
//     return 0;
// }

/*Q2. Calculate electricity bill based on usage.
Question: Write a C++ program to calculate an electricity bill based on the number
of units consumed. The tariff plan is as follows:

For the first 100 units: ₹5/unit
For the next 100 units: ₹6/unit
For units above 200: ₹7/unit
The user should input the total units consumed, and the program should calculate
and print the total bill.
Example Input: 150 units
Output:
Your electricity bill is ₹800.*/

// #include<iostream>
// using namespace std;

// int main() {
//     int units;
//     cout << "Enter the total units consumed: ";
//     cin >> units;

//     int bill = 0;  
//     if (units > 0 && units <= 100) {
//         bill = 5 * units;
//     } 
//     else if (units > 100 && units <= 200) {
//         bill = 5 * 100 + 6 * (units - 100);
//     } 
//     else if (units > 200) {
//         bill = 5 * 100 + 6 * 100 + 7 * (units - 200);
//     } 
//     else {
//         cout << "Invalid units" << endl;
//         return 1;  
//     }

//     cout << "Your electricity bill is ₹" << bill << endl;

//     return 0;
// }

/*### Q3. Convert temperature and classify it.

Question: Write a C++ program to convert a temperature from Celsius to
Fahrenheit. Classify the temperature as hot, warm, or cold based on the following
conditions:

Temp > 40°C: Hot
20°C <= Temp <= 40°C: Warm
Temp < 20°C: Cold
Formula for Conversion:
To convert Celsius to Fahrenheit, use the formula:
F=(9/5×C)+32
Where:
F is the temperature in Fahrenheit.
C is the temperature in Celsius.
Example Input: 30°C
Output:
The temperature in Fahrenheit is 86°F, classified as warm.*/

// #include<iostream>
// using namespace std;

// int main() {
//     float celsius, fahrenheit;
//     cout << "Enter the temperature in Celsius: ";
//     cin >> celsius;
//     fahrenheit = (9.0/5.0) * celsius + 32;
//     string classification;
//     if (celsius > 40) {
//         classification = "hot";
//     } 
//     else if (celsius >= 20 && celsius <= 40) {
//         classification = "warm";
//     } 
//     else {
//         classification = "cold";
//     }
//     cout << "The temperature in Fahrenheit is " << fahrenheit << "°F, classified as " << classification << "." << endl;

//     return 0;
// }

// #include<iostream>
// using namespace std;

// int main() {
//     char ch;
    
//     cout << "Enter a character: ";
//     cin >> ch;
    
//     if (ch >= 'A' && ch <= 'Z') {
//         cout << ch << " is an uppercase letter." << endl;
//     }
//     else if (ch >= 'a' && ch <= 'z') {
//         cout << ch << " is a lowercase letter." << endl;
//     }
//     else if (ch >= '0' && ch <= '9') {
//         cout << ch << " is a digit." << endl;
//     }
//     else {
//         cout << ch << " is a special symbol." << endl;
//     }

//     return 0;
// }


// Factorial of a number
// #include<iostream>
// using namespace std;

// int main() {
//     int n, factorial = 1;
    
//     cout << "Enter a number: ";
//     cin >> n;
    
//     if (n < 0) {
//         cout << "Factorial is not defined for negative numbers." << endl;
//     } else {
//         for (int i = 1; i <= n; i++) {
//             factorial *= i;
//         }
//         cout << "The factorial of " << n << " is " << factorial << "." << endl;
//     }
    
//     return 0;
// }
// #include<iostream>
// using namespace std;

// int main() {
//     int num, sum = 0;
    
//     cout << "Enter a number: ";
//     cin >> num;

//     do {
//         sum += num % 10;  // Add the last digit to sum
//         num /= 10;        // Remove the last digit
//     } while (num != 0);

//     cout << "The sum of the digits is " << sum << "." << endl;
    
//     return 0;
// }
// #include<iostream>
// using namespace std;

// int main() {
//     int N, a = 0, b = 1, next = 0, count = 1;

//     cout << "Enter the value of N: ";
//     cin >> N;

//     cout << "The first " << N << " Fibonacci numbers are: " << endl;

//     while (count <= N) {
//         if (count == 1) {
//             cout << a << " ";  // First Fibonacci number
//         } else if (count == 2) {
//             cout << b << " ";  // Second Fibonacci number
//         } else {
//             next = a + b;
//             cout << next << " ";
//             a = b;
//             b = next;
//         }
//         count++;
//     }

//     cout << endl;

//     return 0;
// }
#include<iostream>
using namespace std;

int main() {
    int num, i;
    bool isPrime = true;

    cout << "Enter a number: ";
    cin >> num;

    if (num <= 1) {
        isPrime = false;
    } else {
        for (i = 2; i <= num / 2; i++) {
            if (num % i == 0) {
                isPrime = false;
                break;
            }
        }
    }

    if (isPrime) {
        cout << num << " is a prime number." << endl;
    } else {
        cout << num << " is not a prime number." << endl;
    }

    return 0;
}
