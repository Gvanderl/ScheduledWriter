import pusher

for i in range(pusher.get_pushes_for_day()):
    pusher.write_new_line()
    pusher.push_text()