class QualifiedElement:
    def __init__(self, parents, element):
        self.parents = parents
        self.element = element

class XmlVisitorDiff:
    def comparefiles(self, left, right):

    def comparestrings(self, left, right):

    def compareelements(self, left, right, parents_left = None, parents_right = None, reporter):
        parents_left = parents_left if parents_left is not None else []
        parents_right = parents_right if parents_right is not None else parents_left
        qualified_left = QualifiedElement(left_parents, left)
        qualified_right = QualifiedElement(right_parents, right)
        if left.tag != right.tag:
            reporter.tags_differ(qualified_left, qualified_right)
        for name_left, value_left in left.attrib.items():
            value_right = right.attrib.get(name_left)
            if value_right != value_left:
                reporter.attributes_differ(qualified_left, qualified_right, name_left, value_left, value_right)
        for name_right in right.attrib.keys():
            if name_right not in left.attrib:
                reporter.attributes_differ(qualified_left, qualified_right, name_right, None, right.attrib.get(name_right))
        if not self._text_compare(left.text, right.text):
            reporter.contents_differ(qualified_left, qualified_right)
        if not self._text_compare(left.tail, right.tail):
            reporter.tails_differ(qualified_left, qualified_right)
        left_children = self._getchilddict(left)
        right_children = self._getchilddict(right)
        if len(left_children) != len(right_children):
            reporter.child_counts_differ(qualified_left, qualified_right)
        
      
     
