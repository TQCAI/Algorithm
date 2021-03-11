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

string matrix2str(vector<vector<int>> v) {
    string final;
    for (int i = 0; i < v.size(); ++i) {
        for (int j = 0; j < v[i].size(); ++j) {
            string ans = "[";
            char chr[100];
            sprintf(chr, "%d", v[i][j]);
            ans += string(chr);
            if (i != v.size() - 1)
                ans += " , ";
            ans += "]";
            final += ans;
        }
    }
    return final;
}

string two_d_arr_to_str(int v[1005][1005], int n, int m) {
    string final;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            string ans = "[";
            char chr[100];
            sprintf(chr, "%d", v[i][j]);
            ans += string(chr);
            if (j != m - 1)
                ans += " , ";
            ans += "]";
            final += ans+"\n";
        }
    }
    return final;
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
