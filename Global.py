import numpy as np

def get_average_points(points=[], delta=1):
    # calculate the average point within delta distance of each point
    avg_points = []
    for point in points:
        # get all points within delta distance of current point
        dist = np.linalg.norm(points - point, axis=1)
        nearby_points = points[dist <= delta]
        
        # calculate the average point of nearby points
        if len(nearby_points) > 0:
            avg_point = np.mean(nearby_points, axis=0)
            avg_points.append(avg_point)
        
    return avg_points