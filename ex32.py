the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d " %number)

# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# also we can go through mixed list too
# notice we have used %r because we do not know the type
for i in change:
    print("I got %r" % i)

# we can also build list first start with empty one
elements = []

# then use range function to do 0 to 4 count
for i in range(0, 5):
    print("Adding %d to the list" % i)
    # append is the function that list understand
    elements.append(i)

# now we can print out too
for i in elements:
    print("Element was: %d" % i)