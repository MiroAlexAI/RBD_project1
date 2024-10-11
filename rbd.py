import networkx as nx

class RBD:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_component(self, name, reliability):
        """Добавить компонент в RBD схему с заданной надежностью"""
        if name in self.graph.nodes:
            print(f"Компонент {name} уже существует.")
        else:
            self.graph.add_node(name, reliability=reliability)
            print(f"Компонент {name} добавлен с надежностью {reliability}.")

    def add_connection(self, from_node, to_node):
        """Добавить связь между компонентами"""
        if from_node not in self.graph.nodes or to_node not in self.graph.nodes:
            print(f"Один из компонентов {from_node} или {to_node} не существует.")
        else:
            self.graph.add_edge(from_node, to_node)
            print(f"Связь между {from_node} и {to_node} добавлена.")

    def calculate_total_reliability(self):
        """Рассчитать общую надежность системы"""
        try:
            sequential_nodes = list(nx.topological_sort(self.graph))
            reliability_map = {}  # Словарь для хранения расчетной надежности узлов
            
            for node in sequential_nodes:
                # Если это исходный узел (нет входящих ребер)
                if self.graph.in_degree(node) == 0:
                    reliability_map[node] = self.graph.nodes[node]["reliability"]
                    
                else:
                    incoming_reliabilities = []
                    for pred in self.graph.predecessors(node):
                        incoming_reliabilities.append(reliability_map[pred])

                    # Определяем, параллельные ли узлы (больше одной связи)
                    is_parallel = self.graph.in_degree(node) > 1 or self.graph.out_degree(node) > 1

                    if is_parallel:
                        total_failure = 1
                        for rel in incoming_reliabilities:
                            total_failure *= (1 - rel)  # Вероятность отказа всех параллельных компонентов
                        reliability_map[node] = 1 - total_failure  # Надежность параллельных компонентов

                    else:
                        # Если узел последовательный, то просто передаем надежность
                        reliability_map[node] = incoming_reliabilities[0] * self.graph.nodes[node]["reliability"]

            # Надёжность последнего узла, если у него нет потомков
            last_node = sequential_nodes[-1]
            if last_node not in reliability_map:
                reliability_map[last_node] = self.graph.nodes[last_node]["reliability"]

            # Возвращаем надежность последнего узла
            return reliability_map[sequential_nodes[-1]]

        except nx.NetworkXUnfeasible:
            print("Ошибка в графе: циклы в графе недопустимы для RBD.")
            return None

    def identify_parallel_and_sequential_nodes(self):
        """Определить, какие узлы являются параллельными, а какие последовательными"""
        parallel_nodes = []
        sequential_nodes = []

        for node in self.graph.nodes:
            if self.graph.in_degree(node) > 1 or self.graph.out_degree(node) > 1:
                parallel_nodes.append(node)
            else:
                sequential_nodes.append(node)

        return parallel_nodes, sequential_nodes

