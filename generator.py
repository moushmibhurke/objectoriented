def remote_control_next():
    yield "cnn"
    yield "HBO"
    yield "espn"
    yield "bbc"
    yield "zee news"
    yield "republic bharat"

for c in remote_control_next():
    print(c)
itr=remote_control_next()
#or
print(next(itr))
print(next(itr))
print(next(itr))
