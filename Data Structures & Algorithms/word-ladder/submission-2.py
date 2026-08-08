class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList: return 0

    adj_list = defaultdict(list)
    visited = set([beginWord])
    queue = deque([beginWord])
    res = 1
    
    wordList.append(beginWord)
    for word in wordList:
      for j in range(len(word)):
        pattern = word[:j]+'*'+word[j+1:]
        adj_list[pattern].append(word)

    while queue:
      for _ in range(len(queue)):
        word = queue.popleft()
        # if word is equal to endWord just return it, you've found it
        if word == endWord: return res
        # now create pattern from the word to traverse other items in adj_list
        for j in range(len(word)):
          pattern = word[:j]+'*'+word[j+1:]
          for k in adj_list[pattern]:
            if k not in visited:
              visited.add(k)
              queue.append(k)
      res += 1

    # no valid path found
    return 0