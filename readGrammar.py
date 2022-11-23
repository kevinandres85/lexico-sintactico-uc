d = {}
with open("analizador-lexico/datos.txt") as f:
    for line in f:
        rule = line.replace("\n","")
        (key, val) = rule.split(":")
        prod = val.split("|")
        nt = []
        for x in prod:
            p = x.replace(" ", "").split(",")
            nt.append(p)
            d[str(key)] = nt
