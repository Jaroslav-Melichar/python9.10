names = "James Smith, Emily Johnson, John Davis, Sarah Wilson, Michael Brown, Jennifer Anderson, William Clark, Olivia Lee, David Taylor, Sophia Martinez"

name_list = names.split(', ')
with open("ukol3.txt", "a") as f:
    for name in name_list:
        f.write(name + '\n')