from rbd import RBD
from rbd_io import save_to_file, load_from_file
from rbd_display import display_graph

def interactive_rbd():
    rbd_system = RBD()

    while True:
        print("\n1. Добавить компонент")
        print("2. Добавить связь")
        print("3. Рассчитать общую надежность")
        print("4. Отобразить граф")
        print("5. Сохранить граф в файл (CSV)")
        print("6. Загрузить граф из файла (CSV)")
        print("7. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Введите имя компонента: ")
            reliability = float(input("Введите вероятность надежности (например, 0.95): "))
            rbd_system.add_component(name, reliability)

        elif choice == '2':
            from_node = input("Введите имя компонента, откуда идёт связь: ")
            to_node = input("Введите имя компонента, куда идёт связь: ")
            rbd_system.add_connection(from_node, to_node)

        elif choice == '3':
            pri = rbd_system.identify_parallel_and_sequential_nodes()
            reliability = rbd_system.calculate_total_reliability()
            if reliability is not None:
                print(pri)
                print(f"Общая надежность системы: {reliability:.4f}")

        elif choice == '4':
            display_graph(rbd_system.graph)

        elif choice == '5':
            filename = input("Введите имя файла для сохранения (например, graph.csv): ")
            save_to_file(rbd_system.graph, filename)

        elif choice == '6':
            filename = input("Введите имя файла для загрузки (например, graph.csv): ")
            load_from_file(rbd_system.graph, filename)

        elif choice == '7':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")
