def get_codes():
    results = []
    with open('./emojis.txt') as f: lines = f.read().split('\n')
    for l in lines:
        temp = l.split(';')[0].strip().split('..')
        if len(temp) > 1:
            results.append( [int(temp[0], 16), int(temp[1], 16)] )
        else:
            results.append( [int(temp[0], 16)] )

    return results

EMOJI_CODES = get_codes()

def is_emoji(c):
    for o in EMOJI_CODES:
        if len(o) > 1:
            if o[0] <= ord(c) and ord(c) <= o[1]:
                return True
        else:
            if ord(c) == o[0]:
                return True

    return False

def has_emoji(s):
    for i in range(0, int(len(s) / 2)):
        if is_emoji(s[i]): return True
        if is_emoji(s[len(s) - i - 1]): return True

    if len(s) % 2 > 0:
        return is_emoji(s[int(len(s) / 2)])

    return False

def get_emojis(s):
    results = []
    for i in range(0, int(len(s) / 2)):
        if is_emoji(s[i]): results.append((i, s[i]))
        if is_emoji(s[len(s) - i - 1]): results.append((len(s) - i - 1, s[len(s) - i - 1]))

    if len(s) % 2 > 0:
        idx = int(len(s) / 2) + 1
        if is_emoji(s[idx]): results.append((idx, s[idx]))

    return results
