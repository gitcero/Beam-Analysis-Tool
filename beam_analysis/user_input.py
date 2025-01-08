def get_user_input():
    """Collects all user input for the beam problem."""
    beam_length = float(input("Enter the length of the beam (m): "))
    supports = []
    print("Support options:\n1 - Two supports\n2 - One simple support\n3 - One fixed support")
    choice = int(input("Enter your choice (1/2/3): "))

    # Supports
    if choice == 1:
        supports.append(("simple", float(input("Enter the position of the first support (m): "))))
        supports.append(("simple", float(input("Enter the position of the second support (m): "))))
    elif choice == 2 or choice == 3:
        supports.append(("fixed" if choice == 3 else "simple", float(input("Enter the position of the support (m): "))))

    # Point Loads
    num_loads = int(input("Enter number of point loads: "))
    loads, positions = [], []
    for i in range(num_loads):
        load = float(input(f"Load {i + 1} magnitude (N): "))
        position = float(input(f"Load {i + 1} position (m): "))
        direction = input("Direction (up/down): ").strip().lower()
        load = load if direction == 'up' else -load
        loads.append(load)
        positions.append(position)

    # Moments
    moments, moment_positions, moment_directions = [], [], []
    num_moments = int(input("Enter number of moments: "))
    for i in range(num_moments):
        moment = float(input(f"Moment {i + 1} magnitude (Nm): "))
        position = float(input(f"Moment {i + 1} position (m): "))
        direction = input("Moment direction (anticlockwise/clockwise): ").strip().lower()
        moments.append(moment)
        moment_positions.append(position)
        moment_directions.append(direction)

    # Distributed Loads
    distributed_loads = []
    num_distributed = int(input("Number of distributed loads: "))
    for _ in range(num_distributed):
        dist_type = input("Type (rectangular/triangular/trapezoidal): ").strip().lower()
        direction = input("Direction (up/down): ").strip().lower()
        
        orientation = None
        if dist_type in ['triangular', 'trapezoidal']:
            orientation = input(f"Is the peak intensity at the start or end for {dist_type}? (start/end): ").strip().lower()

        if dist_type == 'trapezoidal':
            w = float(input("Lower intensity (N/m): "))
            w2 = float(input("Higher intensity (N/m): "))
            start = float(input("Start position (m): "))
            end = float(input("End position (m): "))
            distributed_loads.append((w, w2, start, end, dist_type, orientation, direction))
        else:  
            w = float(input("Intensity (N/m): "))
            start = float(input("Start position (m): "))
            end = float(input("End position (m): "))
            distributed_loads.append((w, start, end, dist_type, orientation, direction))

    return beam_length, loads, positions, supports, moments, moment_positions, moment_directions, distributed_loads

