class tree_node:
    def __init__(self, text, id, question, isleaf):
        self.text = text
        self.id = id
        self.question = question
        self.answers = {}
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
            self.node_map[parent_id].answers[new_node.text] = new_node
        pass

    def show_tree(self, root, padding_text):
        if not root:
            return
        else:
            print(padding_text + str(root.text))
            padding_text = "    " + padding_text
            for child in root.answers.keys():
                self.show_tree(root.answers[child], padding_text)
        pass

    def traverse_tree(self):
        curr = self.root
        while curr and not curr.isleaf:
            selection = 0
            print(curr.question)
            temp_dict = {}
            i = 0
            for ans in curr.answers.keys():
                print("   " + str(i) + "." + curr.answers[ans].text)
                temp_dict[i] = curr.answers[ans].text
                i += 1
            if len(curr.answers.keys()) > 0:
                if not curr.answers[temp_dict[0]].isleaf:
                    selection = int(input("\nselect above option:"))
                curr = curr.answers[temp_dict[selection]]
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
