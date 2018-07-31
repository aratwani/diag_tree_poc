class tree_node:
    def __init__(self, text, id, question, isleaf):
        self.text = text
        self.id = id
        self.question = question
        self.answers = {}
        self.isleaf = isleaf
        pass

    def ask_node_question(self):
        print(self.question)
        if len(self.answers.keys()) > 0:
            i = 0
            temp_dict = {}
            for key in self.answers.keys():
                print(" " + str(i) + " .  " + self.answers[key].text)
                temp_dict[i] = self.answers[key]
                i += 1
            pass
            if len(self.answers.keys()) > 0:
                if not temp_dict[0].isleaf:
                    while(1):
                        try:
                            selection = int(input("\nselect above option:"))
                            return temp_dict[selection]
                        except:
                            print("please select an integer")
            else:
                return None

        pass

    def traverse_tree(self):
        curr = self
        while curr and not curr.isleaf:
            curr = curr.ask_node_question()
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
            curr = curr.ask_node_question()
        pass

    def search_sent(self, sent=""):
        tokens = sent.split('--')
        if tokens[0] == self.root.text:
            curr = self.root
            for idx in range(1, len(tokens)):
                if tokens[idx] in curr.answers:
                    curr = curr.answers[tokens[idx]]
                # traverse tree from here
                curr.traverse_tree()
                pass

        pass
