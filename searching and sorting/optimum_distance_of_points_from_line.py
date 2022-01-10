# Python 3

import math


class OptimumDistance:
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Line:
        def __init__(self, m, n, c):
            self.m = m
            self.n = n
            self.c = c

    def dist(self, point, x, y):
        return math.sqrt(((x - point.x) ** 2) + ((y - point.y) ** 2))

    def compute(self, points, line, x):
        total_distance = 0
        # calculate value of y of point with value x on line using line equation ax + by + c = 0
        y = -1 * (line.m*x + line.c) / line.n
        # calculate distance from every point in points array
        for point in points:
            total_distance += self.dist(point, x, y)
        return total_distance

    def find_dist(self, points, line):
        low = -1e6
        high = 1e6
        accuracy = 1e-06

        # For mid1 and mid2 we are calculating x values
        while high - low > accuracy:
            offset = (high - low) / 3
            mid1 = low + offset
            mid2 = high - offset

            # compute method calculates total distance from every point from line and mid_point
            dist_from_mid1 = self.compute(points, line, mid1)
            dist_from_mid2 = self.compute(points, line, mid2)

            # shortening search area based on total distance from mid1 and mid2
            if dist_from_mid1 < dist_from_mid2:
                high = mid2
            else:
                low = mid1

        return self.compute(points, line, (low + high) / 2)

    def calculate_optimum_distance(self, p, l):
        # Initialize points with Point class and line with Line class
        points = []
        for i in p:
            point_obj = self.Point(i[0], i[1])
            points.append(point_obj)
        line = self.Line(l[0], l[1], l[2])

        # calling find_dist method to calculate minimum distance
        return '{:.4f}'.format(self.find_dist(points, line))


def main():
    # Initialize object for optimum distance
    obj = OptimumDistance()
    n = int(input())
    points = []
    for i in range(n):
        x, y = list(map(int, input().split()))
        points.append([x,y])
    line = list(map(int, input().split()))
    # method calculate_optimum_distance of class OptimumDistance calculates minimum distance
    print(obj.calculate_optimum_distance(points, line))


if __name__ == '__main__':
    main()