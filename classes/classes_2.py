import datetime as dt


class Archangel:
    def __init__(self, fname, party, nname):
        self.name = fname
        self.affiliation = party
        self.nickname = nname
        self.date_created = dt.date.today()
        self.original_affiliation = "Heaven"

    def about_angel(self):
        return self.name + " is affiliated with the " + self.affiliation + \
                           " and sometimes called " + self.nickname + "."


lucifer = Archangel(fname="Lucifer", party="Demons", nname="Satan")

print(lucifer.date_created)
print(lucifer.original_affiliation)

print(lucifer.about_angel())

gabriel = Archangel("Gabriel", "Pagan Gods", "Loki")

print(gabriel.about_angel())
