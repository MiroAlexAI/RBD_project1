import pandas as pd

def save_to_file(graph, filename):
    data = []
    for node, attrs in graph.nodes(data=True):
        # Для каждого узла сохраняем его надежность и затем все его связи
        for succ in graph.successors(node):
            # Сохраняем информацию о связи и надежности узлов
            data.append([node, attrs['reliability'], succ, graph.nodes[succ]['reliability']])

    # Создаем DataFrame с нужными заголовками
    df = pd.DataFrame(data, columns=['From', 'Reliability1', 'To', 'Reliability2'])
    
    # Сохраняем в CSV файл
    df.to_csv(filename, index=False)
    print(f"Граф сохранен в файл {filename}.")

def load_from_file(graph, filename):
    try:
        df = pd.read_csv(filename)
        graph.clear()
        for index, row in df.iterrows():
            from_node = row['From']
            to_node = row['To']
            reliability1 = row['Reliability1']
            reliability2 = row['Reliability2']
            
            # Добавляем узлы с указанной надежностью
            graph.add_node(from_node, reliability=reliability1)
            graph.add_node(to_node, reliability=reliability2)
            graph.add_edge(from_node, to_node)
        
        print(f"Граф загружен из файла {filename}.")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
