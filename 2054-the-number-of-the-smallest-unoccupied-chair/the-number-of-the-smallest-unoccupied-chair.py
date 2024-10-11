class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        n = len(times)
        # Sort the times array based on arrival times and keep track of the original indices
        events = sorted([(times[i][0], times[i][1], i) for i in range(n)], key=lambda x: x[0])

        # List to track chair assignments
        chairs = [-1] * n
        free_chairs = list(range(n))  # Smallest unoccupied chairs, initially all chairs are available
        occupied = []

        for arrival, leaving, friend in events:
            # Free up chairs for people who have already left
            while occupied and occupied[0][0] <= arrival:
                chair_to_free = occupied.pop(0)[1]
                free_chairs.append(chair_to_free)
                free_chairs.sort()  # Sort to always get the smallest available chair

            # Assign the smallest available chair to the current friend
            assigned_chair = free_chairs.pop(0)
            chairs[friend] = assigned_chair

            # If this is the target friend, return the assigned chair
            if friend == targetFriend:
                return assigned_chair

            # Add the current friend's chair to the list of occupied chairs
            occupied.append((leaving, assigned_chair))
            occupied.sort()  # Sort based on leaving time to free chairs in order
