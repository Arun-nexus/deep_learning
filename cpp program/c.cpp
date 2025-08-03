#include <iostream>
using namespace std;

class student{

    public:
    int c;
student (){
    cout<<"hi i am a constructor";

}

    void display(){
        cout << "the value of c"<< endl;
        cin>> c;
        cout<<c;

    }
};
int main(){
    student s1;
    s1.display();
    
}

