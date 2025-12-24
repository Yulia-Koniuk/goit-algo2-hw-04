import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.DiGraph()

edges = [
    (1, 3, 25), (1, 4, 20), (1, 5, 15),
    (2, 4, 10), (2, 5, 15), (2, 6, 30),

    (3, 7, 15), (3, 8, 10), (3, 9, 20),
    (4,10, 15), (4,11, 10), (4,12, 25),
    (5,13, 20), (5,14, 15), (5,15, 10),
    (6,16, 20), (6,17, 10), (6,18, 15), (6,19, 5), (6,20, 10)
]

G.add_weighted_edges_from(edges)

pos = {
    1:(0,3), 2:(0,1),
    3:(2,4), 4:(2,3), 5:(2,2), 6:(2,1)
}

for i in range(1, 15):
    pos[6+i] = (4, 4 - i*0.3)


plt.figure(figsize=(16,8))
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="pink", arrows=True, font_size=10)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Логістична мережа: Термінали → Склади → Магазини")


plt.show()



def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()
        for neighbor in range(len(capacity_matrix)):
            if not visited[neighbor] and capacity_matrix[current_node][neighbor] - flow_matrix[current_node][neighbor] > 0:
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    return True
                queue.append(neighbor)
    return False


def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    parent = [-1] * num_nodes
    max_flow = 0

    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        path_flow = float('Inf')
        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(path_flow, capacity_matrix[previous_node][current_node] - flow_matrix[previous_node][current_node])
            current_node = previous_node
        
        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node
        
        max_flow += path_flow

    return max_flow, flow_matrix


# У всіх місцях, де вказано 500, це використовується як достатньо велика пропускна здатність, щоб суперджерело або суперсток не обмежували реальний потік у мережі.
# Тобто 500 не є реальною пропускною здатністю каналів, а технічним трюком для алгоритму.

capacity_matrix = [
    [0,500,500,0,  0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0,  0, 25, 20, 15, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0,  0, 0,  10, 15, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0,  0, 0,  0,  0,  0, 15,10,20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 15,10,25, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 20,15,10, 0, 0, 0, 0, 0, 0],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20,10,15, 5,10,0],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0, 0,  0, 0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,500],
    [0]*22 
]


source = 0   
sink = 21    

max_flow, flow_matrix = edmonds_karp(capacity_matrix, source, sink)
print(f"Максимальний потік: {max_flow}\n")



terminals = [1, 2]
warehouses = [3,4,5,6]
stores = list(range(7,21))  

flow_copy = [row[:] for row in flow_matrix]

print("Термінал\tМагазин\tФактичний Потік (одиниць)")

for t in terminals:
    for w in warehouses:
        if capacity_matrix[t][w] > 0: 
            for s in stores:
                if capacity_matrix[w][s] > 0: 
                    flow_to_store = min(flow_matrix[t][w], flow_matrix[w][s])

                    print(f"Термінал {t}\tМагазин {s-6}\t{flow_to_store}")

                    flow_matrix[t][w] -= flow_to_store
                    flow_matrix[w][s] -= flow_to_store


print("\nСумарний потік по терміналах:")
for t in terminals:
    total = sum(flow_copy[t][w] for w in warehouses)
    print(f"Термінал {t}: {total} одиниць")


print("\nПостачання по магазинах:")
for s in stores:
    received = sum(flow_copy[w][s] for w in warehouses)
    capacity = sum(capacity_matrix[w][s] for w in warehouses)
    percent = (received / capacity * 100) if capacity > 0 else 0
    print(f"Магазин {s-6}: отримано {received} одиниць ({percent:.1f}% від пропускної здатності)")


def node_name(v):
    if v in [1, 2]:
        return f"Термінал {v}"
    elif v in [3, 4, 5, 6]:
        return f"Склад {v}"
    elif 7 <= v <= 20:
        return f"Магазин {v - 6}"
    else:
        return None  


print("\nПовні маршрути з мінімальним фактичним потоком (0):")
print("Термінал → Склад → Магазин | Пропускна здатність")

for t in terminals:
    for w in warehouses:
        for s in stores:
            if capacity_matrix[t][w] > 0 and capacity_matrix[w][s] > 0:
                
                route_flow = min(flow_copy[t][w], flow_copy[w][s])

                if route_flow == 0:
                    terminal_name = f"Термінал {t}"
                    warehouse_name = f"Склад {w - 2}"
                    store_name = f"Магазин {s - 6}"

                    print(
                        f"{terminal_name} → {warehouse_name} → {store_name} | "
                        f"{capacity_matrix[w][s]}"
                    )



print("\nМаксимальна пропускна здатність від терміналів до складів:")

total_capacity_tw = 0
total_used_tw = 0

for t in terminals:
    for w in warehouses:
        if capacity_matrix[t][w] > 0:
            total_capacity_tw += capacity_matrix[t][w]
            total_used_tw += flow_copy[t][w]

percent_used_tw = (total_used_tw / total_capacity_tw * 100) if total_capacity_tw > 0 else 0

print(f"Загальна пропускна здатність: {total_capacity_tw} одиниць")
print(f"Фактично використано: {total_used_tw} одиниць")
print(f"Використано: {percent_used_tw:.1f}%")


print("\nМаксимальна пропускна здатність від складів до магазинів:")

total_capacity_ws = 0
total_used_ws = 0

for w in warehouses:
    for s in stores:
        cap = capacity_matrix[w][s]
        if cap > 0: 
            total_capacity_ws += cap
            total_used_ws += flow_copy[w][s]

percent_used_ws = (total_used_ws / total_capacity_ws * 100) if total_capacity_ws > 0 else 0

print(f"Загальна пропускна здатність: {total_capacity_ws} одиниць")
print(f"Фактично використано: {total_used_ws} одиниць")
print(f"Використано: {percent_used_ws:.1f}%")


print("\nРекомендації по збільшенню пропускної здатності терміналів → складів (повні маршрути):")

current_total_flow = sum(flow_copy[w][s] for w in warehouses for s in stores)

for w in warehouses:
    total_store_capacity = sum(capacity_matrix[w][s] for s in stores)
    total_flow_to_store = sum(flow_copy[w][s] for s in stores)
    remaining_capacity = total_store_capacity - total_flow_to_store

    if remaining_capacity <= 0:
        continue  

    terminal_flows = [(t, capacity_matrix[t][w]) for t in terminals if capacity_matrix[t][w] > 0]
    num_terminals = len(terminal_flows)

    for t, cap in terminal_flows:
        added_flow = round(remaining_capacity / num_terminals, 1)
        percent_increase = added_flow / current_total_flow * 100
        print(f"Маршрут: Термінал {t} → Склад {w-2} | додати {added_flow} одиниць "
              f"(потенційне покращення загального потоку: {percent_increase:.1f}%)")


print("\nДетальний звіт з аналізом отриманих результатів знаходиться у файлі README")
















