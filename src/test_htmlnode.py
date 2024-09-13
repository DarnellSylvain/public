import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "p", "Some text in paragraph", None, {"className": "text-white", "key": "1"}
        )
        node2 = HTMLNode("p", "Some text in paragraph", None, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node2.props, None)

    def test_props_to_html(self):
        node = HTMLNode(
            "p", "Some text in paragraph", None, {"className": "text-white", "key": "1"}
        )
        self.assertEqual(node.props_to_html(), ' className="text-white" key="1"')

    def test_repr(self):
        node = HTMLNode(
            "p", "Some text in paragraph", [], {"className": "text-white", "key": "1"}
        )
        self.assertEqual(
            node.__repr__(),
            'HTMLNode(p, Some text in paragraph, [], className="text-white" key="1")',
        )

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_no_props(self):
        node3 = LeafNode(None, value="This is text without a tag")
        self.assertEqual(node3.to_html(), "This is text without a tag")

    def test_to_html_with_props(self):
        node2 = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com", "className": "uppercase"},
        )
        self.assertEqual(
            node2.to_html(),
            '<a href="https://www.google.com" className="uppercase">Click me!</a>',
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
