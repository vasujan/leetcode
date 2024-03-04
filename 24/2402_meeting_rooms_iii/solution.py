import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [None] * n
        room_counter = [0] * n
        current_time = -1
        delayed_meetings = []

        meetings.sort(key=lambda x: x[0], reverse=True)

        while meetings:
            current_time += 1

            if meetings[-1] == current_time:
                current_meeting = meetings.pop()
            else:
                continue
            
            