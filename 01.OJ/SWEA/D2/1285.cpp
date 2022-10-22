// 아름이의 돌 던지기
#include <iostream> 
using namespace std;
int main() {
    int T, x;
    cin >> T;

    int N, n, distance, min_distance, min_count;
    for (x=1; x<=T; x++) {
        cin >> N;
        min_distance = 100001;
        for (n=0;n<N;n++){
            cin >> distance;
            distance = abs(distance);
            if( distance < min_distance){
                min_distance = distance;
                min_count = 1;
                continue;
            }
            if (distance == min_distance) {
                min_count++;
            }
        }
        cout << "#" << x << " " << min_distance << " " << min_count << endl;
    }
}