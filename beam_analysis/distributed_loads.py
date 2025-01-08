def convert_distributed_loads(distributed_loads):
    """Convert distributed loads into equivalent point loads."""
    equivalent_loads = []
    equivalent_positions = []

    for load_data in distributed_loads:
        if len(load_data) == 7:
            w, w2, start, end, dist_type, orientation, direction = load_data
        elif len(load_data) == 6:
            w, start, end, dist_type, orientation, direction = load_data
            w2 = w
        elif len(load_data) == 5:
            w, start, end, dist_type, direction = load_data
            w2 = w
            orientation = None

        sign = 1 if direction == 'up' else -1

        if dist_type == 'rectangular':
            F_eq = sign * w * (end - start)
            x_eq = (start + end) / 2
        elif dist_type == 'triangular':
            if orientation == 'start':
                F_eq = sign * 0.5 * w * (end - start)
                x_eq = start + (1 / 3) * (end - start)
            elif orientation == 'end':
                F_eq = sign * 0.5 * w * (end - start)
                x_eq = start + (2 / 3) * (end - start)
        elif dist_type == 'trapezoidal':
            F_eq = ((w + w2) / 2) * (end - start) * sign
            x_eq = start + ((w + 2 * w2) / (3 * (w + w2))) * (end - start)
        else:
            raise ValueError("Invalid distributed load type")

        equivalent_loads.append(F_eq)
        equivalent_positions.append(x_eq)

    return equivalent_loads, equivalent_positions
