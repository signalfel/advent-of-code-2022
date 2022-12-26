def add(tuple1: tuple, tuple2: tuple):
    return tuple(map(lambda x, y: x + y, tuple1, tuple2))

def get_grid_neighbours(point: tuple, n_neighbours: int, as_dict: bool = False):
    """
    Return the neighbours of a point on the 2D grid.

    Parameters
    ----------
    n_neigbours : int, 4 or 8
        the number of neighbors to return on the grid.
        4 gives n, s, e, and w neighbours, and 8 includes the diagonals 
    as_dict : bool , default: False
        if True, returns a dict with keys: n, s, w, ... the neighbours as values.

    Returns
    -------
    grid_neighbours

    """
    # n = (0, -1)
    # s = (0, 1)
    # w = (-1, 0)
    # e = (1, 0)
    n = (-1,  0)
    s = (1, 0)
    w = (0, -1)
    e = (0, 1)

    neighbours = dict()
    neighbours['n'] = add(point, n)
    neighbours['s'] = add(point, s)
    neighbours['w'] = add(point, w)
    neighbours['e'] = add(point, e)
    
    if n_neighbours == 8:
        neighbours['nw'] = add(point, add(n, w))
        neighbours['sw'] = add(point, add(s, w))
        neighbours['ne'] = add(point, add(n, e))
        neighbours['se'] = add(point, add(s, e))
        
    return neighbours if as_dict else list(neighbours.values())