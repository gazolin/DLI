score = 1.0

safe = open("/home/uri/DLI/server/safe.txt", 'r+')
danger = open("/home/uri/DLI/server/danger.txt", 'r+')

for line in safe:
    if "DLI scores" in line:
        print "<h4> DLI scores this file: " + str(score) + " out of 10.</h4>"
        safe.write("<h4> DLI scores this file: " + str(score) + " out of 10.</h4>")
    else:
        safe.write(line)

safe.close()

for line in danger:
    if "<h4> DLI scores this file: out of 10.</h4>" in line:
        danger.write("<h4> DLI scores this file: " + str(score) + " out of 10.</h4>")
    else:
        danger.write(line)


danger.close()