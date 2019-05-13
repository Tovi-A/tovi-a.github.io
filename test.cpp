#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

class base{
public:
    base() = default;
    base(int nn) : num(nn) { }
    base(int nn1, int nn2) : num(nn1), num1(nn2) { }
    static int sta;
protected:
    int num;
    int num1;
};

int base::sta = 999;//类的静态成员必须在外面初始化

class derive : public base{
public:
    derive() = default;
    derive(int nn) {
        num = nn;
    }
    derive(int nn1, int nn2) : base(nn1, nn2) { }       //派生类构造函数

    void assign_num(derive &obj, int nn) const {
        obj.num = nn;
    }
    
    void print_num() const {
        cout << num << endl;
        sta = 9999;
    }
};

int main() {
    derive D(99);
    base B;
    D.print_num();
    D.assign_num(D, 123);
    D.print_num();
    cout << D.sta<< endl;
    
    //cout << B.num << endl;//这样是不能的
    //D.num = 9;
    //cout << D.num << endl;//这样是不能的
    return 0;
}



class Quote {
public:
    Quote() = default;
    Quote(const std:: string &book, double sales_price):
                bookNo(book), price(sales_price) { }
    std::string isbn() const { return bookNo; }
    virtual double net_price(std::size_t n) const 
            { return n * price; }
    virtual ~Quote() = default;
private:
    std::string bookNo;
protected:
    double price = 0.0;
};

class Bulk_quote : public Quote {
public:
    Bulk_quote() = default;
    Bulk_quote(const std::string&, double, std::size_t, double);
    double net_price(std::size_t)   const override;
private:
    std::size_t min_qty = 0;
    double discount = 0.0;
};