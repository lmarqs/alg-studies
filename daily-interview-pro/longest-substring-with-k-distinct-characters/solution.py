def longest_substring_with_k_distinct_characters(s, k):
    visited = {}
    ans = 0
    tail = head = 0
    while head < len(s):
        visited[s[head]] = head

        if len(visited) > k:
            tmp = visited[s[tail]] + 1
            del visited[s[tail]]
            tail = tmp

        ans = max(head - tail + 1, ans)
        head += 1

    return ans
