def rev_name(name):
    y = name.split()
    rev = y[::-1]
    return " ".join(rev)

name = ["swostik nepal","rahul jaiker","ram khanal"]
list(map(rev_name,names))