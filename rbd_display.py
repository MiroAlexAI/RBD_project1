import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib.colors as mcolors

import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib.colors as mcolors




import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib.colors as mcolors

def display_graph(graph):
    pos = left_to_right_layout(graph)
    
    # Получение меток надежности для каждого узла
    labels = nx.get_node_attributes(graph, 'reliability')
    
    # Настройка цвета узлов: от белого до красного в зависимости от значения надежности
    node_colors = [mcolors.to_hex((1- labels[node], 0.6, 0.4)) for node in graph.nodes()]
    
    # Отрисовка графа с заданными цветами узлов
    nx.draw(graph, pos, with_labels=False, node_color=node_colors, node_size=2000, font_size=10, font_weight="bold", arrows=True)
    
    # Добавляем метки для узлов: название + значение надежности
    nx.draw_networkx_labels(graph, pos, labels={k: f"{k}\n({v:.2f})" for k, v in labels.items()}, font_size=10)

    # Отображение меток на рёбрах (если нужно)
    nx.draw_networkx_edge_labels(graph, pos)
    
    # Отображаем таблицу с параметрами всех узлов
    display_node_table(graph)
    
    # Показ графа
    plt.show()

def left_to_right_layout(graph):
    pos = {}
    levels = list(nx.topological_sort(graph))
    level_dict = defaultdict(int)

    for i, node in enumerate(levels):
        level = len(nx.ancestors(graph, node))
        pos[node] = (level, level_dict[level])
        level_dict[level] += 1

    return pos

def display_node_table(graph):
    # Получение информации о всех узлах для отображения в таблице
    node_data = [(node, f"{graph.nodes[node]['reliability']:.2f}") for node in graph.nodes()]
    
    # Создание новой фигуры для отображения таблицы
    fig, ax = plt.subplots(figsize=(4, 1 + 0.25 * len(node_data)))  # размер подстраивается под количество узлов
    ax.set_axis_off()  # убираем оси
    
    # Добавляем таблицу в matplotlib
    table = ax.table(cellText=node_data, colLabels=["Node", "Reliability"], loc="center", cellLoc="center")
    
    # Настройка размеров колонок
    table.auto_set_column_width([0, 1])
    
    # Отображаем таблицу
    plt.show()

