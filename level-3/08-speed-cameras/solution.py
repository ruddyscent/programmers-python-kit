def solution(routes):
    def exit_point(route):
        return route[1]

    cameras = 0
    camera_position = None
    for start, end in sorted(routes, key=exit_point):
        if camera_position is None or start > camera_position:
            cameras += 1
            camera_position = end
    return cameras
