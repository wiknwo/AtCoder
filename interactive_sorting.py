'''Interactive Sorting

    William Ikenna-Nwosu (wiknwo)
'''
def main():
    data = []
    data = input("").split(" ")
    N = int(data[0])
    Q = int(data[1])
    sortedstr = []

    # Creating string to sort
    for i in range(N):
        sortedstr.append(str(chr(65 + i)))
    
    # Sorting
    for i in range(N):
        for j in range(i + 1, N - 1):
            print("? {} {}".format(sortedstr[i], sortedstr[j]), flush=True)
            ans = input("")
            # c1 is heavier than the ball c2
            if ans == '>':
                sortedstr[i], sortedstr[j] = sortedstr[j], sortedstr[i]
            # c2 is heavier than the ball c1
            elif ans == '<':
                pass

    # Print sorted string
    print("! {}".format(''.join(sortedstr)), flush=True)
        
if __name__ == '__main__':
    main()