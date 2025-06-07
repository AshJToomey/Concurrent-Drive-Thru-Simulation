import time
import random
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

class Car:
    def __init__(self, car_id):
        self.car_id = car_id
        self.order = random.choice(["Burger", "Fries", "Nuggets", "Salad", "Coffee"])
        self.status = "Waiting"
        
    def log(self, message):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {self.car_id} - {message}")

def process_car(car):
    car.log(f"arrived and ordering {car.order}")
    time.sleep(random.uniform(1, 2)) # Ordering
    car.log("is paying")
    time.sleep(random.uniform(0.5, 1.5)) # Payment
    car.log(f"picked up {car.order} and left\n")

def main():
    cars = [Car(f"CAR-{i}") for i in range(1, 11)]
    
    with ThreadPoolExecutor(max_workers=3) as executor:  # 3 drive-thru lanes
        executor.map(process_car, cars)

if __name__ == "__main__":
    main()

