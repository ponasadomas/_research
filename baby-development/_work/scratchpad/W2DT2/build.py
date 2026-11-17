def build(src,out,rows,default=None):
    ids=[l.split(' | ')[0] for l in open(src)]
    assert set(ids)==set(rows) and len(ids)==len(rows),set(ids)^set(rows)
    open(out,'w').write(''.join(f"{i}\t{rows[i][0]}\t{rows[i][1]}\n" for i in ids))
