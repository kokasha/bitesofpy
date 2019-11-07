INDENTS = 4

rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """

def print_hanging_indents(poem):
    lines = poem.strip().splitlines()
    for line in lines:
        line = line.strip()
        print('{4:>10}'.format('line clear'))
        # print('{:>10}'.format(line.strip()))

print_hanging_indents(rosetti_unformatted)