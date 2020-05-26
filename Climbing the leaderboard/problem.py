import os


def climbingLeaderboard(scores, user_scores):
    user_ranks = []
    unique_scores = list(dict.fromkeys(scores))
    unique_scores.sort(reverse=True)

    for user_score in user_scores:
        num_scores = len(unique_scores)
        last = num_scores - 1
        first = 0
        middle = 0
        found = False
        while first <= last < num_scores and not found:
            middle = (first + last) // 2
            if unique_scores[middle] == user_score:
                found = True
                user_ranks.append(middle + 1)
            else:
                if unique_scores[middle] > user_score:
                    first = middle + 1
                else:
                    last = middle - 1

        if not found:
            if first > last:
                user_ranks.append(first + 1)
            elif last <= 0:
                user_ranks.append(1)
            else:
                user_ranks.append(middle + 1)

    return user_ranks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr = open('output.txt', 'w')
    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
