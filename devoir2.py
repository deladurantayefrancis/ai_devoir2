import random
import sys

if len(sys.argv) != 3:
    print "\n --- Execution de la forme :\n" \
          "       python devoir2.py (rejet | ponderation) nb_echantillons\n"
    quit(1)

PB = .001

PE = .002

PA = [[.001, .29],
      [.94,  .95]]

PJ = [.05, .90]

PM = [.01, .7]


B_cnt = 0  # burglary count
nB_cnt = 0  # no burglary count
result = 0

if sys.argv[1] == 'rejet':

    i = 0

    while i < int(sys.argv[2]):

        B, E, A, J, M = False, False, False, False, False

        if random.random() < PB:
            B = True
        if random.random() < PE:
            E = True
        if random.random() < PA[B][E]:
            A = True
        if random.random() < PJ[A]:
            J = True
        if random.random() < PM[A]:
            M = True

        if J and not E:
            B_cnt += B
            i += 1

    result = B_cnt / float(sys.argv[2])

elif sys.argv[1] == 'ponderation':

    for i in range(int(sys.argv[2])):

        values = {'B': None, 'E': False, 'A': None, 'J': True, 'M': None}
        w = 1

        for var in 'BEAJM':

            if var is 'B':
                p = PB
            elif var is 'E':
                p = PE
            elif var is 'A':
                p = PA[values['B']][values['E']]
            elif var is 'J':
                p = PJ[values['A']]
            else:
                p = PM[values['A']]

            if values[var] is None:
                # draw the value according to distribution
                values[var] = random.random() < p
            else:
                # otherwise update the weight
                if values[var]:
                    w *= p
                else:
                    w *= 1 - p

        if values['B']:
            B_cnt += w
        else:
            nB_cnt += w

    result = B_cnt / (B_cnt + nB_cnt)

else:
    print "\n --- Le premier parametre doit etre 'rejet' ou 'ponderation'\n"
    quit(1)

# final result
print "\n --- Probabilite obtenue : " + str(result) + "\n"
