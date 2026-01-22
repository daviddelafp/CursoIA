from collections import deque

def camino_con_deque(grid, start, goal):
    """
    grid: matriz 0=libre, 1=bloqueado
    start, goal: (fila, col)
    Devuelve:
      - lista de coordenadas del camino (incluye inicio y meta)
      - string de movimientos (por ejemplo: "RRDDLU")
    Si no hay camino -> (None, None)
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    sr, sc = start
    gr, gc = goal

    # Validaciones básicas
    if rows == 0 or cols == 0:
        return None, None
    if sr < 0 or sr >= rows or sc < 0 or sc >= cols:
        return None, None
    if gr < 0 or gr >= rows or gc < 0 or gc >= cols:
        return None, None
    if grid[sr][sc] == 1 or grid[gr][gc] == 1:
        return None, None

    # visited y parent (TODO son listas)
    visited = [[0] * cols for _ in range(rows)]
    parent_r = [[-1] * cols for _ in range(rows)]
    parent_c = [[-1] * cols for _ in range(rows)]
    parent_mv = [[""] * cols for _ in range(rows)]

    # Cola deque
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 1

    # Movimientos: (letra, dr, dc)
    moves = [("U", -1, 0), ("D", 1, 0), ("L", 0, -1), ("R", 0, 1)]

    # Bucle de búsqueda (con deque)
    while q:
        r, c = q.popleft()

        if r == gr and c == gc:
            # Reconstruir camino
            coords = []
            movs = []
            cr, cc = gr, gc

            while not (cr == sr and cc == sc):
                coords.append((cr, cc))
                movs.append(parent_mv[cr][cc])
                pr = parent_r[cr][cc]
                pc = parent_c[cr][cc]
                cr, cc = pr, pc

            coords.append((sr, sc))
            coords.reverse()
            movs.reverse()
            return coords, "".join(movs)

        for mv, dr, dc in moves:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if visited[nr][nc] == 0 and grid[nr][nc] == 0:
                    visited[nr][nc] = 1
                    parent_r[nr][nc] = r
                    parent_c[nr][nc] = c
                    parent_mv[nr][nc] = mv
                    q.append((nr, nc))

    return None, None


# Demo rápido
if __name__ == "__main__":
    grid = [
        [0,0,0,0,0],
        [1,1,1,0,0],
        [0,0,0,0,1],
        [0,1,0,0,0],
        [0,0,0,1,0],
    ]
    start = (0, 0)
    goal  = (4, 4)

    coords, movs = camino_con_deque(grid, start, goal)
    if coords is None:
        print("No existe camino 😭")
    else:
        print("Camino:", coords)
        print("Movimientos:", movs)