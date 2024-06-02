#Stable Marriage Problem
#I made this algorithm acoordin to a YT video
#https://www.youtube.com/watch?v=fudb8DuzQlM

def smp(chr, heros):
    n = len(chr)
    free_chr = list(range(n))
    heros_partner = [-1] * n
    chr_next_proposal = [0] * n

    heros_preferences_ranking = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            heros_preferences_ranking[i][heros[i][j]] = j

    while free_chr:
        c = free_chr[0]
        h = chr[c][chr_next_proposal[c]]

        current_partner = heros_partner[h]
        if current_partner == -1:
            heros_partner[h] = c
            free_chr.pop(0)
        else:
            if heros_preferences_ranking[h][c] < heros_preferences_ranking[h][current_partner]:
                heros_partner[h] = c
                free_chr.pop(0)
                free_chr.append(current_partner)
            else:
                chr_next_proposal[c] += 1
    
    return heros_partner

anakin = [1, 0, 2]
luke = [1, 2, 0]
obiwan = [0, 2, 1]

superman = [1, 0, 2]
ironman = [2, 1, 0]
batman = [0, 2, 1]

chr = [anakin, luke, obiwan]
heros = [superman, ironman, batman]

chr_names = ["Anakin", "Luke", "Obi-Wan"]
heros_names = ["Superman", "Ironman", "Batman"]

matches = smp(chr, heros)

for i in range(len(matches)):
    print(f"{chr_names[i]}'s partner is {heros_names[matches[i]]}")