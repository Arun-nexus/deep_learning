#include <iostream>
using namespace std;

class student
{
    public:
    string name;
    int roll;

    student (int roll,string name){
        this->name=name;
       this-> roll=roll;


    }
    student (){
        name="";
        roll=0;
        
    }

void getinfo(){
    cout<<"name and roll no";
    cin>> name>>roll;

cout <<name<<roll;

}
};




int main(){
    student s1;
    s1.getinfo();
    
}