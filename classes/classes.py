class Archangel:
    """ Create a new archangel with first name and affiliation """
    def __init__(self, fname, affiliation, nname):
        # define attributes, give them values
        self.first_name = fname
        self.affiliation = affiliation
        self.nickname = nname


michael = Archangel(fname="Michael", affiliation="Heaven",
                    nname="The Boss Man")
lucifer = Archangel(fname="Lucifer", affiliation="Hell", nname="Satan")
gabriel = Archangel(fname="Gabriel", affiliation="Pagans", nname="Loki")
raphael = Archangel(fname="Raphael", affiliation="Heaven",
                    nname="Ruler of Heaven")

print(michael.affiliation)
print(gabriel.nickname)

michael_2 = Archangel("Michael", "Alternate World", "The Cleanser of Worlds")

print(michael_2.nickname)

michael_2.nickname = "The Commander of the Host"

print(michael_2.nickname)
