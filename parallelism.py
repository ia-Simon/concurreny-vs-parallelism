from concurrent.futures import ProcessPoolExecutor

def task(id: int):
  count = 0
  total = 10_000_000
  for _ in range(total):
    count += 1
    if count == total * 0.25:
      print(f"{id}: 25%")
    elif count == total * 0.50:
      print(f"{id}: 50%")
    elif count == total * 0.75:
      print(f"{id}: 75%")
    elif count == total:
      print(f"{id}: 100%") 

if __name__ == '__main__':
  with ProcessPoolExecutor(max_workers=4) as executor:
    executor.map(task, range(4))
