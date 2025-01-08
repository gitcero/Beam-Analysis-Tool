def calculate_reactions(beam_length, loads, positions, supports, moments, moment_positions, moment_directions):
    """Calculate reactions for a beam with point loads, moments, and supports."""
    if len(supports) == 1:
        support_type, support_position = supports[0]
        if support_type == "simple":
            R_A = -sum(loads)
            return R_A, 0
        elif support_type == "fixed":
            R_A = -sum(loads)
            M_A = -sum([P * (x - support_position) for P, x in zip(loads, positions)])
            M_A -= sum([M if dir == 'anticlockwise' else -M for M, dir in zip(moments, moment_directions)])
            return R_A, M_A

    elif len(supports) == 2:
        x_A, x_B = [s[1] for s in supports]
        moment_contributions = sum([M if dir == 'anticlockwise' else -M for M, dir in zip(moments, moment_directions)])
        R_B_numerator = -sum([P * (x - x_A) for P, x in zip(loads, positions)]) - moment_contributions
        R_B = R_B_numerator / (x_B - x_A)
        R_A = -(sum(loads) + R_B)
        return R_A, R_B
    else:
        raise ValueError("The system is statically indeterminate with more than two supports.")
