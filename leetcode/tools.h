#include<vector>
#include<iostream>
#include<ostream>
template <typename T>
void array2vector(int *arr, std::vector<T> &v, int length) {
    for (int i=0; i<length; ++i)
        v.push_back(arr[i]);
}

template <typename T>
void print_vector(const std::vector<T> &v) {
    std::cout << "[";
    for (int i=0; i<v.size(); ++i)
        std::cout << v[i] << ", ";
    std::cout << "]" << std::endl;
}

template <typename T>
std::ostream &operator<<(std::ostream &out, std::vector<T> vec) {
    out << "[";
    for (int i=0; i<vec.size(); ++i) {
        out << vec[i];
        if(i< vec.size()-1)
            out << ", ";
    }

    out << "]" << std::endl;
    return out;
}

