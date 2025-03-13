import random
import requests

class graphGenerator:
    # TODO: Figure out how to write better documentation here
    # What is best practice? 
    # nNodes: number of nodes we want in the graph
    # min: minimum cost
    # max: maximum cost
    def __init__(self, nNodes, min, max):
        print("running init function")
        # initialize an array of empty 0s

        # I think the problem with this approach here is that the inner arrays all
        # referenced the same list, so when I tried to do the modification they were all the same...
        # TODO: Look into this further
        # self.adjMatrix = [[0] * nNodes] * nNodes

        self.adjMatrix = [[] for _ in range(nNodes)]
        self.nNodes = nNodes

        total_cells = nNodes * nNodes
        request_string = f"https://www.random.org/integers/?num={total_cells}&min={min}&max={max}&col=1&base=10&format=plain&rnd=new"
        r = requests.get(request_string)
        print(request_string)
        
        # TODO: Is there a better way to do this?
        random_values = [int(x) for x in r.text.strip().split('\n')]

        # print(random_values)

        # TODO: figure out how to get the random object working. 
        # the problem was, I kept running into each row having the same value
        # so I need to fix that... 
        #random.seed()
        # to populate the matrix with random distances
        for i in range(nNodes):
            #print(f"Current value of i {i}")
            # get a truly random seed from random.org
            #r = requests.get("https://www.random.org/integers/?num=1&min=1&max=10000&col=1&base=10&format=plain&rnd=new")

            # sanitize the output from random.org
            # remove the newline and convert to an integer
            #self.seed = int(r.text.strip())


            #print(f"Current seed {self.seed}")
            # random.seed(self.seed)
            #print(f"Looping... {i}")

            for j in range(nNodes):
                print(self.adjMatrix[i])
                # TODO: This is good enough for now
                # but there has to be a better way to do this...
                random_value_index = i * nNodes + j
                print(f"Current random value index {random_value_index}")

                print(f"Current value of i and j... {i} {j}")


               
                self.adjMatrix[i].append(random_values[random_value_index])

    def __str__(self):

        for i in range(self.nNodes):
            print(self.adjMatrix[i])




    