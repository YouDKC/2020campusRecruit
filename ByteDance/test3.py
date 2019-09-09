blocks_count, max_digit, game_times = [int(i) for i in input().strip().split(' ')]
blocks_all = [i for i in input().strip().split(' ')]
for i in range(len(blocks_all)):
    if i not in {'<','>'}:
        blocks_all[i] = int(blocks_all[i])
while game_times>0:
    game_times -= 1
    start,end = [int(i) for i in input().strip().split(' ')]
    blocks = blocks_all[start:end+1]
    # 可能存在边界问题
    res = 0
    last_block = -1
    direction = 'right'
    while len(blocks)>0:
        if len(blocks)==0 and blocks in {'>', '<',0}:
            break
        if blocks[i] in {'>','<'}:
            if blocks[i] == '>':
                direction = 'right'
                i+=1
            elif  blocks[i] == '<':
                direction = 'left'
                i-=1

            if last_block in {'>', '<'}:
                blocks = blocks[:i]+blocks[i+1:]
            else:
                last_block = blocks[i]
        elif blocks[i] not in {'>','<'}:
            res += blocks[i]
            blocks[i] -= 1
            if direction == 'right':
                i += 1
            elif direction == 'left':
                i -= 1
            if last_block == 0:
                blocks = blocks[:i]+blocks[i+1:]
            if last_block==0:
                blocks = blocks[:i]+blocks[i+1:]
            else:
                last_block = blocks[i]
    print(res)
