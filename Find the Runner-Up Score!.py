if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # Remove duplicates by converting the list to a set and back to a list
    unique_scores = list(set(arr))
    
    # Sort the list of unique scores in descending order
    sorted_scores = sorted(unique_scores, reverse=True)
    
    # The runner-up score is the second element in the sorted list
    runner_up_score = sorted_scores[1]
    
    # Print the runner-up score
    print(runner_up_score)
