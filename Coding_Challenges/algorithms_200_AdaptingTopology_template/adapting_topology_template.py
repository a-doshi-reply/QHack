#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1],
    4: [1, 5, 7, 8],
    5: [4, 6],
    6: [5, 7],
    7: [4, 6],
    8: [4],
}


def n_swaps(cnot):
    """Count the minimum number of swaps needed to create the equivalent CNOT.

    Args:
        - cnot (qml.Operation): A CNOT gate that needs to be implemented on the hardware
        You can find out the wires on which an operator works by asking for the 'wires' attribute: 'cnot.wires'

    Returns:
        - (int): minimum number of swaps
    """

    # QHACK #
    wires=list(cnot.wires)
    start_node=wires[0]
    end_node=wires[1]
    found=False
    checked_nodes=set([start_node])
    working_nodes=set(graph[start_node])
    i=1
    
    if(end_node in working_nodes):
        return(0)
    
    while found==False:
        new_nodes=set()
        print(i)
        for node in working_nodes:
            new_nodes.update(set(graph[node]))
        checked_nodes.update(working_nodes)
        
        new_nodes=new_nodes.difference(checked_nodes)
        print(new_nodes)
        print(checked_nodes)
        
        
        if(end_node in new_nodes):
            found=True
        else:
            i+=1
            working_nodes=new_nodes
    return(i*2)
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    output = n_swaps(qml.CNOT(wires=[int(i) for i in inputs]))
    print(f"{output}")
