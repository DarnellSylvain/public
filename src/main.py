from textnode import TextNode
from inline_markdown import extract_markdown_images, extract_markdown_links


def main():
    textNode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    extract_markdown_images(text)

    text1 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    extract_markdown_links(text1)


main()
