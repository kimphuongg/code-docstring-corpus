#! /usr/bin/python

import sys

def main():
    if len(sys.argv) != 10:
        usage()

    decl_fs = open(sys.argv[1])
    desc_fs = open(sys.argv[2])
    bodies_fs = open(sys.argv[3])
    meta_fs = open(sys.argv[4])
    repos_fs = open(sys.argv[5])
    out_decl_fs = open(sys.argv[6], "w")
    out_desc_fs = open(sys.argv[7], "w")
    out_bodies_fs = open(sys.argv[8], "w")
    out_meta_fs = open(sys.argv[9], "w")

    decl = decl_fs.readlines()
    desc = desc_fs.readlines()
    bodies = bodies_fs.readlines()
    meta = meta_fs.readlines()
    repos = repos_fs.readlines()

    repo_set = set([repo.strip() for repo in repos])
    for i in xrange(len(decl)):
        src_file = meta[i].split()[0]
        repo = '/'.join(src_file.split('/')[:3])
        if repo not in repo_set:
            continue
        print >> out_decl_fs, decl[i].strip()
        print >> out_desc_fs, desc[i].strip()
        print >> out_bodies_fs, bodies[i].strip()
        print >> out_meta_fs, meta[i].strip()
        

def usage():
    print >> sys.stderr, "Usage:"
    print >> sys.stderr, sys.argv[0], "declarations-file descriptions-file bodies-file metadata-file repos out-declarations-file out-descriptions-file out-bodies-file out-metadata-file"
    sys.exit(-1)

if __name__ == '__main__':
    main()


