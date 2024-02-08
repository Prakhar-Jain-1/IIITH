import math

def is_point_inside_circle(point, circle_center, circle_radius):
    x, y = point
    center_x, center_y = circle_center
    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
    return distance < circle_radius


def is_position_open(position, place, ind):

    if ind == -1:
        for i in place.emptyPos:
            if is_point_inside_circle(position,place.star_points[i], 40):
                return i,None
        # return -1,None

    if ind % 2 == 0:
        neighbors = [ind + 1, ind - 1]
    else:
        neighbors = [ind + 1, ind - 1, ind + 2, ind - 2]

    if place.current_player == "Vulture":
        killPlace = [(ind + 3)%10, (ind -3)%10]
        # print(killPlace)
        # print(place.emptyPos)
        l = (ind + 1)%2
        if killPlace[0] in place.emptyPos and (killPlace[0] - 1 - l)%10 not in place.emptyPos and is_point_inside_circle(position,place.star_points[killPlace[0]], 40):
            place.emptyPos.append((killPlace[0] - 1 - l)%10)
            for crow in place.crows:
                if crow.ind == (killPlace[0] - 1- l)%10: 
                    place.crows.remove(crow)
                    place.killCount+=1
            return killPlace[0],None
        if killPlace[1] in place.emptyPos and (killPlace[1] + 1 + l)%10 not in place.emptyPos and is_point_inside_circle(position,place.star_points[killPlace[1]], 40):
            place.emptyPos.append((killPlace[1] + 1 + l)%10)
            for crow in place.crows:
                if crow.ind == (killPlace[1] + 1 + l)%10: 
                    # crow.ind = -2
                    place.crows.remove(crow)
                    # crow.x,crow.y = 0, 0
                    place.killCount+=1
            return killPlace[1],None
            

    for neighbor in neighbors:
        if neighbor%10 in place.emptyPos and is_point_inside_circle(position,place.star_points[neighbor%10], 40):
            # place.emptyPos.append[ind]
            return neighbor%10,None
        # for 
        for crow in place.crows:
            if is_point_inside_circle(position,(crow.x,crow.y), 40):
                return -1, (crow if place.current_player == 'Crow' else place.vulture)


        continue


    return -1,None

