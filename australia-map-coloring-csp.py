def is_consistent(state, color, assignment, neighbors):
    for neighbor in neighbors.get(state, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack_search(assignment, states, domains, neighbors):
    if len(assignment) == len(states):
        return assignment

    unassigned_states = [s for s in states if s not in assignment]
    current_state = unassigned_states[0]

    for color in domains[current_state]:
        if is_consistent(current_state, color, assignment, neighbors):
            assignment[current_state] = color
            
            result = backtrack_search(assignment, states, domains, neighbors)
            if result is not None:
                return result
                
            del assignment[current_state]
            
    return None

def solve_australia_map():
    states = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']
    
    colors = ['Red', 'Green', 'Blue']
    domains = {state: colors for state in states}
    
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }
    
    solution = backtrack_search({}, states, domains, neighbors)
    
    if solution:
        print("CSP Solution Found:")
        print("-" * 20)
        for state in states:
            print(f"{state:<4} : {solution[state]}")
    else:
        print("No solution exists with the given constraints.")

if __name__ == "__main__":
    solve_australia_map()