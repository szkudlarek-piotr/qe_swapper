import os

curdir = os.getcwd()
changed_file = "scf.in"
print(curdir)
file_dir = os.path.join(curdir, changed_file)
r = open(file_dir, "r")
text = r.readlines()
new_text = ""
def swap(attribute, change_to):
    for line in text:
        if attribute in line:
            changed = line.split("=")[-1]
            new_line = line.replace(changed, change_to)
            new_text += new_line
        else:
            new_text += line
swap("tot_charge", "21.37")

print(new_text)