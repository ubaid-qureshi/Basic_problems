list1 = ['<greeting>', 'Hello World!', '</greeting>']
def tag_count(list1):
    count=0
    #xml = '<'
    for xml in list1:
        if xml.startswith("<") and xml.endswith(">"):
            count += 1
    return count

# Test for the tag_count functio..n:

count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))