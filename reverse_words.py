spaces = [" "]

instr = "I don't know what the speed implications of building your strings as lists and then .join()ing them are, but I find it's generally the cleanest way. I've also had great successes with using %s notation within a string for a SQL templating engine I wrote."

def rev1(instr):
    out = ""
    i = len(instr) - 1
    lastspace = len(instr)
    while i >= -1:

        char = instr[i]
        if char in spaces or i == -1:
            out += instr[i+1:lastspace] + " "
            lastspace = i
        i = i - 1

    print(out)


def reverse_string(instr, start_index, end_index):

    while start_index < end_index:
        char = instr[start_index]
        instr[start_index] = instr[end_index]
        instr[end_index] = char
        start_index = start_index + 1
        end_index = end_index - 1
        # print(start_index, end_index, char)

    # print("".join(instr))
    return instr



def rev2(instr):
    start_index = 0
    end_index = len(instr) - 1
    instr = reverse_string(list(instr), 0, end_index)
    for end_index in range(len(instr)):
        if instr[end_index] == " " or end_index == len(instr):
            instr = reverse_string(instr, start_index, end_index - 1)
            start_index = end_index + 1
    print("".join(instr))


rev1(instr)
rev2(instr)