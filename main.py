def task_5():
    import random
    tablica = []
    tablica2 = ['abecadlo', 'z', 'pieca', 'spadlo', 'musztarda', 'pilot', 'telefon']
    for i in range(0, 10):
        tablica.append(random.randint(1, 100))

    def sort(tablica):
        for i in range(len(tablica) - 1, 0, -1):
            for j in range(i):
                if tablica[j] > tablica[j + 1]:
                    tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]

    sort(tablica)
    print(tablica)
    sort(tablica2)
    print(tablica2)
def task_6():
    zdanie = input("podaj zdanie: ")
    tablica = []

    tablica = zdanie.split(' ')

    def sort(tablica):
        for i in range(len(tablica) - 1, 0, -1):
            for j in range(i):
                if tablica[j] > tablica[j + 1]:
                    tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    def sort2(tablica):
        for i in range(len(tablica) - 1, 0, -1):
            for j in range(i):
                if len(tablica[j]) > len(tablica[j + 1]):
                    tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    sort(tablica)
    print(tablica)
    sort2(tablica)
    print(tablica)

def task_7():
        import random
        def sort(tablica):
            for i in range(len(tablica) - 1, 0, -1):
                for j in range(i):
                    if tablica[j] > tablica[j + 1]:
                        tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]

        tablica2 = []

        for j in range(100):
            string = ""
            tablica1 = []
            for i in range(random.randrange(3, 9)):
                tablica1.append(random.randrange(97, 123))
                string += (chr(tablica1[i]))
            tablica2.append(string)
        sort(tablica2)
        print(tablica2)

def task_71():
    import random
    tablica2 = []
    litery = [97, 101, 105, 111, 117, 121]

    def sort(tablica):
        for i in range(len(tablica) - 1, 0, -1):
            for j in range(i):
                if tablica[j] > tablica[j + 1]:
                    tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]

    for j in range(100):
        string = ""
        tablica1 = []
        for i in range(random.randrange(3, 9)):
            tablica1.append(random.randrange(97, 123))

            if (i + 1) % 3 == 0 and i != 0:
                if tablica1[i] not in litery:
                    tablica1[i] = random.choice(litery)

            if i > 0:
                if tablica1[i] == tablica1[i - 1]:
                    while tablica1[i] == tablica1[i - 1]:
                        tablica1[i] = random.randrange(97, 123)

            string += (chr(tablica1[i]))
        tablica2.append(string)

    sort(tablica2)
    print(tablica2)


def main():
    task_5()
    task_6()
    task_7()
    task_71()






if __name__ == '__main__':
    main()