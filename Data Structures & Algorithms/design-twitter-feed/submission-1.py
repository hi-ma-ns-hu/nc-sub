class Twitter:

    def __init__(self):
        self.time = 0 # time of posting tweet
        self.follows = defaultdict(set) # {followerId, set of followeeIds}
        self.tweets = defaultdict(list) # {userId: list([time, tweetId])}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = list(), list()
        self.follows[userId].add(userId)
        for followeeId in self.follows[userId]:
            if not self.tweets[followeeId]: continue
            index = len(self.tweets[followeeId])-1
            time, tweetId = self.tweets[followeeId][index]
            heap.append([-time, tweetId, followeeId, index-1])
        heapq.heapify(heap)
        while heap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap, [-time, tweetId, followeeId, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]: self.follows[followerId].remove(followeeId)