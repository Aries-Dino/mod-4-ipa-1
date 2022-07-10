'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if social_graph[from_member]["following"].count(to_member) > 0 and social_graph[to_member]["following"].count(from_member) > 0:
        x = str("friends")
    elif social_graph[from_member]["following"].count(to_member) > 0:
        x = str("follower")
    elif social_graph[to_member]["following"].count(from_member) > 0:
        x = str("followed by")
    else:
        x = str("no relationship")
    
    return x


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    horizontal = []
    for i in range(len(board)):
        x_hor = all(v == board[i][0] for v in board[i])
        horizontal.append(x_hor)
    
    vertical = []
    for y in range(len(board)):
        x_vert = [i for i in zip(*board)][y].count([i for i in zip(*board)][y][0]) == len([i for i in zip(*board)][y])
        vertical.append(x_vert)

    if horizontal.count(True) > 0:
        winner = board[horizontal.index(True)][0]
    elif vertical.count(True) > 0:
        winner = board[0][vertical.index(True)]
    elif [board[i][i] for i in range(len(board))].count([board[i][i] for i in range(len(board))][0]) == len([board[i][i] for i in range(len(board))]):
        winner = [board[i][i] for i in range(len(board))][0]
    elif [board[len(board)-1-i][i] for i in range(len(board))].count([board[len(board)-1-i][i] for i in range(len(board))][0]) == len([board[len(board)-1-i][i] for i in range(len(board))]):
        winner = [board[len(board)-1-i][i] for i in range(len(board))][0]
    else:
        winner = "NO WINNER"
    
    return winner

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    stop1 = []
    for i in range(len(list(route_map.keys()))):
        x = list(route_map.keys())[i][0]
        stop1.append(x)

    y = []
    z = stop1.index(first_stop)
    travel = list(route_map.keys())[z][1]

    while list(route_map.keys())[z][1] != second_stop:
        if z < len(route_map)-1:
            z = z+1
        else:
            z = z-(len(route_map)-1)
        travel = travel + "," + list(route_map.keys())[z][1]


    y.append(travel)

    stop2 = y

    stop2list = stop2[0].split(",")

    b = []
    for v in range(len(stop2list)):
        a = 0          
        while list(route_map.keys())[a][1] != stop2list[v]:
            a = a + 1
        c = list(route_map.keys())[a]
        b.append(c)

    final = []
    for i in range(len(b)):
        last = route_map[b[i]]["travel_time_mins"]
        final.append(last)

    final
    final_2 = sum(final)

    return final_2