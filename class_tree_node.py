class tree_node:
    def __init__(self, text, id, question, isleaf):
        self.text = text
        self.id = id
        self.question = question
        self.answers = []
        self.isleaf = isleaf
        pass
    pass


class ym_diag_tree:
    def __init__(self):
        self.root = None
        self.node_map = {}
        pass

    def add_node(self, id, question, text, parent_id, isleaf):
        new_node = tree_node(text, id, question, isleaf)
        if id not in self.node_map:
            self.node_map[id] = new_node
        if not self.root:
            self.root = new_node
        else:
            self.node_map[parent_id].answers.append(new_node)
        pass

    def show_tree(self, root, padding_text):
        if not root:
            return
        else:
            print(padding_text + str(root.text))
            padding_text = "    " + padding_text
            for child in root.answers:
                self.show_tree(child, padding_text)
        pass

    def traverse_tree(self):
        curr = self.root
        while curr and not curr.isleaf:
            selection = 0
            print(curr.question)
            for index, ans in enumerate(curr.answers):
                print("   " + str(index) + ". " + ans.text)
            if len(curr.answers) > 0:
                if not curr.answers[0].isleaf:
                    selection = int(input("\nselect above option:"))
                curr = curr.answers[selection]
            else:
                curr = None
        pass

    def search_sent(self, sent=""):
        tokens = sent.split('--')
        if tokens[0] == self.root.text:
            curr = self.root
            for idx in range(1,len(tokens)):
                pass

        pass
