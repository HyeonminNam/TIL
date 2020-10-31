def solution(clothes):
    # 부위별 옷 개수 딕셔너리, 해당 부위 안 입을 경우 포함하기 위해서 초깃값 1
    closet = {y:1 for _, y in clothes}
    for x, y in clothes:
        closet[y] += 1
    # 모든 경우의 수 곱 - 1(모두 안 입는 경우 제외)
    return eval('*'.join(map(str, closet.values())))-1

if __name__ == "__main__":
    clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
    print(solution(clothes))