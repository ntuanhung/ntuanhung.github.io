---
permalink: /notes/
title: "Notes"
author_profile: true
redirect_from: 
  - /nt/
  - /notes.html
---

# Mimimal-mistake notes

## TODO

+ Support multiple languages: https://www.sylvaindurand.org/making-jekyll-multilingual/
+ Insert navigation functions

## Locations of key files/directories

* Basic config options: _config.yml
* Top navigation bar config: _data/navigation.yml
* Single pages: _pages/
* Collections of pages are .md or .html files in:
  * _publications/
  * _portfolio/
  * _posts/
  * _teaching/
  * _talks/
* Footer: _includes/footer.html
* Static files (like PDFs): /files/
* Profile image (can set in _config.yml): images/profile.png

## Tips and hints

* Name a file ".md" to have it render in markdown, name it ".html" to render in HTML.
* Go to the [commit list](https://github.com/academicpages/academicpages.github.io/commits/master) (on your repo) to find the last version Github built with Jekyll. 
  * Green check: successful build
  * Orange circle: building
  * Red X: error
  * No icon: not built

## Resources
 * [Liquid syntax guide](https://shopify.github.io/liquid/tags/control-flow/)

## HTML using Template Tags 
This syntax is based on jinja, known as Template Engine system. An example code as follows:


### Benefits of using template engines include:

+ Encouraging organization of source code into operationally-distinct layers (see e.g., MVC)
+ Enhancing productivity by reducing unnecessary reproduction of effort
+ Enhancing teamwork by allowing separation of work based on skill-set (e.g., artistic vs. technical)


### Typical features

Template engines typically include features common to most high-level programming languages, with an emphasis on features for processing plain text. Such features include:

+ variables and functions
+ text replacement
+ file inclusion (or transclusion)
+ conditional evaluation and loops

# Markdown notes

## Markdown headers

### Header three

#### Header four

##### Header five

###### Header six

## Blockquotes

Single line blockquote:

> Quotes are cool.

## Tables

### Table 1

| Entry            | Item   |                                                              |
| --------         | ------ | ------------------------------------------------------------ |
| [John Doe](#)    | 2016   | Description of the item in the list                          |
| [Jane Doe](#)    | 2019   | Description of the item in the list                          |
| [Doe Doe](#)     | 2022   | Description of the item in the list                          |

### Table 2

| Header1 | Header2 | Header3 |
|:--------|:-------:|--------:|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|-----------------------------|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|=============================|
| Foot1   | Foot2   | Foot3   |

## Definition Lists

Definition List Title
:   Definition list division.

Startup
:   A startup company or startup is a company or temporary organization designed to search for a repeatable and scalable business model.

#dowork
:   Coined by Rob Dyrdek and his personal body guard Christopher "Big Black" Boykins, "Do Work" works as a self motivator, to motivating your friends.

Do It Live
:   I'll let Bill O'Reilly [explain](https://www.youtube.com/watch?v=O_HyZ5aW76c "We'll Do It Live") this one.

## Unordered Lists (Nested)

  * List item one 
      * List item one 
          * List item one
          * List item two
          * List item three
          * List item four
      * List item two
      * List item three
      * List item four
  * List item two
  * List item three
  * List item four

## Ordered List (Nested)

  1. List item one 
      1. List item one 
          1. List item one
          2. List item two
          3. List item three
          4. List item four
      2. List item two
      3. List item three
      4. List item four
  2. List item two
  3. List item three
  4. List item four

## Buttons

Make any link standout more when applying the `.btn` class.

## Notices

**Watch out!** You can also add notices by appending `{: .notice}` to a paragraph.
{: .notice}

## Emoji

+ https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#symbols

## HTML Tags

### Address Tag

<address>
  1 Infinite Loop<br /> Cupertino, CA 95014<br /> United States
</address>

### Anchor Tag (aka. Link)

This is an example of a [link](http://github.com "Github").

### Abbreviation Tag

The abbreviation CSS stands for "Cascading Style Sheets".

*[CSS]: Cascading Style Sheets

### Cite Tag

"Code is poetry." ---<cite>Automattic</cite>

### Code Tag

You will learn later on in these tests that `word-wrap: break-word;` will be your best friend.

### Strike Tag

This tag will let you <strike>strikeout text</strike>.

### Emphasize Tag

The emphasize tag should _italicize_ text.

### Insert Tag

This tag should denote <ins>inserted</ins> text.

### Keyboard Tag

This scarcely known tag emulates <kbd>keyboard text</kbd>, which is usually styled like the `<code>` tag.

### Preformatted Tag

This tag styles large blocks of code.

<pre>
.post-title {
  margin: 0 0 5px;
  font-weight: bold;
  font-size: 38px;
  line-height: 1.2;
  and here's a line of some really, really, really, really long text, just to see how the PRE tag handles it and to find out how it overflows;
}
</pre>

### Quote Tag

<q>Developers, developers, developers&#8230;</q> &#8211;Steve Ballmer

### Strong Tag

This tag shows **bold text**.

### Subscript Tag

Getting our science styling on with H<sub>2</sub>O, which should push the "2" down.

### Superscript Tag

Still sticking with science and Isaac Newton's E = MC<sup>2</sup>, which should lift the 2 up.

### Variable Tag

This allows you to denote <var>variables</var>.

# LaTeX notes

## IEEETrans guidance

+ General guidance https://www.icmu.org/icmu2014/files/IEEEtran_HOWTO.pdf
+ Greek synbols https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols

### Cross referencing
https://www.overleaf.com/learn/latex/Cross%20referencing%20sections,%20equations%20and%20floats#Referencing_equations.2C_figures_and_tables

### List and Numbering
+ https://www.overleaf.com/learn/latex/lists#Ordered_lists_2
+ https://tex.stackexchange.com/questions/54055/using-lower-case-roman-numerals-in-enumerate-lists

### Figure
+ Import PNG image https://tex.stackexchange.com/questions/329186/inserting-png-file-as-is
+ Subfloat using https://tex.stackexchange.com/questions/119984/subfigures-side-by-side-with-captions
+ Using \columnwidth \pagewidth \textwidth for resize figure.

### Hyperlink
+ https://tex.stackexchange.com/questions/85553/undefined-control-sequence-url-error

### Bibtex
+ https://www.overleaf.com/learn/latex/bibliography_management_with_bibtex
+ https://www.openoffice.org/bibliographic/bibtex-defs.html