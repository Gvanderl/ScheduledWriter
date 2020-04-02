import pusher
from time import sleep

num_pushes = pusher.get_pushes_for_day()
for i in range(num_pushes):
    print(f"Push {i + 1}/{num_pushes}")
    pusher.write_new_line()
    pusher.push_text()
    if i < (num_pushes - 1):
        print("Waiting...")
        sleep(60)
    print("All done!")
