class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n_customers = len(customers)
        wait_time = 0
        current_time = 0

        for customer in customers:
            arrival, time = customer
            start = max(current_time, arrival)
            current_time = start + time
            wait_time += current_time - arrival
        
        return wait_time / n_customers
