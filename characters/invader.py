def read_frames(name):
    frames = []
    frame = []

    f = open('./' + name + '.dat', 'r')

    for line in f:
        line = line.strip()

        if len(line) == 0:
            continue

        if line == '-':
            frames.append(frame)
            frame = []
            continue

        frame.append(tuple(map(int, line.split())))

    frames.append(frame)

    return frames
