import os
import sys
import networkx as nx # Graph library. Include data structures and algorithms

from heuristics import Heuristics

def read_instance(file_path):
    """
    Reads an instance file.
    The expected format is:
    First line: <number_of_nodes> <number_of_edges>
    Subsequent lines: <node_u> <node_v> <weight>
    """
    with open(file_path, 'r') as file:
        # Read the first line to get the number of nodes and edges
        first_line = file.readline().strip().split()
        if not first_line:
            return None
            
        num_nodes = int(first_line[0])
        num_edges = int(first_line[1])
        
        G = nx.Graph()
        G.add_nodes_from(range(num_nodes))
        
        # Parse the remaining lines for the edges
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 3:
                # Can be int or float for weights, using float to be safe
                u = int(parts[0])
                v = int(parts[1])
                weight = float(parts[2])
                G.add_edge(u, v, weight=weight)
                
        return G

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <instance_name> <algorithm> ")
        return

    instance_name = sys.argv[1]
    algorithm = sys.argv[2]

    # Construct the path to the 'instancias' directory relative to this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    instances_dir = os.path.join(base_dir, 'instancias')
    file_path = os.path.join(instances_dir, instance_name)
    
    if not os.path.exists(file_path):
        print(f"Instance file not found: {file_path}")  
        return
    
    print(f"Processing {instance_name} with algorithm '{algorithm}'...")
    instance_data = read_instance(file_path)
    
    if instance_data is not None:
        print(f"  -> Nodes: {instance_data.number_of_nodes()}, Edges: {instance_data.number_of_edges()}")
        heuristics = Heuristics(instance_data)
        
        match algorithm:
            case "construtiva" | "construtivo" | "guloso" | "gulosa":
                heuristics.construtiva()
                # Add algorithm 1 logic here
            # case "local":
                # Add algorithm 2 logic here
            case _:
                print(f"Unknown algorithm: {algorithm}")

        heuristics.evaluate()
if __name__ == '__main__':
    main()
