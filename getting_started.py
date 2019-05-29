## Milestone checking for gettingStarted
## if milestone is found in dot file
## highlight
## credit to Aashrays milestone checking
## b3rp
## 3/13/19

import sys
import os
import pydot

def milestone_check(s, out):
    milestones = {
            'go_to_bin' : [1,False],
            'followMe' : [2,False],
            'man_file' : [3, False],
            'cat_file' : [4,False],
            'combine_files' : [5,False],
            'edit_file' : [6,False],
            'find_edurange' : [7,False],
            'final_mission' : [8,False]
    }

    read_lines = s.splitlines()

    for l in read_lines:
        out_str = ""
        #cd to bin
        if not milestones['go_to_bin'][1]:
            if 'cd' in l and 'bin' in l:
                milestones['go_to_bin'][1] = True
            if milestones['go_to_bin'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')
        # cd to okYouAreHERE!
        if not milestones['followMe'][1]:
            if l.find('okYouAreHERE') !=-1:
                milestones['followMe'][1] = True
            if milestones['followMe'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')
        # man file
        if not milestones['man_file'][1]:
            if 'man' in l and 'file' in l:
                milestones['man_file'][1] = True
            if milestones['man_file'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')
        # cat imatextfiletoo.txt
        if not milestones['cat_file'][1]:
            if 'cat' in l and 'imatextfiletoo.txt' in l:
                milestones['cat_file'][1] = True
            if milestones['cat_file'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')
        # cat one.txt two.txt three.txt > alltogether.txt
        if not milestones['combine_files'][1]:
            if 'cat' in l and 'one.txt' in l and 'two.txt' in l and 'three.txt' in l and 'alltogether.txt' in l:
                milestones['combine_files'][1] = True
            if milestones['combine_files'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')
        # edit editme.txt
        if not milestones['edit_file'][1]:
            if ('vim' in l or 'nano' in l or 'emacs' in l or 'vi' in l) and 'editme.txt' in l:
                milestones['edit_file'][1] = True
            if milestones['edit_file'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')
        # finding 6 files that have edurange
        if not milestones['find_edurange'][1]:
            if 'find' in l and '-iname' in l and '*edurange*' in l:
                milestones['find_edurange'][1] = True
            if milestones['find_edurange'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')
        if not milestones['final_mission'][1]:
            if 'find' in l and '-iname' in l and '*cowFJS*' in l:
                milestones['final_mission'][1] = True
            if milestones['final_mission'][1]:
                out_str = l[:-1] + " , style=filled, fillcolor=yellow" + l[-1:]
                out.write(out_str + '\n')
        #if not a milestone write to output
        if out_str == "":
            out_str = l
            out.write(out_str + '\n')

def main(input_file):
    with open(input_file) as fp:
        s = fp.read()
    output_file = 'GS_MST_'+input_file
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
