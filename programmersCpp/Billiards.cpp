// 당구대의 가로 길이 m, 세로 길이 n과 머쓱이가 쳐야 하는 공이 놓인 위치 좌표를 나타내는
// 두 정수 startX, startY, 그리고 매 회마다 목표로 해야하는 공들의 위치 좌표를 나타내는 
// 정수 쌍들이 들어있는 2차원 정수배열 balls가 주어집니다. "원쿠션" 연습을 위해 머쓱이가 
// 공을 적어도 벽에 한 번은 맞춘 후 목표 공에 맞힌다고 할 때, 각 회마다 머쓱이가 친 공이 
// 굴러간 거리의 최솟값의 제곱을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

// 단, 머쓱이가 친 공이 벽에 부딪힐 때 진행 방향은 항상 입사각과 반사각이 동일하며, 
// 만약 꼭짓점에 부딪힐 경우 진입 방향의 반대방향으로 공이 진행됩니다. 
// 공의 크기는 무시하며, 두 공의 좌표가 정확히 일치하는 경우에만 두 공이 서로 맞았다고 판단합니다. 
// 공이 목표 공에 맞기 전에 멈추는 경우는 없으며, 목표 공에 맞으면 바로 멈춘다고 가정합니다.

// 제한사항
// 3 ≤ m, n ≤ 1,000
// 0 < startX < m
// 0 < startY < n
// 2 ≤ balls의 길이 ≤ 1,000
// balls의 원소는 [a, b] 형태입니다.
// a, b는 머쓱이가 맞춰야 할 공이 놓인 좌표를 의미합니다.
// 0 < a < m, 0 < b < n
// (a, b) = ( startX, startY )인 입력은 들어오지 않습니다.
// 입출력 예
// m	n	startX	startY	balls	                    result
// 10	10	3	    7	    [[7, 7], [2, 7], [7, 3]]	[52, 37, 116]

#include <string>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

vector<int> solution(int m, int n, int startX, int startY, vector<vector<int>> balls) {
    vector<int> answer;
    vector<pair<int, int>> startB;
    startB.push_back(make_pair(-startX, startY));
    startB.push_back(make_pair(startX, 2*n - startY));
    startB.push_back(make_pair(startX, -startY));
    startB.push_back(make_pair(2*m - startX, startY));
    
    for (int i = 0; i < balls.size() ; i++){
        int min = 987654321;
        for (int j = 0; j <startB.size(); j++){
            if (startY == balls[i][1] && j == 0 && startX > balls[i][0])
                continue;
            else if (startX == balls[i][0] && j == 1 && startY < balls[i][1])
                continue;
            else if (startX == balls[i][0] && j == 2 && startY > balls[i][1])
                continue;
            else if (startY == balls[i][1] && j == 3 && startX < balls[i][0])
                continue;
            else {
                int temp = pow(balls[i][0] - startB[j].first, 2) + pow(balls[i][1] - startB[j].second, 2);
                if (temp <= min)
                    min = temp;
            }
        }
        answer.push_back(min);
    }
    return answer;
}