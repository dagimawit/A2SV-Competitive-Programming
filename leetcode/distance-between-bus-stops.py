class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        n = len(distance)
        total_distance = sum(distance)
        clockwise_distance = sum(distance[min(start, destination):max(start, destination)])
        counterclockwise_distance = total_distance - clockwise_distance

        return min(clockwise_distance, counterclockwise_distance)