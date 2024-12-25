#include <iostream>
#include <vector>
using namespace std;

int solve(int n, vector<int>& a) {
    // Case 1: Check if array is already all zeros
    bool all_zeros = true;
    for (int i = 0; i < n; i++) {
        if (a[i] != 0) {
            all_zeros = false;
            break;
        }
    }
    if (all_zeros) return 0;
    
    // Case 2: Check if we can solve in one operation
    if (n == 1) return (a[0] == 0 ? 0 : 1);
    
    // If first element is 0 and array has only one non-zero element after it
    // OR if last element is 0 and array has only one non-zero element before it
    if (a[0] == 0) {
        bool single_non_zero = true;
        for (int i = 2; i < n; i++) {
            if (a[i] != 0) {
                single_non_zero = false;
                break;
            }
        }
        if (single_non_zero && a[1] != 0) return 1;
    }
    if (a[n-1] == 0) {
        bool single_non_zero = true;
        for (int i = 0; i < n-2; i++) {
            if (a[i] != 0) {
                single_non_zero = false;
                break;
            }
        }
        if (single_non_zero && a[n-2] != 0) return 1;
    }
    
    // Case 3: If array starts or ends with non-zeros and no zeros in between them
    int first_zero = -1;
    for (int i = 0; i < n; i++) {
        if (a[i] == 0) {
            first_zero = i;
            break;
        }
    }
    
    if (first_zero == -1) return 1; // No zeros in array
    
    // Otherwise, we need 2 operations
    return 2;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        cout << solve(n, a) << '\n';
    }
    
    return 0;
}