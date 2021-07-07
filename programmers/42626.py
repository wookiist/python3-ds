# 42626 더 맵게
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        # 가장 작은 요리
        C1 = heapq.heappop(scoville)
        # 두 번째로 작은 요리
        C2 = heapq.heappop(scoville)
        # 조리법대로 섞고
        New_C = C1 + (C2*2)
        answer += 1
        # 리스트에 삽입
        heapq.heappush(scoville, New_C)

        if scoville[0] >= K:
            # 가장 낮은 음식이 K 이상이 됐으니 종료
            break

    if scoville[0] >= K:
        return answer
    else:
        return -1