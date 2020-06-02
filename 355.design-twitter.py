#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#


# @lc code=start
import heapq
from collections import deque


class Tweet:
    def __init__(self, id, timestamp) -> None:
        self.id = id
        self.timestamp = timestamp
        self.next = None

    def __lt__(self, other):
        return self.timestamp > other.timestamp


class User:
    def __init__(self, userId) -> None:
        self.id = userId
        # head of a linked list of tweets
        self.head = None
        self.followed = set()
        self.follow(userId)

    def follow(self, userId):
        if userId not in self.followed:
            self.followed.add(userId)

    def unfollow(self, userId):
        if userId != self.id and userId in self.followed:
            self.followed.remove(userId)

    def post(self, tweetId, timestamp):
        tweet = Tweet(tweetId, timestamp)
        tweet.next = self.head
        self.head = tweet


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = 0
        self.users = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.users:
            self.users[userId] = User(userId)
        user = self.users.get(userId)
        user.post(tweetId, self.timestamp)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        res = []
        if userId not in self.users:
            return res

        pq = []
        for _id in self.users[userId].followed:
            user = self.users[_id]
            if user.head:
                heapq.heappush(pq, user.head)

        while pq:
            if len(res) >= 10:
                break
            latest = heapq.heappop(pq)
            res.append(latest.id)

            if latest.next:
                heapq.heappush(pq, latest.next)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        for _id in [followeeId, followerId]:
            if _id not in self.users:
                self.users[_id] = User(_id)
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.users:
            self.users[followerId].unfollow(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
