#include <iostream>
using namespace std;

class Copyable {
public:
    Copyable(){cout << "Born" << endl; }
    Copyable(const Copyable &o) {
        cout << "Copied" << endl;
    }
    ~Copyable(){cout << "Die." << endl; }
};
Copyable ReturnRvalue() {
    return Copyable();
}
void AcceptVal(Copyable a) {

}
void AcceptRef(const Copyable& a) {
}


class A {

private:
    A(){};
    ~A(){};
    static A *instance;

public:
    static A *Get_instance(){
        if(instance == nullptr){
            instance = new A();
        }
        return instance;
    };
};

A* A::instance = nullptr;

int main() {
    cout << "pass by value: " << endl;
    AcceptVal(ReturnRvalue()); 
    cout << "pass by reference: " << endl;
    AcceptRef(ReturnRvalue()); 

    A* a = A::Get_instance();
}


// pass by value:
// Born
// Copied
// Die.
// Copied
// Die.
// Die.
// pass by reference:
// Born
// Copied
// Die.
// Die.