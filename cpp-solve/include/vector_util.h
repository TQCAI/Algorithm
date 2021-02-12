//
// Created by tqc on 2021/2/10.
//
#include "bits/stdc++.h"

#ifndef PRO01_VECTOR_UTIL_H
#define PRO01_VECTOR_UTIL_H

#endif //PRO01_VECTOR_UTIL_H

using namespace std;

string vector2str(vector<int> v) {
    string ans = "[";
    for (int i = 0; i < v.size(); ++i) {
        char chr[100];
        sprintf(chr, "%d", v[i]);
        ans += string(chr);
        if (i != v.size() - 1)
            ans += " , ";
    }
    ans += "]";
    return ans;
}

string vector2str(vector<char> v) {
    string ans = "[";
    for (int i = 0; i < v.size(); ++i) {
        char chr[100];
        sprintf(chr, "%c", v[i]);
        ans += string(chr);
        if (i != v.size() - 1)
            ans += " , ";
    }
    ans += "]";
    return ans;
}
