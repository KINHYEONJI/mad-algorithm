#include <iostream>
#include <vector>
#include <map>
#include <string>

#define INF 0x3f3f3f

using namespace std;

int main() {
    int n, r;
    cin >> n >> r;
    map<string, int> city_m;
    for (int i = 0; i < n; i++) {
        string city;
        cin >> city;
        city_m[city] = i;
    }
    int m;
    cin >> m;
    vector<int> visit_city_i(m);
    for (int i = 0; i < m; i++) {
        string city;
        cin >> city;
        visit_city_i[i] = city_m[city];
    }
    int k;
    cin >> k;
    vector<vector<double>> use_n(n + 2, vector<double>(n + 2, INF));
    vector<vector<double>> not_use_n(n + 2, vector<double>(n + 2, INF));
    while (k--) {
        string ticket, s, e;
        double p;
        cin >> ticket >> s >> e >> p;
        int s_i, e_i;
        s_i = city_m[s];
        e_i = city_m[e];
        if (ticket == "Mugunghwa" || ticket == "ITX-Saemaeul" || ticket == "ITX-Cheongchun") {
            use_n[s_i][e_i] = 0;
            not_use_n[s_i][e_i] = min(not_use_n[s_i][e_i], p);
            use_n[e_i][s_i] = 0;
            not_use_n[e_i][s_i] = min(not_use_n[e_i][s_i], p);
        } else if (ticket == "S-Train" || ticket == "V-Train") {
            use_n[s_i][e_i] = min(use_n[s_i][e_i], p / 2);
            not_use_n[s_i][e_i] = min(not_use_n[s_i][e_i], p);
            use_n[e_i][s_i] = min(use_n[e_i][s_i], p / 2);
            not_use_n[e_i][s_i] = min(not_use_n[e_i][s_i], p);
        } else {
            use_n[s_i][e_i] = min(use_n[s_i][e_i], p);
            not_use_n[s_i][e_i] = min(not_use_n[s_i][e_i], p);
            use_n[e_i][s_i] = min(use_n[e_i][s_i], p);
            not_use_n[e_i][s_i] = min(not_use_n[e_i][s_i], p);
        }
    }
    for (int l = 0; l < n; l++) {
        for (int i = 0; i < n; i++) {
            if (i == l) continue;
            for (int j = 0; j < n; j++) {
                if (l == j || i == j) continue;
                if (use_n[i][j] > use_n[i][l] + use_n[l][j]) {
                    use_n[i][j] = use_n[i][l] + use_n[l][j];
                }
                if (not_use_n[i][j] > not_use_n[i][l] + not_use_n[l][j]) {
                    not_use_n[i][j] = not_use_n[i][l] + not_use_n[l][j];
                }
            }
        }
    }

    double use_t_p = 0;
    double not_use_t_p = 0;
    for (int i = 0; i < m - 1; i++) {
        use_t_p += use_n[visit_city_i[i]][visit_city_i[i + 1]];
        not_use_t_p += not_use_n[visit_city_i[i]][visit_city_i[i + 1]];
    }
    if (not_use_t_p <= use_t_p + r) cout << "No";
    else cout << "Yes";
}