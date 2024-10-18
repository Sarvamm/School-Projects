// Q1. Task: Create a program that defines variables of different data types to store the following  information: 
// o Your age (an integer). 
// o Your height in meters (a float or double). 
// o Your first initial (a character). 
// o Whether you are a student (a boolean). 
// o Your favorite quote (a string). 
// Instructions: 
// • Declare variables of appropriate data types to store each piece of information. 
// • Initialize each variable with a value. 
// • Output all the values to the console using cout. 

#include <iostream>
using namespace std;

// int main() {
//     int age = 25;
//     float height = 1.78;
//     char initial = 'S';
//     bool isStudent = true;
//     string favoriteQuote = "The journey of a thousand miles begins with a single step.";
    
//     cout << "Age: " << age << endl;
//     cout << "Height: " << height << " meters" << endl;
//     cout << "First Initial: " << initial << endl;
//     cout << "Student Status: " << (isStudent ? "Yes" : "No") << endl;
//     cout << "Favorite Quote: " << favoriteQuote << endl;

//     return 0;
// }

// Part 2: What happens if you try to assign a floating-point number to an integer variable? Why? 

// The decimal part is truncated and only the integer value is stored in the variable as it is an int 
// type variabe, note that the compiler doesnt round the decimal, so 89.99 will be stored as 89, not 90.
// int main(){
//     int x = 89.99;
//     cout<<x; // prints 89
// }

// Q2. Task: Write a C++ program that performs the following operations: 
// o Declare three integer variables: a, b, and c. 
// o Assign the value to a and b. 
// o Swap the values of a and b using a temporary variable c. 
// o Print the values of a and b before and after the swap. 
// Instructions: 
// • Declare and initialize the variables as described.

// int main(){
//     int a,b,c;
//     a = 25; b = 35;
//     cout << "Before Swapping Values: a = "<<a<<", b = " << b <<endl;
//     c = a; a = b; b = c; 
//     cout << "Before Swapping Values: a = "<<a<<", b = " << b <<endl;
// }

// Q3. Create a C++ Program: 
// o Your program should prompt the user to enter two integers. 
// o The program should perform and display the results of the following operations on  the entered numbers: 
// ▪ Arithmetic Operations: Addition, subtraction, multiplication, division, and  modulus. 
// ▪ Relational Operations: Compare the two numbers to determine which is  greater, lesser, or if they are equal. 
// int main(){
//     int num1, num2;
//     cout << "Enter first number: ";
//     cin >> num1;
//     cout << "Enter second number: ";
//     cin >> num2;
    
//     cout << "Addition: " << num1 + num2 << endl;
//     cout << "Subtraction: " << num1 - num2 << endl;
//     cout << "Multiplication: " << num1 * num2 << endl;
//     cout << "Division: " << num1 / num2;

//     cout << "\nRelational Operations: " << endl;
//     cout << (num1 > num2? num1 : num2) << " is greater" << endl;
//     cout << (num1 < num2? num1 : num2) << " is lesser" << endl;
//     cout << (num1 == num2? "Both numbers are equal" : "Numbers are not equal") << endl;
// }

// Follow-Up Questions 
// What happens if the user enters zero as the second number and the program attempts to  divide by zero? How can this be handled?  
// int main(){
//     int num1, num2;
//     cout << "Enter first number: ";
//     cin >> num1;
//     cout << "Enter second number: ";
//     cin >> num2;

    
//     cout << "Addition: " << num1 + num2 << endl;
//     cout << "Subtraction: " << num1 - num2 << endl;
//     cout << "Multiplication: " << num1 * num2 << endl;

//     if (num2 == 0){
//     cout << "Error: Division by zero is not defined";}
//     else{
//         cout << "Division: " << num1 / num2 << endl;
//     }
    
// }