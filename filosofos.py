import threading
import time

NUM_FILOSOFOS = 3

garfos = [threading.Semaphore(1) for _ in range(NUM_FILOSOFOS)]

def filosofo(id):
    while True:
        print(f'Filósofo {id} está pensando.')

        time.sleep(4)

        garfo_esquerda = garfos[id]
        garfo_direita = garfos[(id + 1) % NUM_FILOSOFOS]

        garfo_esquerda.acquire()
        garfo_direita.acquire()

        print(f'Filósofo {id} está comendo.')

        garfo_esquerda.release()
        garfo_direita.release()

        print(f'Filósofo {id} terminou de comer.')

filosofos = [threading.Thread(target=filosofo, args=(i,)) for i in range(NUM_FILOSOFOS)]

for f in filosofos:
    f.start()

for f in filosofos:
    f.join()