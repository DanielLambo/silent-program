import os
#dictionary practice
def silentauction():
    bids = {} 
    print("             ___________\n" \
      "             \\         /\n" \
      "              )_______(\n" \
      "              |\"\"\"\"\"\"\"\"|_.-._,.---------.,_.-._\n" \
      "              |       | | |               | | ''-.\n" \
      "              |       |_| |_             _| |_..-'\n" \
      "              |_______| '-' `'---------'` '-'\n" \
      "             )\"\"\"\"\"\"\"\"(\n" \
      "            /_________\\\n" \
      "            `'-------'`\n" \
      "          .-------------.\n" \
      "         /_______________\\")
    names = []
    bidder= []
    name = input("What is your name: ")
    amount = int(input("how much is your bid: $"))
    choice = input("Do you have any other bidders: ")
    names.append(name)
    bidder.append(amount)
    if choice == "yes":
        os.system('clear')
        while choice == "yes":
           name = input("What is your name: ")
           amount = int(input("how much is your bid: $"))
           names.append(name)
           bidder.append(amount)
           choice = input("Do you have any other bidders: ")
           os.system('clear')
    if choice == "no":
        pass
    index = 0
    while index < len(names):
        bids[names[index]] = bidder[index]
        index += 1 
    maxbid = max(bidder)
    indexmaxbid= bidder.index(maxbid)
    return (f'the highest bidder is {names[indexmaxbid]} with a bid of ${maxbid}')


print(silentauction())


  
