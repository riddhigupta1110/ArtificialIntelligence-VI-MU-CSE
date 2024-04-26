import networkx as nx
import matplotlib.pyplot as plt

def joint_probability(burglary, earthquake, alarm, john_calls, mary_calls):
    burglary_p = 0.001
    earthquake_p = 0.002

    # Conditional Probability Tables (CPTs)
    p_alarm_given_BE = {
        (True, True): 0.95, 
        (True, False): 0.94, 
        (False, True): 0.29, 
        (False, False): 0.001
    }
    p_john_calls_given_alarm = {
        True: 0.9, 
        False: 0.05
    }
    p_mary_calls_given_alarm = {
        True: 0.7,  
        False: 0.01
    }

    # Calculate probabilities based on input
    p_burglary = burglary_p if (burglary == True) else (1 - burglary_p)
    p_earthquake = earthquake_p if (earthquake == True) else (1 - earthquake_p)
    p_alarm = p_alarm_given_BE[(burglary, earthquake)] if (alarm == True) else (1 - p_alarm_given_BE[(burglary, earthquake)])
    p_john_calls = p_john_calls_given_alarm[john_calls]
    p_mary_calls = p_mary_calls_given_alarm[mary_calls]

    # Joint probability calculation
    return p_alarm * p_burglary * p_earthquake * p_john_calls * p_mary_calls

b = True if (input("Enter if Burglary happened: ") == "T") else False
e = True if (input("Enter if Earthquake happened: ") == "T") else False
a = True if (input("Enter if Alarm rang: ") == "T") else False
j = True if (input("Enter if John calls: ") == "T") else False
m = True if (input("Enter if Mary calls: ") == "T") else False

# Compute joint probability
p_query = joint_probability(b, e, a, j, m)

print(f"Probability of Burglary={b}, Earthquake={e}, Alarm={a}, John Calls={j}, Mary Calls={m}:", p_query)

G = nx.DiGraph()
G.add_nodes_from(["Burglary", "Earthquake", "Alarm", "John Calls", "Mary Calls"])
G.add_edges_from([("Burglary", "Alarm"), ("Earthquake", "Alarm"), ("Alarm", "John Calls"), ("Alarm", "Mary Calls")])

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000)
plt.title("Bayesian Network Diagram")
plt.show()