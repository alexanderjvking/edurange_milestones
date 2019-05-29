## Milestone checking for Total_Recon
## we are checking for two conditions
## for each milestone if only one is
## met they will be highlighted in red
## instead of yellow
## if milestone is found in dot file
## highlight (red=only half of milestone) 
## (yellow= full milestone completed)
## b3rp
## 5/13/19

import sys
import os
import pydot

def milestone_check(s, out):
    milestones_nmap = {
            'REKALL_nmap' : [1,False],
            'SUBWAY_nmap' : [2,False],
            'EARTH_AERO_PORT_nmap' : [3, False],
            'MARS_AERO_PORT_nmap' : [4,False],
            'VENUSVILLE_nmap' : [5,False],
            'LAST_RESORT_nmap' : [6,False],
            'RESISTANCE_BASE_nmap' : [7,False],
            'CONTROL_ROOM_nmap' : [8,False]

    }
    milestones_ssh = {
            'REKALL_ssh' : [1,False],
            'SUBWAY_ssh' : [2,False],
            'EARTH_AERO_PORT_ssh' : [3, False],
            'MARS_AERO_PORT_ssh' : [4,False],
            'VENUSVILLE_ssh' : [5,False],
            'LAST_RESORT_ssh' : [6,False],
            'RESISTANCE_BASE_ssh' : [7,False],
            'CONTROL_ROOM_ssh' : [8,False]

    }
    read_lines = s.splitlines()

    for l in read_lines:
        out_str = ""
        #first instance HOME -> REKALL
        if not milestones_nmap['REKALL_nmap'][1] and not milestones_ssh['REKALL_ssh'][1]:
            if 'nmap' in l and '10.0.0.4' in l:
                milestones_nmap['REKALL_nmap'][1] = True
            if 'ssh' in l and '10.0.0.4' in l and '444' in l:
                milestones_ssh['REKALL_ssh'][1] = True
            if milestones_nmap['REKALL_nmap'][1] or milestones_ssh['REKALL_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=red" + l[-1:]
                out.write(out_str + '\n')
            if milestones_nmap['REKALL_nmap'][1] and milestones_ssh['REKALL_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')

        #REKALL -> SUBWAY
        if not milestones_nmap['SUBWAY_nmap'][1] and not milestones_ssh['SUBWAY_ssh'][1]:
            if 'nmap' in l and '10.0.0.0/24' in l:
                milestones_nmap['SUBWAY_nmap'][1] = True
            if 'ssh' in l and '10.0.0.17' in l:
                milestones_ssh['SUBWAY_ssh'][1] = True
            if milestones_nmap['SUBWAY_nmap'][1] or milestones_ssh['SUBWAY_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=red" + l[-1:]
                out.write(out_str + '\n')
            if milestones_nmap['SUBWAY_nmap'][1] and milestones_ssh['SUBWAY_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')

        #SUBWAY -> EARTH_AERO_PORT
        if not milestones_nmap['EARTH_AERO_PORT_nmap'][1] and not milestones_ssh['EARTH_AERO_PORT_ssh'][1]:
            if 'nmap' in l and '-Pn' in l and '10.0.0.55' in l:
                milestones_nmap['EARTH_AERO_PORT_nmap'][1] = True
            if 'ssh' in l and '10.0.0.55' in l and '666' in l:
                milestones_ssh['EARTH_AERO_PORT_ssh'][1] = True
            if milestones_nmap['EARTH_AERO_PORT_nmap'][1] or milestones_ssh['EARTH_AERO_PORT_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=red" + l[-1:]
                out.write(out_str + '\n')
            if milestones_nmap['EARTH_AERO_PORT_nmap'][1] and milestones_ssh['EARTH_AERO_PORT_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')

        #EARTH_AERO_PORT -> MARS_AERO_PORT
        if not milestones_nmap['MARS_AERO_PORT_nmap'][1] and not milestones_ssh['MARS_AERO_PORT_ssh'][1]:
            if 'nmap' in l and '10.0.192.0/18' in l:
                milestones_nmap['MARS_AERO_PORT_nmap'][1] = True
            if 'ssh' in l and '10.0.200.33' in l:
                milestones_ssh['MARS_AERO_PORT_ssh'][1] = True
            if milestones_nmap['MARS_AERO_PORT_nmap'][1] or milestones_ssh['MARS_AERO_PORT_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=red" + l[-1:]
                out.write(out_str + '\n')
            if milestones_nmap['MARS_AERO_PORT_nmap'][1] and milestones_ssh['MARS_AERO_PORT_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')

        #MARS_AERO_PORT -> VENUSVILLE
        if not milestones_nmap['VENUSVILLE_nmap'][1] and not milestones_ssh['VENUSVILLE_ssh'][1]:
            if 'nmap' in l and '10.0.208.64' in l:
                milestones_nmap['VENUSVILLE_nmap'][1] = True
            if 'ssh' in l and '10.0.208.64' in l and '123' in l:
                milestones_ssh['VENUSVILLE_ssh'][1] = True
            if milestones_nmap['VENUSVILLE_nmap'][1] or milestones_ssh['VENUSVILLE_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=red" + l[-1:]
                out.write(out_str + '\n')
            if milestones_nmap['VENUSVILLE_nmap'][1] and milestones_ssh['VENUSVILLE_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')

        #VENUSVILLE -> LAST_RESORT
        if not milestones_nmap['LAST_RESORT_nmap'][1] and not milestones_ssh['LAST_RESORT_ssh'][1]:
            if 'nmap' in l and '10.0.0-255.144' in l:
                milestones_nmap['LAST_RESORT_nmap'][1] = True
            if 'ssh' in l and '10.0.244.144' in l and '2345' in l:
                milestones_ssh['LAST_RESORT_ssh'][1] = True
            if milestones_nmap['LAST_RESORT_nmap'][1] or milestones_ssh['LAST_RESORT_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=red" + l[-1:]
                out.write(out_str + '\n')
            if milestones_nmap['LAST_RESORT_nmap'][1] and milestones_ssh['LAST_RESORT_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')

        #LAST_RESORT -> RESISTANCE
        if not milestones_nmap['RESISTANCE_BASE_nmap'][1] and not milestones_ssh['RESISTANCE_BASE_ssh'][1]:
            if 'nc' in l and '-zv' in l and '10.0.234.8' in l:
                milestones_nmap['RESISTANCE_BASE_nmap'][1] = True
            if 'ssh' in l and '10.0.234.8' in l and '632' in l:
                milestones_ssh['RESISTANCE_BASE_ssh'][1] = True
            if milestones_nmap['RESISTANCE_BASE_nmap'][1] or milestones_ssh['RESISTANCE_BASE_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=red" + l[-1:]
                out.write(out_str + '\n')
            if milestones_nmap['RESISTANCE_BASE_nmap'][1] and milestones_ssh['RESISTANCE_BASE_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')

        #RESISTANCE -> CONTROL_ROOM
        if not milestones_nmap['CONTROL_ROOM_nmap'][1] and not milestones_ssh['CONTROL_ROOM_ssh'][1]:
            if 'nmap' in l and '10.0.250.5' in l:
                milestones_nmap['CONTROL_ROOM_nmap'][1] = True
            if 'ssh' in l and '10.0.250.5' in l and '1938' in l:
                milestones_ssh['CONTROL_ROOM_ssh'][1] = True
            if milestones_nmap['CONTROL_ROOM_nmap'][1] or milestones_ssh['CONTROL_ROOM_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=red" + l[-1:]
                out.write(out_str + '\n')
            if milestones_nmap['CONTROL_ROOM_nmap'][1] and milestones_ssh['CONTROL_ROOM_ssh'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')

        #if not a milestone
        if out_str == "":
            out_str = l
            out.write(out_str + "\n")

def main(input_file):
    with open(input_file) as fp:
        s = fp.read()
    output_file = 'TR_MST_'+input_file
    out = open(output_file, 'w')
    milestone_check(s, out)

    fp.close()
    out.close()

    (graph,) = pydot.graph_from_dot_file(output_file)
    graph.write_png(output_file+'.png')

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print('dot file needed')
        exit(1)
    main(sys.argv[1])
