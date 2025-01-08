from distributed_loads import convert_distributed_loads
from reactions import calculate_reactions
from user_input import get_user_input

def main():
    """Main function to run the beam analysis with detailed output."""
    # Collect user input
    beam_length, loads, positions, supports, moments, moment_positions, moment_directions, distributed_loads = get_user_input()
    
    # Convert distributed loads to point loads
    equivalent_loads, equivalent_positions = convert_distributed_loads(distributed_loads)
    
    # Combine all loads and positions
    loads.extend(equivalent_loads)
    positions.extend(equivalent_positions)

    # Display detailed information about the loads
    print("\n--- Load Summary ---")
    for i, (load, position) in enumerate(zip(loads, positions)):
        print(f"Load {i + 1}: Magnitude = {load} N at position = {position} m")

    # Display detailed information about the distributed loads
    if distributed_loads:
        print("\n--- Distributed Load Conversion Summary ---")
        for i, (F_eq, x_eq) in enumerate(zip(equivalent_loads, equivalent_positions)):
            print(f"Distributed Load {i + 1}: Equivalent Force = {F_eq} N, Position = {x_eq} m")

    # Display moments if any
    if moments:
        print("\n--- Moment Summary ---")
        for i, (moment, pos, direction) in enumerate(zip(moments, moment_positions, moment_directions)):
            print(f"Moment {i + 1}: Magnitude = {moment} Nm, Position = {pos} m, Direction = {direction}")

    # Display support details
    print("\n--- Support Summary ---")
    for support in supports:
        print(f"{support[0].capitalize()} Support at position = {support[1]} m")

    # Calculate reactions
    reactions = calculate_reactions(beam_length, loads, positions, supports, moments, moment_positions, moment_directions)

    # Display reactions in detail
    print("\n--- Reactions Summary ---")
    if len(supports) == 1:
        support_type, support_position = supports[0]
        if support_type == "simple":
            print(f"Reaction at {support_type.capitalize()} Support (position {support_position} m): R_A = {reactions[0]} N")
        elif support_type == "fixed":
            print(f"Reaction at {support_type.capitalize()} Support (position {support_position} m): R_A = {reactions[0]} N, Moment = {reactions[1]} Nm")
    elif len(supports) == 2:
        (support_A, support_B) = supports
        print(f"Reaction at {support_A[0].capitalize()} Support (position {support_A[1]} m): R_A = {reactions[0]} N")
        print(f"Reaction at {support_B[0].capitalize()} Support (position {support_B[1]} m): R_B = {reactions[1]} N")
    else:
        print("Invalid support configuration!")

    print("\n--- Analysis Completed Successfully! ---")

if __name__ == "__main__":
    main()

