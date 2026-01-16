class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # For every OFFLINE event add ONLINE event to avoid tracking time
        for event, timestamp, message in events:
            if event == "OFFLINE":
                events.append(["ONLINE", str(int(timestamp) + 60), message])

        # Sort first by event in order ONLINE, OFFLINE, MESSAGE
        # The sort by timestamp that will keep the order by event for equal timestamps
        events.sort(key=lambda x: x[0], reverse=True)
        events.sort(key=lambda x: int(x[1]))

        # Set of online users
        online = set(range(numberOfUsers))

        # Separate variable to keep track of ALL mentions to increment 
        # it just once at the end instead of incrementing by 1 every step
        all_mentioned = 0

        result = [0] * numberOfUsers
        for event, timestamp, message in events:
            match event:
                case "MESSAGE":
                    # Count everyone
                    if message == "ALL":
                        all_mentioned += 1

                    # Add only online users
                    elif message == "HERE":
                        for i in online:
                            result[i] += 1

                    # Add directly mentioned users
                    else:
                        for idstr in message.split():
                            result[int(idstr[2:])] += 1

                # Process online/offline users
                case "OFFLINE":
                    online.remove(int(message))
                case "ONLINE":
                    online.add(int(message))

        for i in range(numberOfUsers):
            result[i] += all_mentioned

        return result