#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import re
class AboutRegex(Koan):
    """
        This koans are based on the Ben's book: Regular Expressions in 10 minutes.
        I found this books very useful so I decided to write a koans in order to practice everything I had learned from it.
        http://www.forta.com/books/0672325667/
    """
    def test_matching_literal_text(self):
        """
            Lesson 1 Matching Literal String
        """
        string = "Hello, my name is Felix and this koans are based on the Ben's book: Regular Expressions in 10 minutes."
        m = re.search(__, string)
        self.assertTrue(m and m.group(0) and m.group(0)== 'Felix', "I want my name")

    def test_matching_literal_text_how_many(self):
        """
            Lesson 1 How many matches?

            The default behaviour of most regular extression engines is to return just the first match.
            In python you have the next options:

                match()    -->  Determine if the RE matches at the beginning of the string.
                search()   -->  Scan through a string, looking for any location where this RE matches.
                findall()  -->  Find all substrings where the RE matches, and returns them as a list.
                finditer() -->  Find all substrings where the RE matches, and returns them as an iterator.
                
        """
        string = "Hello, my name is Felix and this koans are based on the Ben's book: Regular Expressions in 10 minutes. Repeat My name is Felix"
        m = re.match('Felix', string) #TIP: Maybe match it's not the best option
        self.assertEqual(len(m),2, "I want to know how many times appears my name")

    def test_matching_any_character(self):
        """
            Lesson 1 Matching any character

            . matches any character, alphabetic characters, digits and .
        """
        string = "pecks.xlx\n"    \
                + "orders1.xls\n" \
                + "apec1.xls\n"   \
                + "na1.xls\n"     \
                + "na2.xls\n"     \
                + "sa1.xls"

        #TIP: remember the issue of this lesson
        self.assertEquals(len(re.findall(__, string)),3, "I want to find all files for North America(na) or South America(sa)")

    def test_matching_special_character(self):
        """
            Lesson 1 Matching special character

            Uses \ if you want to match special character
        """
        string = "sales.xlx\n"    \
                + "sales1.xls\n"  \
                + "orders1.xls\n" \
                + "apac1.xls\n" \
                + "sales2.xls\n"  \
                + "na1.xls\n"  \
                + "na2.xls\n"  \
                + "sa1.xls"  
        #TIP you can use the pattern .a. which matches in above test but in this case matches more than you want
        self.assertEquals(len(re.findall(__, string)),3, "I want to find all files for North America(na) or South America(sa)")

    def test_matching_set_character(self):
        """
            Lesson 2 Matching sets of characters

            A set of characters is defined using the metacharacters [ and ]. Everything between them is part of the set and
            any one of the set members must match (but not all).
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
        #TIP you can use the pattern .a. which matches in above test but in this case matches more than you want
        self.assertEquals(len(re.findall(__, string)),3, "I want to find all files for North America(na) or South America(sa), but not (ca)")

    def test_using_character_set_ranges(self):
        """
            Lesson 2 Using character set ranges

            The previous pattern could be [ns]a.\.xls and if a in the list had a file name sam.xls would be matched because the . matches all 
            characters, not just digits. This can be solved with Character sets.
            You can use  this pattern [ns]a[0123456789]\.xls but to simplify you can use a special metacharacter: - (hyphen). i.e [0-9]

            - is only a metacharacter when used between [].

        """
        string = "sales.xlx\n"    \
                + "sales1.xls\n"  \
                + "orders3.xls\n" \
                + "apac1.xls\n" \
                + "sales2.xls\n"  \
                + "na1.xls\n"  \
                + "na2.xls\n"  \
                + "sa1.xls\n"  \
                + "sam.xls\n"  \
                + "ca1.xls"  
        self.assertEquals(len(re.findall(__, string)),3, "I want to find all files for North America(na) or South America(sa), but not (ca)")

    def test_using_multiple_ranges(self):
        """
            Lesson 2 Using character set ranges

            The following are valid ranges:
                A-Z matches all uppercase characters from A to Z
                a-z matches all uppercase characters from a to z
                A-F matches all uppercase characters from A to F
                A-z matches all uppercase characters from A to z. This pattern also includes characters such as [ and ^
                Any two ASCII characters may be specified as the range start and end.

        """
        string = '<BODY BGCOLOR="#336633" TEXT="#FFFFFF" MARGINWIDTH="0" MARGINHEIGHT="0" TOPMARGIN="0" LEFTMARGIN="0">'
        self.assertEquals(len(re.findall(__, string)),2, "I want to find all the colors in RGB")

