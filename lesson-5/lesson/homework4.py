txt = 'abcabcdabcdeabcdefabcdefg'

done = 'aeiou'

counter = 0
ans = []
# ans = ""

for i in range(len(txt)):
    counter += 1
    ans += txt[i]
    if i != len(txt)-1 and counter >=3 and txt[i] not in done:
        done += txt[i]
        # ans += "_"
        ans.append('_')
        counter = 0

    print(''.join(ans))