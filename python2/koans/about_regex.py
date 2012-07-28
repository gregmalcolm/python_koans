#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

import re


class AboutRegex(Koan):
    """
        These koans are based on Ben's book: Regular Expressions in 10
        minutes. I found this book very useful, so I decided to write
        a koan file in order to practice everything it taught me.
        http://www.forta.com/books/0672325667/
    """

    def test_matching_literal_text(self):
        """
            Lesson 1 Matching Literal String
        """
        string = "Hello, my name is Felix and these koans are based " + \
        "on Ben's book: Regular Expressions in 10 minutes."
        m = re.search(__, string)
        self.assertTrue(
            m and m.group(0) and
                m.group(0) == 'Felix',
            "I want my name")

    def test_matching_literal_text_how_many(self):
        """
            Lesson 1 -- How many matches?

            The default behaviour of most regular extression engines is
            to return just the first match. In python you have the
            following options:

                match()    -->  Determine if the RE matches at the
                                beginning of the string.
                search()   -->  Scan through a string, looking for any
                                location where this RE matches.
                findall()  -->  Find all substrings where the RE
                                matches, and return them as a list.
                finditer() -->  Find all substrings where the RE
                                matches, and return them as an iterator.
        """
        string = ("Hello, my name is Felix and these koans are based " +
            "on Ben's book: Regular Expressions in 10 minutes. " +
            "Repeat My name is Felix")
        m = re.match('Felix', string)  # TIP: match may not be the best option

        # I want to know how many times my name appears
        self.assertEqual(m, __)

    def test_matching_literal_text_not_case_sensitivity(self):
        """
            Lesson 1 -- Matching Literal String non case sensitivity.
            Most regex implementations also support matches that are not
            case sensitive. In python you can use re.IGNORECASE, in
            Javascript you can specify the optional i flag. In Ben's
            book you can see more languages.

        """
        string = "Hello, my name is Felix or felix and this koan " + \
            "is based on Ben's book: Regular Expressions in 10 minutes."

        self.assertEqual(re.findall("felix", string, 20), __)
        self.assertEqual(re.findall("felix", string, 10), __)

    def test_matching_any_character(self):
        """
            Lesson 1: Matching any character

            `.` matches any character: alphabetic characters, digits,
            and punctuation.
        """
        string = "pecks.xlx\n"    \
                + "orders1.xls\n" \
                + "apec1.xls\n"   \
                + "na1.xls\n"     \
                + "na2.xls\n"     \
                + "sa1.xls"

        # I want to find all uses of myArray
        change_this_search_string = 'a..xlx'
        self.assertEquals(
            len(re.findall(change_this_search_string, string)),
            3)

    def test_matching_set_character(self):
        """
            Lesson 2 -- Matching sets of characters

            A set of characters is defined using the metacharacters
            `[` and `]`. Everything between them is part of the set, and
            any single one of the set members will match.
        """
        string = "sales.xlx\n"    \
                + "sales1.xls\n"  \
                + "orders3.xls\n" \
                + "apac1.xls\n" \
                + "sales2.xls\n"  \
                + "na1.xls\n"  \
                + "na2.xls\n"  \
                + "sa1.xls\n"  \
                + "ca1.xls"
        # I want to find all files for North America(na) or South
        # America(sa), but not (ca) TIP you can use the pattern .a.
        # which matches in above test but in this case matches more than
        # you want
        change_this_search_string = '[nsc]a[2-9].xls'
        self.assertEquals(
            len(re.findall(change_this_search_string, string)),
            3)

    def test_anything_but_matching(self):
        """
            Lesson 2 -- Using character set ranges
            Occasionally, you'll have a list of characters that you don't
            want to match. Character sets can be negated using the ^
            metacharacter.

        """
        string = "sales.xlx\n"    \
                + "sales1.xls\n"  \
                + "orders3.xls\n" \
                + "apac1.xls\n" \
                + "sales2.xls\n"  \
                + "sales3.xls\n"  \
                + "europe2.xls\n"  \
                + "sam.xls\n"  \
                + "na1.xls\n"  \
                + "na2.xls\n"  \
                + "sa1.xls\n"  \
                + "ca1.xls"

        # I want to find the name 'sam'
        change_this_search_string = '[^nc]am'
        self.assertEquals(
            re.findall(change_this_search_string, string),
            ['sam.xls'])
