import sys

INCREASING=1
DECREASING=2

def process_sliding_window(working_keys, text):
    window_start = 0
    window_length = 1
    max_len = 1
    keyset = { text[0] : 1 }
    direction = INCREASING

    while window_length + window_start < len(text):
        if direction == INCREASING:
            window_length += 1
            char = text[window_start + window_length - 1]
            if keyset.has_key(char):
                keyset[char] += 1
            else:
                keyset[char] = 1

            if len(keyset) > working_keys:
                direction = DECREASING
            else:
                if window_length > max_len:
                    max_len = window_length
        else:
            char = text[window_start]

            keyset[char] -= 1
            if keyset[char] == 0:
                del(keyset[char])
                if len(keyset) <= working_keys:
                    direction = INCREASING

            window_start += 1
            window_length -=1
    
    return max_len

def process_single_brute_force(working_keys, text):
    max_len = 1
    for index in range(0, len(text)-1):
        diff = 1
        offset = 0
        keyset = [ text[index] ]
        while diff <= working_keys:
            offset += 1
            if index + offset >= len(text):
                break

            key = text[index + offset]
            if key not in keyset:
                keyset.append(key)
                diff += 1

        max_len = max(offset, max_len)
    return max_len

def process_single(working_keys, text):
    return process_sliding_window(working_keys, text)

def process(data):
    lines = data.split('\n')
    idx = 0
    output = ""
    while lines[idx] != '0':
        keys = int(lines[idx])
        string = lines[idx+1]
        idx += 2
        if idx > len(lines): break
        output += repr(process_single(keys, string)) + "\n"
    return output

if __name__=='__main__':
    while 1:
        try:
            working_keys = int(sys.stdin.readline())
            if working_keys == 0:
                break
            text = sys.stdin.readline().rstrip('\n')
            print(process_single(working_keys, text))
        except:
            break

