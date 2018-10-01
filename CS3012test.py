    import CS3012


def test_answer():
    # build a sample tree                                            it looks like this
    root = CS3012.Node(1)                                                    #1
    root.left = CS3012.Node(2)                   #                      /           \
    root.right = CS3012.Node(3)                                       #2             #3
    root.left.left = CS3012.Node(4)              #                  /   \           /  \
    root.left.right = CS3012.Node(5)                              #4    #5        #6    #7
    root.right.left = CS3012.Node(6)
    root.right.right = CS3012.Node(7)


    # test lca in straight line tree

    one = CS3012.Node(1)
    two = CS3012.Node(2)
    three = CS3012.Node(3)
    four = CS3012.Node(4)
    five = CS3012.Node(5)

    root = one                                          #it looks like this
    root.right = two                                     #1-2-3-4-5
    root.right.right = three
    root.right.right.right = four
    root.right.right.right.right = five

    assert CS3012.findLCA(root, 3, 5) == 3

    # test lca between nodes that aren't on the same tier of the tree

    assert CS3012.findLCA(root, 5, 3) == 3

    # test lca between a node and itself

    assert CS3012.findLCA(root, 4, 4) == 4

    # test lca between non-existent nodes

    assert CS3012.findLCA(root, 6, 7) == -1

    # test lca between one existing node and one non-existing node

    assert CS3012.findLCA(root, 4, 8) == -1

    # test lca between a parent node and its child

    assert CS3012.findLCA(root, 4, 5) == 4

    # test lca in 3-node tree

    root = one
    root.left = two
    root.right = three
    two.right = None
    two.left = None
    three.right = None
    three.left = None

    assert CS3012.findLCA(root, 2, 3) == 1

    # test lca between the root and another node

    assert CS3012.findLCA(root, 1, 3) == 1

    # test lca between two nodes in an invalid tree

    root = CS3012.Node(10)                                      #looks like this
    root.right = CS3012.Node(11)                            #10-11-12-13        15
    root.right.right = CS3012.Node(12)                      #       |
    root.right.right.right = CS3012.Node(13)                #       14
    root.right.right.left = CS3012.Node(14)

    loner = CS3012.Node(15)

    assert CS3012.findLCA(root, 12, 15) == -1

    # test lca when root is null

    assert CS3012.findLCA(None, 10, 11) == -1


