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

    def test_matching_literal_text_not_case_sensitivity(self):
        """
            Lesson 1 Matching Literal String non case sensitivity.
            Most regex implementations also support matches that are not case sensitive. In python you can use re.IGNORECASE, in
            Javascript you can specify the optional i flag.
            In Ben's book you can see more languages.

        """
        string = "Hello, my name is Felix or felix and this koans are based on the Ben's book: Regular Expressions in 10 minutes."
        self.assertEqual(len(re.findall("felix", string,__)),2, "I want my name")
                                              
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


    def test_anything_but_matching(self):
        """
            Lesson 2 Using character set ranges
            Occsionally, you'll want a list of characters that you don't want to match. 
            Character sets can be negated using the ^ metacharacter.

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
        m = re.search(__, string)
        self.assertTrue(m and m.group(0) and m.group(0)== 'sam.xls', "I want to find the name sam")

    def using_metacharacters_escaping(self):
        """
            Lesson 3 Using metacharacters

            Metacharacters are characters that have special meaning within regular expressions.
            
            Metacharacters can be escaped by preceding them with a backslash, therefore \. matches . 
        """
        string = "var myArray = new Array();\n"    \
                + "if (myArray[0]) { \n"  \
                + "}" 
        m = re.search("myArray[0]", string) #TIP: This pattern  matches "myArray0" because [ and ] are metacharacters
        self.assertTrue(m and m.group(0) and m.group(0)== 'myArray[0]', "I want to find myArray[0]")

    def using_metacharacters_matching_white_spaces(self):
        """
            Lesson 3 Matching whitespace character

            Sometimes you'll have to match nonprinting whitespace characters embedded in your text. For example tab characters
            or line breaks .
            In this cases you can use these special metacharacters: 
                [\b]   Backspace
                \f     Form feed
                \n     Line feed
                \r     Carriage return
                \t     Tab
                \v     Vertical tab
            
        """
        f = open('koans/regex_cvs', 'r')
        string = f.read()
        #This text contains a series of records in comma-delimited format (cvs). Before processing the records, you need
        # to remove any blank lines in the data. 
        m = re.search("", string)         
        self.assertTrue(m and m.group(0) and m.group(0)== '\n\n', "I want to find the blank lines")

    def using_metacharacters_matching_digits(self):
        """
            Lesson 3 Using metacharacters

            As you have seen in Lesson 2, [0-9] is a shorcut for [0123456789] and is used to match any digit. 
            To match anything other than a digit, the set can be negated as [^0-9].
            With the next metacharacters you can do the same:
                \d match any digit (same as [0-9])
                \D match any nondigit (same as [0-9])
        """
        string = "var myArray = new Array();\n"    \
                + "if (myArray[0]) { \n"  \
                + "    alert('Learning regex'); \n" \
                + "} \n"   \
                + "if (myArray[1]) { \n"  \
                + "    alert('With this great book');\n" \
                + "} \n"  
        
        self.assertEquals( len(re.findall(__, string)), 2, "I want to find all uses of myArray")


    def using_metacharacters_matching_alphanumeric_characters(self):
        """
            Lesson 3 Using metacharacters

            Like with the digits you have special characters for alphanumeric characters:
                \w Any alphanumeric character in uppercase or lowercase and underscore: [a-zA-Z0-9_]
                \W Any nonalphanumeric or underscore character: [^a-zA-Z0-9_]
            
            Here you have a list of IDs made of 3 characters/digits/underscores, 1 hyphen and 3 characters/digits/underscores: 
                A1A-B_A or BA_-2e3 or 1_2-34R
        """
        string = "A_1-DRA\n" \
                +"A01-2ER\n" \
                +"A01-(4d\n" \
                +"B11=223\n" \
                +"A1A-B_A\n" \
                +"1_2-34R\n" \
                +"BA_-2e3"

        self.assertEquals( len(re.findall(__, string)), 5, "I want to find the ids") 
