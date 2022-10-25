from concurrent.futures import ProcessPoolExecutor
import os

def task(id: int):
  count = 0
  target = int(os.getenv('LOOP_RUNS', 10_000_000))
  for _ in range(target):
    count += 1
    if count == target * 0.25:
      print(f"{id}: 25%")
    elif count == target * 0.50:
      print(f"{id}: 50%")
    elif count == target * 0.75:
      print(f"{id}: 75%")
    elif count == target:
      print(f"{id}: 100%") 

if __name__ == '__main__':
  with ProcessPoolExecutor(max_workers=int(os.getenv('MAX_WORKERS', 4))) as executor:
    executor.map(task, range(int(os.getenv('TASK_COUNT', 4))))
