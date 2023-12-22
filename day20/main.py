with open('data.txt') as f:
    lines = f.readlines()


def solve():
    modules = {}
    links = {}
    pulses = []
    for line in lines:
        p1 = line.split("-")[0][1:].replace(" ", "")
        print(p1)
        mod = line.rstrip().replace(" ", "").split(">")[1].split(",")
        if line[0] == "%":
            modules[p1] = ["fp", False]
            links[p1] = mod

        if line[0] == "&":
            modules[p1] = ["cj", {}]
            links[p1] = mod

        if p1 == "roadcaster":
            links["b" + p1] = mod
    for line in lines:
        p1 = line.split("-")[0][1:].replace(" ", "")
        mod = line.rstrip().replace(" ", "").split(">")[1].split(",")
        for m in mod:
            if m in modules.keys():
                if modules[m][0] == "cj":
                    modules[m][1][p1] = "low"

    low = 0
    high = 0

    for i in range(0, 1000):
        pulses.append("broadcaster")

        low += 1
        for link in links[pulses[0]]:
            pulses.append((link, "low", "broadcaster"))
            low += 1
        pulses.pop(0)

        while pulses:
            m = pulses[0][0]
            signal = pulses[0][1]
            sender = pulses[0][2]

            print(sender, "->", signal, "->", m)
            if m in modules.keys():

                if modules[m][0] == "fp" and signal == "low":
                    if modules[m][1]:
                        for link in links[m]:
                            pulses.append((link, "low", m))
                            low += 1
                    else:
                        for link in links[m]:
                            pulses.append((link, "high", m))
                            high += 1
                    modules[m][1] = not modules[m][1]
                    pulses.pop(0)

                elif modules[m][0] == "fp":
                    pulses.pop(0)

                elif modules[m][0] == "cj":
                    modules[m][1][sender] = signal
                    sendOk = True
                    for k, v in modules[m][1].items():
                        if v != "high":
                            sendOk = False
                    if not sendOk:
                        for link in links[m]:
                            pulses.append((link, "high", m))
                            high += 1
                    else:
                        for link in links[m]:
                            pulses.append((link, "low", m))
                            low += 1

                    pulses.pop(0)

            else:
                pulses.pop(0)
        print("\n")
        print(low, high)
        print(low * high)



solve()
