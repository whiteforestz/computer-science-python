# https://en.wikipedia.org/wiki/Netpbm

CHAN_P1 = 'P1'
CHAN_P2 = 'P2'
CHAN_P3 = 'P3'

CHAN = {
    CHAN_P1: 1,
    CHAN_P2: 2,
    CHAN_P3: 3,
}

with open('img.pnm') as im_file:
    raw_chan = im_file.readline().replace('\n', '')
    chan = CHAN[raw_chan]

    (width, height) = map(int, im_file.readline().replace('\n', '').split())

    im = []
    for y in range(0, height):
        row = []
        for x in range(0, width):
            r = int(im_file.readline().replace('\n', ''))
            g = int(im_file.readline().replace('\n', ''))
            b = int(im_file.readline().replace('\n', ''))
            row.append((r, g, b))
        im.append(row)

# gray = (r + g + b) / 3
with open('gray.pnm', 'w') as im_file:
    im_file.write(f'{CHAN_P2}\n')
    im_file.write(f'{width} {height}\n')

    for y in range(0, height):
        for x in range(0, width):
            (r, g, b) = im[y][x]
            gray = (r + g + b) // 3
            im_file.write(f'{gray}\n')
