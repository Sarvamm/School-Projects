//  Finding the Maximum of Two Numbers 
//Description: Write a function that receives three numbers and returns the larger one.
#include <iostream>
using namespace std;

// int maxOfThree(int a, int b, int c) {
//     if ((a > b) && (a > c)) {
//         return a;
//     }
//     else if ((b > c ) && (b > a)) {
//         return b;
//     }
//     else {
//         return c;
//     }
// }

// int main() {
//     cout<<maxOfThree(3, 5, 9);
// }

#include <iostream>
using namespace std;

// int sumOfArray(int arr[], int size) { 
//     int sum = 0;
//     for (int i = 0; i < size; i++) {
//         sum += arr[i];
//     }
//     return sum;
// }

// int main() {
//     int arr[] = {5, 8, 23, 9, 11};
//     int size = sizeof(arr) / sizeof(arr[0]); 
//     cout << "Sum of array elements: " << sumOfArray(arr, size); 
//     return 0;
// }
/*Create a function that takes a number, adds 10 to it, and displays the result inside the 
function. The function should use "call by value," so the original number outside the function should 
remain unchanged. Use 5 as the initial number. */

// addTen(int &x){
//     x += 10;
//     cout << "Number after adding 10: " << x<< endl;
// }
// int main(){
//     int number = 5;
//     addTen(number);
//     cout << "initial number after modification: " << number;
//     return 0;
// }

/*Write a C++ program to define a Student class that includes private attributes for the student's name, 
age, and grade. check if student is an adult (age 18 or older). Demonstrate these functionalities by 
creating a student object in the main function, displaying the initial details and checking if the student 
is an adult. */
class Student{
  private:
    string name; int age; char grade;
  public:
     void setData(string n, int a, char g)
       { name = n; age = a; grade = g; }
     void displayData(){
        cout<<"Initial Information:"<<endl;
        cout<<"Name: "<<name<<endl;
        cout<<"Age: "<<age<<endl;
        cout<<"Grade: "<<grade<<endl;
     }
     void isAdult(){
        cout<< "Checking if student is an adult: "<<endl;
        if    (age>=18) {   cout<<"Student is an adult."<<endl   ;}
        else    {   cout<<"Student is not an adult."<<endl;    }    }};
int main(){Student A; A.setData("Alice", 20, 'A'); A.displayData(); A.isAdult();}