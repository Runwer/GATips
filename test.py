testlist = [[u'(direct)', 222], [u'Facebook', 73], [u'ekstrabladet.dk', 49], [u'google', 34], [u'Twitter', 20], [u'ni_krak', 20], [u'agf.dk', 9], [u'jyllands-posten.dk', 6], [u'footballworld.dk', 3], [u'fcbarcelona.dk', 2], [u'90minutter.dk', 1], [u'alleroed.lokalavisen.dk', 1], [u'clubnews.dk', 1], [u'danskfodbold.com', 1], [u'lokalavisen.dk', 1]]
print [x[1] for x in testlist if x[0] == 'Facebook']
