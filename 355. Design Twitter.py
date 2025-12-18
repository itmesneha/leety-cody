import heapq as h
class Twitter:
    '''
    min heap only put [-10:] tweets of each user as time is increasing and u are just
    appending to a list
    '''

    def __init__(self):
        self.follows = defaultdict(set) # user : follows who all including themself
        self.tweets = defaultdict(list) # user : time, tweetid
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.follows[userId].add(userId)
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        for follower in self.follows[userId]:
            for time, tweetid in self.tweets[follower][-10:]:
                h.heappush(minheap, [time, tweetid])
                if len(minheap) > 10:
                    h.heappop(minheap)
        
        res = []
        while minheap and len(res) < 10:
            res.append(h.heappop(minheap)[1])

        return res[::-1]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.follows[followerId].remove(followeeId)
        except:
            return None
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
