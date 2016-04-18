import sys

INCREASING=1
DECREASING=2

# The logic is this: we increase the size of the window until there are
# more characters within it than working keys, then shrink it from the left
# until there are not, and repeat until the window touches the end of the
# string
def process_sliding_window(working_keys, text):
    window_start = 0
    window_length = 1
    max_len = 1 # running tally

    keyset = { text[0] : 1 } # keep track of the letters in the window
    direction = INCREASING

    while window_length + window_start < len(text):
        if direction == INCREASING:
            # Increase the size of the window and make a note of the new
            # character
            window_length += 1
            char = text[window_start + window_length - 1]
            if keyset.has_key(char):
                keyset[char] += 1
            else:
                keyset[char] = 1

            # If we're now too big, shrink the window
            if len(keyset) > working_keys:
                direction = DECREASING
            else:
                # Otherwise, if we're bigger than our previous max, make a note
                if window_length > max_len:
                    max_len = window_length
        else:
            # If we're shrinking, we need to remove the letter at the start
            # of the window from our records
            char = text[window_start]
            keyset[char] -= 1

            # And shrink the window from the left
            window_start += 1
            window_length -=1

            # If there are no remaining instances of that letter in our window
            # then check to see if we can start increasing the size of the
            # window again (this should always be true, I think)
            if keyset[char] == 0:
                del(keyset[char])
                if len(keyset) <= working_keys:
                    direction = INCREASING

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

