
import os

class add_head:
    def add(self):
        input = "C:\\Users\\Liu\\Desktop\\final_data\output\\"
        output = "C:\\Users\\Liu\\Desktop\\final_data\\output\\final_data\\"
        dir_f = os.listdir(input)
        for x in dir_f:
            if x.endswith('.xml'):
                infile = open(input + x, 'r')
                outfile = open(output + x, 'w')
                for line in infile:
                    if line.startswith('<TEXT>'):
                        outfile.write('<TEXT><![CDATA[\n')
                    elif line.startswith('</TEXT>'):
                        outfile.write(']]></TEXT>\n')
                    else:
                        outfile.write(line)

a = add_head()
a.add()
