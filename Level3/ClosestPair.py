import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def closest_pair_brute_force(points):
    min_distance = float('inf')
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    
    return closest_pair

points = [(2, 3), (12, 30), (40, 50), (5, 21), (12, 10), (3, 20)]
closest_pair = closest_pair_brute_force(points)
print("Closest pair:", closest_pair)
