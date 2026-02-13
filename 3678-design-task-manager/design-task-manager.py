import bisect

class TaskManager:
    def __init__(self, tasks):
        self.mp = {}  # taskId -> (userId, priority)
        self.st = []  # sorted list of (priority, taskId)

        for userId, taskId, priority in tasks:
            self.mp[taskId] = (userId, priority)
            bisect.insort(self.st, (priority, taskId))

    def add(self, userId, taskId, priority):
        self.mp[taskId] = (userId, priority)
        bisect.insort(self.st, (priority, taskId))

    def edit(self, taskId, newPriority):
        userId, oldPriority = self.mp[taskId]
        idx = bisect.bisect_left(self.st, (oldPriority, taskId))
        self.st.pop(idx)
        self.mp[taskId] = (userId, newPriority)
        bisect.insort(self.st, (newPriority, taskId))

    def rmv(self, taskId):
        userId, priority = self.mp[taskId]
        idx = bisect.bisect_left(self.st, (priority, taskId))
        self.st.pop(idx)
        del self.mp[taskId]

    def execTop(self):
        if not self.mp:
            return -1
        priority, taskId = self.st.pop()  # highest priority
        userId, _ = self.mp[taskId]
        del self.mp[taskId]
        return userId