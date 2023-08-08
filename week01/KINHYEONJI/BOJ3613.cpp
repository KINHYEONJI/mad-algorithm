#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string str;
    cin >> str;
    int index = str.find('_');
    vector<char> replace_str;
    int javaFlag = 0;
    int cppFlag = 0;
    for (int i = 0; i < str.size(); i++) {
        if (str[i] >= 'A' && str[i] <= 'Z') {
            if (i == 0) {
                cout << "Error!";
                return 0;
            }
            javaFlag = 1;
            replace_str.push_back('_');
            replace_str.push_back(str[i] - 'A' + 'a');
        } else if (str[i] == '_') {
            if (i == str.size() - 1 || i == 0 || str[i + 1] == '_' || (str[i + 1] >= 'A' && str[i + 1] <= 'Z')) {
                cout << "Error!";
                return 0;
            }
            cppFlag = 1;
            replace_str.push_back(str[i + 1] - 'a' + 'A');
            i++;
        } else {
            replace_str.push_back(str[i]);
        }
    }
    if (javaFlag + cppFlag == 2) cout << "Error!";
    else for (char ch: replace_str) cout << ch;
    return 0;



    //    if (index == string::npos) {
//        for (int i = 0; i < str.size(); i++) {
//            if (str[i] >= 'A' && str[i] <= 'Z'){
//                replace_str.push_back('_');
//                replace_str.push_back(str[i]-'A' +'a');
//            }
//            else{
//                replace_str.push_back(str[i]);
//            }
//        }
//        for(char ch : replace_str) cout<<ch;
//        return 0;
//    }
//    while (index != string::npos) {
//        str.replace(index, 2, 1, str[index + 1] - 'a' + 'A');
//        str.erase(index, 1);
//        index = str.find('_');
//    }
//    cout<<str;
    return 0;
}